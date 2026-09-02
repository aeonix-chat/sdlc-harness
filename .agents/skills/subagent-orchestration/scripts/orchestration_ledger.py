#!/usr/bin/env python3
"""Initialize and validate a transparent Codex subagent run ledger."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any


SCHEMA_VERSION = 1
EFFORTS = {"none", "minimal", "low", "medium", "high", "xhigh", "max", "ultra"}
EVENTS = {
    "planned", "approved", "spawned", "working", "steered",
    "needs_attention", "completed", "failed", "interrupted", "integrated",
}
TERMINAL_EVENTS = {"completed", "failed", "interrupted"}
TASK_EVENTS = EVENTS - {"planned", "approved"}
AGENT_FIELDS = {
    "task_name", "objective", "model", "reasoning_effort", "fork_turns",
    "permission_mode", "owned_paths", "forbidden_paths", "prompt_file",
    "acceptance_criteria", "timeout_minutes", "max_retries",
    "allow_nested_delegation",
}
TOP_FIELDS = {
    "schema_version", "run_id", "objective", "repository", "baseline",
    "approval", "integration_owner", "max_concurrency", "nested_delegation",
    "agents",
}


class ContractError(ValueError):
    """Raised when a manifest or event violates the run contract."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ContractError(f"cannot read JSON from {path}: {error}") from error
    if not isinstance(value, dict):
        raise ContractError(f"{path} must contain a JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_fields(value: dict[str, Any], required: set[str], label: str) -> None:
    missing = sorted(required - value.keys())
    if missing:
        raise ContractError(f"{label} is missing required fields: {', '.join(missing)}")


def relative_path(value: Any, label: str) -> PurePosixPath:
    if not isinstance(value, str) or not value:
        raise ContractError(f"{label} must be a non-empty string")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise ContractError(f"{label} must be repository-relative and must not contain '..'")
    return path


def roots_overlap(left: PurePosixPath, right: PurePosixPath) -> bool:
    shared = min(len(left.parts), len(right.parts))
    return left.parts[:shared] == right.parts[:shared]


def validate_manifest(manifest: dict[str, Any], base: Path | None = None) -> None:
    require_fields(manifest, TOP_FIELDS, "manifest")
    if manifest["schema_version"] != SCHEMA_VERSION:
        raise ContractError(f"unsupported schema_version: {manifest['schema_version']!r}")
    if not isinstance(manifest["run_id"], str) or not manifest["run_id"].strip():
        raise ContractError("run_id must be a non-empty string")
    if not isinstance(manifest["max_concurrency"], int) or manifest["max_concurrency"] < 1:
        raise ContractError("max_concurrency must be a positive integer")
    if manifest["nested_delegation"] is not False:
        raise ContractError("locked runs require nested_delegation=false")

    baseline = manifest["baseline"]
    if not isinstance(baseline, dict):
        raise ContractError("baseline must be an object")
    require_fields(baseline, {"branch", "commit", "dirty"}, "baseline")
    if not isinstance(baseline["dirty"], bool):
        raise ContractError("baseline.dirty must be boolean")

    approval = manifest["approval"]
    if not isinstance(approval, dict):
        raise ContractError("approval must be an object")
    require_fields(approval, {"required", "status", "approved_by", "approved_at"}, "approval")
    if approval["required"] is not True:
        raise ContractError("locked runs require approval.required=true")
    if approval["status"] not in {"pending", "approved"}:
        raise ContractError("approval.status must be pending or approved")
    if approval["status"] == "approved" and (
        not approval["approved_at"] or not approval["approved_by"]
    ):
        raise ContractError("approved manifests require approval.approved_by and approved_at")

    agents = manifest["agents"]
    if not isinstance(agents, list) or not agents:
        raise ContractError("agents must be a non-empty list")
    if manifest["max_concurrency"] > len(agents):
        raise ContractError("max_concurrency cannot exceed the number of agents")

    names: set[str] = set()
    owned: list[tuple[str, PurePosixPath]] = []
    for index, agent in enumerate(agents):
        label = f"agents[{index}]"
        if not isinstance(agent, dict):
            raise ContractError(f"{label} must be an object")
        require_fields(agent, AGENT_FIELDS, label)
        name = agent["task_name"]
        if not isinstance(name, str) or not name:
            raise ContractError(f"{label}.task_name must be a non-empty string")
        if name in names:
            raise ContractError(f"duplicate task_name: {name}")
        names.add(name)
        if not isinstance(agent["model"], str) or not agent["model"]:
            raise ContractError(f"{label}.model must be explicit")
        if not isinstance(agent["permission_mode"], str) or not agent["permission_mode"]:
            raise ContractError(f"{label}.permission_mode must be explicit")
        if agent["reasoning_effort"] not in EFFORTS:
            raise ContractError(f"{label}.reasoning_effort must be explicit and supported")
        fork = agent["fork_turns"]
        if fork not in {"none", "all"} and not (
            isinstance(fork, str) and fork.isdigit() and int(fork) > 0
        ):
            raise ContractError(f"{label}.fork_turns must be none, all, or a positive integer string")
        if agent["allow_nested_delegation"] is not False:
            raise ContractError(f"{label}.allow_nested_delegation must be false in a locked run")
        if not isinstance(agent["timeout_minutes"], int) or agent["timeout_minutes"] < 1:
            raise ContractError(f"{label}.timeout_minutes must be a positive integer")
        if not isinstance(agent["max_retries"], int) or agent["max_retries"] < 0:
            raise ContractError(f"{label}.max_retries must be a non-negative integer")
        if not isinstance(agent["acceptance_criteria"], list) or not agent["acceptance_criteria"]:
            raise ContractError(f"{label}.acceptance_criteria must be a non-empty list")
        for field in ("owned_paths", "forbidden_paths"):
            if not isinstance(agent[field], list):
                raise ContractError(f"{label}.{field} must be a list")
            for raw_path in agent[field]:
                path = relative_path(raw_path, f"{label}.{field}")
                if field == "owned_paths":
                    owned.append((name, path))
        if agent["permission_mode"] == "read-only" and agent["owned_paths"]:
            raise ContractError(f"{label} is read-only but declares owned_paths")
        prompt = relative_path(agent["prompt_file"], f"{label}.prompt_file")
        if base is not None and not (base / prompt).is_file():
            raise ContractError(f"{label}.prompt_file does not exist: {prompt}")

    for index, (left_name, left_path) in enumerate(owned):
        for right_name, right_path in owned[index + 1 :]:
            if left_name != right_name and roots_overlap(left_path, right_path):
                raise ContractError(
                    f"write ownership overlaps: {left_name}:{left_path} and "
                    f"{right_name}:{right_path}"
                )


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def append_event(run_dir: Path, event: str, task_name: str | None, details: dict[str, Any]) -> None:
    if event not in EVENTS:
        raise ContractError(f"unsupported event type: {event}")
    manifest = load_json(run_dir / "manifest.json")
    validate_manifest(manifest, run_dir)
    if event not in {"planned", "approved"} and manifest["approval"]["status"] != "approved":
        raise ContractError(f"cannot record {event} before the run is approved")
    names = {agent["task_name"] for agent in manifest["agents"]}
    if task_name is not None and task_name not in names:
        raise ContractError(f"event references unknown task_name: {task_name}")
    if event in TASK_EVENTS and task_name is None:
        raise ContractError(f"{event} events require task_name")
    if event not in TASK_EVENTS and task_name is not None:
        raise ContractError(f"{event} events must not include task_name")

    history = read_events(run_dir / "events.ndjson")
    task_history = [item["event"] for item in history if item.get("task_name") == task_name]
    terminal_seen = any(item in TERMINAL_EVENTS for item in task_history)
    if event == "spawned" and task_history:
        raise ContractError(f"{task_name} already has lifecycle events")
    if event in {"working", "steered", "needs_attention"} and (
        "spawned" not in task_history or terminal_seen
    ):
        raise ContractError(f"cannot record {event} for {task_name} in its current state")
    if event in TERMINAL_EVENTS and ("spawned" not in task_history or terminal_seen):
        raise ContractError(f"cannot record {event} for {task_name} in its current state")
    if event == "integrated" and (not terminal_seen or "integrated" in task_history):
        raise ContractError(f"cannot record integrated for {task_name} in its current state")
    record = {
        "schema_version": SCHEMA_VERSION,
        "timestamp": utc_now(),
        "event": event,
        "task_name": task_name,
        "details": details,
    }
    with (run_dir / "events.ndjson").open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, sort_keys=True) + "\n")


def read_events(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise ContractError("run ledger is missing events.ndjson")
    events: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError as error:
            raise ContractError(f"events.ndjson:{line_number}: invalid JSON: {error}") from error
        if not isinstance(event, dict):
            raise ContractError(f"events.ndjson:{line_number}: event must be an object")
        if event.get("schema_version") != SCHEMA_VERSION or event.get("event") not in EVENTS:
            raise ContractError(f"events.ndjson:{line_number}: invalid event contract")
        if not isinstance(event.get("details"), dict):
            raise ContractError(f"events.ndjson:{line_number}: details must be an object")
        events.append(event)
    return events


def command_init(args: argparse.Namespace) -> None:
    manifest_path = args.manifest.resolve()
    manifest = load_json(manifest_path)
    validate_manifest(manifest, manifest_path.parent)
    run_dir = args.run_dir.resolve()
    if run_dir.exists():
        raise ContractError(f"run directory already exists: {run_dir}")
    run_dir.mkdir(parents=True)
    shutil.copy2(manifest_path, run_dir / "manifest.json")
    for agent in manifest["agents"]:
        prompt = PurePosixPath(agent["prompt_file"])
        destination = run_dir / prompt
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(manifest_path.parent / prompt, destination)
    (run_dir / "events.ndjson").touch()
    append_event(run_dir, "planned", None, {"agent_count": len(manifest["agents"])})
    print(f"initialized run ledger: {run_dir}")


def command_approve(args: argparse.Namespace) -> None:
    run_dir = args.run_dir.resolve()
    path = run_dir / "manifest.json"
    manifest = load_json(path)
    validate_manifest(manifest, run_dir)
    if manifest["approval"]["status"] != "pending":
        raise ContractError("run is already approved")
    manifest["approval"] = {
        "required": True,
        "status": "approved",
        "approved_by": args.approved_by,
        "approved_at": utc_now(),
    }
    write_json(path, manifest)
    append_event(run_dir, "approved", None, {"approved_by": args.approved_by})
    print(f"approved run ledger: {run_dir}")


def command_event(args: argparse.Namespace) -> None:
    details = json.loads(args.details)
    if not isinstance(details, dict):
        raise ContractError("event details must be a JSON object")
    append_event(args.run_dir.resolve(), args.event, args.task_name, details)
    print(f"recorded {args.event} event")


def command_validate(args: argparse.Namespace) -> None:
    if args.manifest:
        manifest_path = args.manifest.resolve()
        validate_manifest(load_json(manifest_path), manifest_path.parent)
        print(f"valid manifest: {manifest_path}")
        return

    run_dir = args.run_dir.resolve()
    manifest = load_json(run_dir / "manifest.json")
    validate_manifest(manifest, run_dir)
    terminal: set[str] = set()
    integrated: set[str] = set()
    for event in read_events(run_dir / "events.ndjson"):
        if event["event"] in TERMINAL_EVENTS and event.get("task_name"):
            terminal.add(event["task_name"])
        if event["event"] == "integrated" and event.get("task_name"):
            integrated.add(event["task_name"])
    if args.require_complete:
        planned = {agent["task_name"] for agent in manifest["agents"]}
        missing = sorted(planned - terminal)
        if missing:
            raise ContractError(f"agents without terminal disposition: {', '.join(missing)}")
        missing_integration = sorted(planned - integrated)
        if missing_integration:
            raise ContractError(
                "agents without integration disposition: " + ", ".join(missing_integration)
            )
    print(f"valid run ledger: {run_dir}")


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init", help="create a ledger from a manifest and prompt files")
    init.add_argument("--manifest", type=Path, required=True)
    init.add_argument("--run-dir", type=Path, required=True)
    init.set_defaults(handler=command_init)

    approve = commands.add_parser("approve", help="record explicit approval")
    approve.add_argument("--run-dir", type=Path, required=True)
    approve.add_argument("--approved-by", required=True)
    approve.set_defaults(handler=command_approve)

    event = commands.add_parser("event", help="append a sanitized lifecycle event")
    event.add_argument("--run-dir", type=Path, required=True)
    event.add_argument("--event", choices=sorted(EVENTS), required=True)
    event.add_argument("--task-name")
    event.add_argument("--details", default="{}", help="JSON object with sanitized event details")
    event.set_defaults(handler=command_event)

    validate = commands.add_parser("validate", help="validate a manifest or initialized ledger")
    source = validate.add_mutually_exclusive_group(required=True)
    source.add_argument("--manifest", type=Path)
    source.add_argument("--run-dir", type=Path)
    validate.add_argument("--require-complete", action="store_true")
    validate.set_defaults(handler=command_validate)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        args.handler(args)
    except (ContractError, json.JSONDecodeError) as error:
        print(f"orchestration ledger error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

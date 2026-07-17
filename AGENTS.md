# Agent Guidance

## Repository purpose

This repository defines a reusable SDLC knowledge and workflow layer for
software-engineering agents. It contains lifecycle guidance in `docs/` and
executable workflows in `.agents/skills/`.

## Start here

Before changing this repository or applying its SDLC model:

1. Read [`docs/reference-lifecycle.md`](docs/reference-lifecycle.md) for the
   lifecycle model and terminology.
2. Read the applicable document under [`docs/stages/`](docs/stages/) for its
   standards basis, required evidence, and decision criteria.
3. Read [`docs/process.md`](docs/process.md) to select the applicable workflow,
   skill, and required evidence.
4. Invoke every skill whose description matches the task. If several skills
   apply, use them in lifecycle order while avoiding duplicate work.

## Working rules

- Use `uv` for all Python execution and dependency resolution. Do not invoke
  system Python directly.
- Keep normative lifecycle guidance in `docs/`; do not duplicate it in skills.
- Keep each skill focused on one repeatable workflow.
- Store repository-scoped skills under `.agents/skills/<skill-name>/SKILL.md`.
- Use relative Markdown links and keep cross-references valid.
- Treat security, risk, quality, traceability, and documentation as
  cross-cutting concerns rather than final gates.
- Require evidence for completion. A claim that work "looks correct" is not
  evidence.
- Preserve source attribution and license notices when importing material.
- Do not claim ISO conformity from alignment with this repository alone.
- Before every commit, pull request, or other publication, scan the complete
  repository for absolute local filesystem paths, PII, credentials, and secret
  material. Publication safety is a blocking validation, not an advisory review.

## Definition of done

A repository change is complete when:

- affected documentation and cross-links are updated;
- applicable skill instructions remain internally consistent;
- new or changed skills have valid `name` and `description` frontmatter;
- referenced files and commands exist;
- relevant validation has been run and its result is reported;
- known gaps, exceptions, and unverified assumptions are explicit.

## Validation

For every change, run:

```sh
uv run python scripts/validate_docs.py
uv run python scripts/validate_publication.py
git diff --check
```

The documentation validator checks tracked and untracked Markdown. `git diff
--check` remains required for patch-level whitespace validation but does not
inspect untracked files by itself. The publication validator scans tracked and
untracked repository content while excluding Git metadata, virtual environments,
Python caches, and known binary formats. Resolve every finding before commit,
pull request creation, push intended for publication, release, or artifact upload.
Do not add a suppression for real credentials or personal data.

For skill changes, additionally validate every changed skill with the available
Agent Skills validator. If no validator is available, verify frontmatter,
folder naming, and all local links manually.

The current repository skills can be validated with:

```sh
for skill in .agents/skills/*; do
  test ! -f "$skill/SKILL.md" || \
    uv run --with pyyaml python \
      "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" \
      "$skill"
done
```

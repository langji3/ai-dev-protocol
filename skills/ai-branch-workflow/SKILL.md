---
name: ai-branch-workflow
description: Manage AI Dev Protocol branch checks and AI branch naming. Use before creating, validating, switching to, or committing on an AI development branch, especially when branch source, developer identity, or ai/{yyyyMMdd}-{developer}-{short-desc} naming matters.
---

# AI Branch Workflow

Use this skill before creating or validating an AI branch.

## Rules

- AI branches should be created from the developer's personal branch.
- Do not start implementation directly from `main`, `master`, `develop`, or shared integration branches unless the user explicitly confirms that this is the team workflow.
- AI branch names must follow:

```text
ai/{yyyyMMdd}-{developer}-{short-desc}
```

Example:

```text
ai/20260626-zhangsan-order-status-filter
```

## Process

1. Check the current branch.
2. Decide whether the current branch is a developer personal branch.
3. If the branch is not a personal branch, ask for confirmation or ask the user to switch.
4. Create or suggest an `ai/...` branch from the personal branch.

## Missing Information

If the developer name or personal branch convention is unknown, ask the user. Do not invent the developer identifier.

## Exceptions

Branch creation can be skipped when:

- The task is read-only.
- The current directory is not a Git repository.
- The user explicitly asks not to create a branch.
- The environment lacks permission to run Git operations.

Mention the exception in the final handoff.


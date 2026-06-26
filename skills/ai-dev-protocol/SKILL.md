---
name: ai-dev-protocol
description: Route AI-assisted development work through the AI Dev Protocol workflow skills. Use when a team development task may require requirement clarification, AI branch workflow, Chinese requirement specs, implementation scope control, Chinese commits, verified handoff, or Apifox API sync summaries.
---

# AI Dev Protocol

AI Dev Protocol 是团队 AI 辅助开发流程规约的总入口 skill。它不承载全部细则，而是按当前阶段路由到对应 workflow skill。

如果以 Codex plugin 形式安装，技能可能显示为 `ai-dev-protocol:<skill-name>`；下方名称指对应的 skill basename。

## Workflow Routing

Use the phase skill that matches the current work:

- `ai-requirement-intake`: clarify the requirement, enforce one requirement per AI branch, and decide whether the task is ready for a spec.
- `ai-branch-workflow`: check the source branch and create or validate `ai/{yyyyMMdd}-{developer}-{short-desc}`.
- `ai-spec-writing`: write the Chinese requirement spec and wait for user confirmation before implementation.
- `ai-implementation-scope`: keep code edits inside the confirmed requirement and prevent unrelated refactors, formatting, dependency changes, or workflow artifacts.
- `ai-commit-rules`: prepare Chinese `feat:` / `fix:` commit messages for `ai/...` branches.
- `ai-handoff`: produce the final delivery summary with verification results, risks, and follow-up notes.
- `ai-apifox-sync`: produce the Apifox sync summary whenever API behavior or contracts changed.

## Hard Gates

Do not start implementation until all applicable gates are satisfied:

1. Requirement scope is clear and maps to one independent requirement.
2. Branch source is known or explicitly deferred by the user.
3. The current branch situation is known, and the AI branch is expected to be created from the developer's personal branch.
4. The Chinese requirement spec is written and confirmed.
5. Planned edits are limited to the current requirement.
6. Verification expectations are stated before delivery.

If any gate is not satisfied, use the matching phase skill before proceeding.

## Standard Flow

1. Use `ai-requirement-intake` when the task enters.
2. Use `ai-branch-workflow` before creating or validating an AI branch.
3. Use `ai-spec-writing` before implementation.
4. Use `ai-implementation-scope` during code changes.
5. Use project-appropriate verification before delivery.
6. Use `ai-commit-rules` before commits on `ai/...` branches.
7. Use `ai-handoff` for final delivery.
8. Use `ai-apifox-sync` in addition to handoff if API behavior or contracts changed.

## Checklist

Before implementation:

- [ ] Requirement is one independent requirement.
- [ ] Scope, non-goals, and affected areas are clear.
- [ ] Branch source and AI branch naming are checked or explicitly deferred by the user.
- [ ] Chinese spec is written and confirmed.

During implementation:

- [ ] Edits stay inside the approved requirement.
- [ ] No unrelated refactor, formatting sweep, dependency upgrade, or generated workflow artifact is included.
- [ ] Any discovered out-of-scope issue is reported instead of silently fixed.

Before final delivery:

- [ ] Verification commands or manual checks are run, or blockers are explained.
- [ ] Delivery includes change summary, verification result, risk notes, and follow-up suggestions when relevant.
- [ ] API changes include Apifox sync summary.
- [ ] Commit messages on `ai/...` branches follow the Chinese `feat:` / `fix:` rule.

---
name: ai-dev-protocol
description: Route AI-assisted development tasks through AI Dev Protocol. Use for coding tasks that need requirement clarification, branch-mode selection, Chinese specs, scoped implementation, commits, merge-back, verified handoff, or Apifox API sync summaries.
---

# AI Dev Protocol

Entry skill. Use it to pick the next phase skill; keep detailed rules in phase skills.

## Flow

1. `ai-requirement-intake`: clarify one independent requirement.
2. `ai-branch-workflow`: detect branch mode.
3. `ai-spec-writing`: write and confirm Chinese spec.
4. `ai-implementation-scope`: implement within confirmed scope.
5. `ai-commit-rules`: prepare/review Chinese `feat:` / `fix:` commits.
6. `ai-merge-back`: personal branch mode only, squash merge `ai/...` back.
7. `ai-handoff`: final delivery.
8. `ai-apifox-sync`: API changes only.

## Conversation Entry

Treat natural design discussion as the start of the workflow when it is likely to become code work.
Examples include "design this module", "our current idea is", "next step", "start implementation", or "build it this way".

Do not treat requirement clarification, branch confirmation, or AI branch creation as permission to implement.
After those steps, continue to the next gate in the flow.

## Branch Modes

- Requirement branch: work directly on current branch; skip `ai/...` and merge-back.
- Personal branch: create `ai/{yyyyMMdd}-{developer}-{short-desc}`, commit a requirement spec under `docs/specs/`, create an ignored local plan, implement, verify, and squash merge back.
- Existing `ai/...`: continue work; identify source developer branch.
- Trunk/environment branch: stop unless user confirms exception.
- Ambiguous branch: ask before editing.

## Gates

Before implementation:

- One requirement only.
- Scope, non-goals, affected areas, and verification are clear.
- Branch mode is known.
- Chinese spec is confirmed.
- The user has confirmed the Chinese spec in the current workflow after branch mode is known.
- Personal branch mode has a committed `docs/specs/{yyyyMMdd}-{short-desc}.md` requirement spec on the `ai/...` branch.
- Personal branch mode has an ignored local plan, preferably `.ai-dev-protocol/plans/{yyyyMMdd}-{short-desc}-plan.md`; the plan must not be tracked by Git.
- If the user only confirmed "personal branch" or "requirement branch", that confirms branch mode only; next step is `ai-spec-writing`, not implementation.

Before delivery:

- Personal branch mode has spec document path, spec commit status, local plan execution status, implementation commit status, and merge-back status recorded.
- Verification ran, or blocker is stated.
- Implementation plan/goals were tracked, or a reason for a lightweight path is stated.
- Subagent or independent review ran when the task was complex or involved code changes and the environment supported it; otherwise the fallback self-review is stated.
- Commits use Chinese `feat:` / `fix:` when created.
- Personal branch mode has merge-back status.
- Developer takeover is stated.
- API changes include Apifox sync summary.

## Global Rules

- Specs, handoff, Apifox summaries, and AI commit messages use Chinese.
- Code identifiers, API paths, table names, config keys, commands, and file paths stay English.
- No unrelated refactor, formatting sweep, dependency upgrade, tracked plan file, `.superpowers/`, or external workflow artifact unless explicitly requested.
- Implementation may borrow the Superpowers-style working method: split goals, progress step by step, and use independent review. In personal branch mode, create an ignored local plan file for execution; do not create `.superpowers/` files.
- Developer owns final review, self-test, integration testing, PR, merge, and code quality.

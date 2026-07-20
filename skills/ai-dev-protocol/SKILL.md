---
name: ai-dev-protocol
description: Route AI-assisted development tasks through AI Dev Protocol. Use for coding tasks that need requirement clarification, developer-branch workflow selection, Chinese specs, scoped implementation, commits, merge-back, verified handoff, Apifox API sync summaries, or Apifox-ready interface/model catalogs.
---

# AI Dev Protocol

Entry skill. Use it to pick the next phase skill; keep detailed rules in phase skills.

AI Dev Protocol is a lightweight team workflow plugin. It owns requirement clarity, branch gates, specs, scope control, commits, handoff, and API sync. It may borrow useful Superpowers-style working methods, but it must not inherit heavy hidden state, broad agent role systems, or `.superpowers/` artifacts.

## Flow

1. `ai-requirement-intake`: clarify one independent requirement.
2. `ai-branch-workflow`: detect developer branch, existing AI branch, or blocked branch.
3. `ai-spec-writing`: write and confirm Chinese spec.
4. `ai-implementation-scope`: implement within confirmed scope.
5. `ai-commit-rules`: prepare/review Chinese `feat:` / `fix:` commits.
6. `ai-merge-back`: report merge readiness, request explicit developer approval, then squash merge `ai/...` back only after approval.
7. `ai-handoff`: final delivery.
8. `ai-apifox-sync`: API changes, Apifox sync summaries, and Apifox-ready interface/model catalogs.

## Product Principles

- One obvious entry: users normally trigger only `ai-dev-protocol`.
- Keep phase skills small; do not turn the plugin into a large general-purpose agent framework.
- Make gates visible: branch source, spec confirmation, implementation start, commit, merge-back, and handoff.
- Recover from current state by inspecting branch, Git status, existing spec, local plan, and commits.
- Keep temporary AI execution state out of business commits.
- Prioritize developer takeover over automation.

## Conversation Entry

Treat natural design discussion as the start of the workflow when it is likely to become code work.
Examples include "design this module", "our current idea is", "next step", "start implementation", or "build it this way".

Do not treat requirement clarification, branch confirmation, or AI branch creation as permission to implement.
After those steps, continue to the next gate in the flow.

## Branch Workflow

- Developer branch: create `ai/{yyyyMMdd}-{developer}-{short-desc}`, commit a requirement spec under `docs/specs/`, create the corresponding ignored local plan under `docs/plans/`, implement, verify, report readiness, and wait for explicit merge-back approval.
- Existing `ai/...`: continue work; identify source developer branch.
- Trunk/environment branch: stop unless the user explicitly says this branch is their developer aggregation branch.
- Ambiguous branch: ask before editing.

## Gates

Before implementation:

- One requirement only.
- Scope, non-goals, affected areas, and verification are clear.
- Developer branch or existing AI branch is known.
- Chinese spec is confirmed.
- The user has confirmed the Chinese spec in the current workflow after branch mode is known.
- The AI branch has a committed `docs/specs/{yyyyMMdd}-{short-desc}.md` requirement spec.
- The AI branch has an ignored local plan at `docs/plans/{yyyyMMdd}-{short-desc}-plan.md`, using the corresponding spec basename; the plan must not be tracked by Git.
- If the user only confirmed the developer branch, that confirms branch source only; next step is `ai-spec-writing`, not implementation.

Before delivery:

- Spec document path, spec commit status, local plan execution status, implementation commit status, and merge-back status are recorded.
- Verification ran, or blocker is stated.
- Implementation plan/goals were tracked, or a reason for a lightweight path is stated.
- Subagent or independent review ran when the task was complex or involved code changes and the environment supported it; otherwise the fallback self-review is stated.
- Commits use Chinese `feat:` / `fix:` when created.
- Merge-back status is recorded.
- Developer takeover is stated.
- API changes include Apifox sync summary, and Apifox-ready catalogs when requested.

Before merge-back:

- Report the completed implementation, verification, risks, AI branch, target developer branch, and proposed squash commit message.
- Ask the developer whether this specific AI branch may be merged back.
- Treat this as a new authorization gate. Spec confirmation and implementation approval do not carry forward to merge-back.
- Without an explicit affirmative answer, remain on the AI branch and leave the developer branch untouched.

## Recovery Mode

Do not assume the workflow starts from zero. Before deciding the next phase, infer current state:

- Current branch: developer branch, `ai/...`, trunk/environment branch, or ambiguous branch.
- Git status: clean, unstaged work, staged work, committed implementation, or local branch ahead.
- Spec status: missing, present but unconfirmed, confirmed, or stale.
- Local plan status: missing, present and ignored under `docs/plans/`, or incorrectly tracked / misplaced.
- API sync status: no API change, summary needed, Apifox entry catalog requested, or Apifox-ready list completed.

## Global Rules

- Specs, handoff, Apifox summaries, and AI commit messages use Chinese.
- Code identifiers, API paths, table names, config keys, commands, and file paths stay English.
- No unrelated refactor, formatting sweep, dependency upgrade, tracked plan file, `.superpowers/`, or external workflow artifact unless explicitly requested.
- Implementation may borrow selected Superpowers-style methods: context hygiene, goal decomposition, step-by-step progress, scope guard, and independent review. Create an ignored local plan file for execution; do not create `.superpowers/` files or hidden workflow artifacts.
- Never merge, squash merge, cherry-pick, or commit implementation onto the developer branch without explicit developer approval for that specific merge-back.
- Developer owns final review, self-test, integration testing, PR, merge, and code quality.

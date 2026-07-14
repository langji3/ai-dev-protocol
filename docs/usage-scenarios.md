# AI Dev Protocol Usage Scenarios

This document shows how AI Dev Protocol should behave in real team work. Users normally only need to invoke the main entry skill: `ai-dev-protocol`.

## 1. Start A New Requirement

User says:

```text
按 AI Dev Protocol 做一个订单状态筛选需求。
```

Expected behavior:

- Clarify one independent requirement.
- Confirm the developer branch or identify that the current branch can be used as the developer aggregation branch.
- Create or suggest an `ai/{yyyyMMdd}-{developer}-{short-desc}` branch.
- Write a Chinese spec under `docs/specs/`.
- Commit the spec before implementation.
- Wait for user confirmation of the spec.
- Create an ignored local plan under `docs/plans/{yyyyMMdd}-{short-desc}-plan.md`, using the corresponding spec basename.
- Implement within the confirmed scope.
- Verify, review, commit, and prepare merge-back.

## 2. Continue An Existing AI Branch

User says:

```text
继续这个 AI 分支，把剩下的需求做完。
```

Expected behavior:

- Detect the current `ai/...` branch.
- Identify or ask for the source developer branch if it is not clear.
- Read the existing spec and confirm it still matches the requested work.
- Check whether the corresponding local plan exists under `docs/plans/` and whether it is untracked.
- Inspect Git status to distinguish implemented, staged, committed, and pending work.
- Continue from the current stage instead of restarting the workflow.

## 3. Small Bug Fix

User says:

```text
修一下用户列表的空指针问题。
```

Expected behavior:

- Keep the requirement narrow.
- Ask for missing reproduction or expected behavior only when needed.
- Keep the branch and spec gates. If a team wants an emergency path, it should define that policy outside this plugin instead of treating small fixes as an implicit bypass.
- Use a lightweight plan for tiny changes.
- Avoid formatting sweeps, unrelated refactors, dependency upgrades, or adjacent cleanup.
- Commit with a Chinese `fix:` message when asked to commit.

## 4. API Change With Apifox Sync

User says:

```text
给公告模块增加批量已读接口。
```

Expected behavior:

- Treat the endpoint as an API contract change.
- Include request, response, permission, error cases, compatibility, and verification in the spec.
- In final delivery, include Apifox sync summary.
- Ask whether the user needs an Apifox-ready "接口清单 + 数据模型".
- If requested, generate the complete Apifox-ready artifact using `ai-apifox-sync`.

## 5. Design Discussion Only

User says:

```text
我想讨论一下公告模块怎么设计，先不要写代码。
```

Expected behavior:

- Stay in discussion mode.
- Help clarify goals, scope, risks, data model, API surface, and alternatives.
- Do not create branches, specs, plans, or code unless the user asks to enter implementation workflow.
- If the discussion begins to turn into implementation, summarize the requirement and ask whether to start AI Dev Protocol.

## 6. Scope Expansion During Implementation

User says:

```text
顺便把列表页也重构一下。
```

Expected behavior:

- Identify that this expands the confirmed scope.
- Explain whether it should be a separate requirement.
- Continue only after the user explicitly confirms the scope change.
- Record the scope change in the local plan and final handoff.

## 7. Already Implemented, Need Handoff

User says:

```text
你交付一下这次改动。
```

Expected behavior:

- Inspect Git status and recent commits.
- Summarize changed files and confirmed scope.
- Report spec path, local plan state, implementation commit state, verification, review, risks, and merge-back status.
- State that the developer owns final review, self-test, integration testing, PR, merge, and follow-up.
- Include Apifox sync summary when API behavior changed.

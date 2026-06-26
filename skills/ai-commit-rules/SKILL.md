---
name: ai-commit-rules
description: Apply AI Dev Protocol commit rules. Use before preparing or reviewing commits on ai/... branches to ensure Chinese commit messages, correct feat:/fix: prefixes, and no unrelated changes.
---

# AI Commit Rules

Use this skill before committing or reviewing commits on an `ai/...` branch.

## Message Format

Commit messages must be Chinese and use one of:

- `feat:` for requirements, features, or new capabilities.
- `fix:` for modifications, bug fixes, or behavior corrections.

Examples:

```text
feat: 增加订单状态筛选
fix: 修复订单状态筛选参数缺失
```

## Pre-Commit Checklist

- Current branch is `ai/...`, or the exception is explicit.
- Changes belong only to the current requirement.
- No unrelated refactor, formatting sweep, dependency change, or workflow artifact is included.
- Verification has run, or the reason it cannot run is recorded.
- Commit message is Chinese and uses the correct prefix.


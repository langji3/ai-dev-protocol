# AI Dev Protocol

本项目使用 AI Dev Protocol 作为 AI 辅助开发流程规约。

分支模式自动判断：AI 在实现前先查看当前分支命名风格。

- 需求分支模式：如果当前分支已经是明确需求分支，例如 `feature/...`、`fix/...`、`hotfix/...`、`task/...` 或 ticket 命名分支，AI 直接在当前分支工作，并跳过 merge-back。
- 个人分支模式：如果当前分支是开发者个人分支，例如 `developer/<name>`、`dev/<name>`、`<name>/dev`，每个明确需求从该分支创建一个 `ai/...` 分支；AI 先提交 `docs/specs/*.md`，再创建未追踪的本地 plan，完成实现和验证后 squash merge 回开发者个人分支。
- 分支含义不明确时，AI 必须先询问当前分支是个人分支还是需求分支。

AI 不应直接在 `main`、`master`、`dev`、`develop`、`site`、`staging`、`test`、`prod`、`production` 等主干或环境分支上实现，除非用户明确确认这是团队规则。

当任务涉及需求实现、代码修改、bug fix、提交或交付时，Codex 必须使用 AI Dev Protocol workflow skills：

- `ai-dev-protocol`：总入口和流程路由。
- `ai-requirement-intake`：需求澄清、一需求一工作单元。
- `ai-branch-workflow`：根据当前分支命名风格选择需求分支模式、个人分支模式或停止在主干/环境分支。
- `ai-spec-writing`：中文 spec 和实现前确认；个人分支模式下 spec 写入并提交到 `docs/specs/*.md`。
- `ai-implementation-scope`：范围控制、本地临时 plan、plan/goals 拆分、subagent / 独立审查，禁止无关改动。
- `ai-commit-rules`：中文 `feat:` / `fix:` commit。
- `ai-merge-back`：个人分支模式下 squash merge 回开发者个人分支。
- `ai-handoff`：最终交付、spec 文档路径、spec 提交状态、本地 plan Git 状态、实现提交状态、实现范围记录、范围变化说明、plan/goals 完成情况、subagent / 独立审查情况、验证说明和开发者接管说明。
- `ai-apifox-sync`：API 变更后的 Apifox sync summary。

如果这些 skills 由 Codex plugin 加载，名称可能显示为 `ai-dev-protocol:<skill-name>`。

自然语言的模块设计讨论如果可能进入代码实现，也必须从 `ai-requirement-intake` 开始。用户确认“个人分支”或“需求分支”只表示分支模式已确认，不表示允许实现；下一步必须进入 `ai-spec-writing`。个人分支模式下先提交 `docs/specs/*.md`，等待中文 spec 确认后，再创建未追踪的本地 plan，之后才能改实现文件。

进入实现后，Codex 应按本地 plan 拆分 plan/goals 并持续更新状态；极小改动可使用轻量 plan。复杂任务或代码变更优先使用 subagent / 多 AI 做独立审查。若当前环境不支持 subagent，交付时说明原因并记录替代自检。可以借鉴 Superpowers 式逐 goal 推进的方法，但不得提交被 Git 追踪的 plan 文件或创建 `.superpowers/` 产物，除非用户明确要求。

完整规则以 `skills/` 下各 `SKILL.md` 为准。

# AI Dev Protocol

本项目使用 AI Dev Protocol 作为 AI 辅助开发流程规约。

当任务涉及需求实现、代码修改、bug fix、提交或交付时，Codex 必须使用 AI Dev Protocol workflow skills：

- `ai-dev-protocol`：总入口和流程路由。
- `ai-requirement-intake`：需求澄清、一需求一分支。
- `ai-branch-workflow`：个人分支检查、`ai/...` 分支命名。
- `ai-spec-writing`：中文 spec 和实现前确认。
- `ai-implementation-scope`：范围控制，禁止无关改动。
- `ai-commit-rules`：中文 `feat:` / `fix:` commit。
- `ai-handoff`：最终交付和验证说明。
- `ai-apifox-sync`：API 变更后的 Apifox sync summary。

如果这些 skills 由 Codex plugin 加载，名称可能显示为 `ai-dev-protocol:<skill-name>`。

完整规则以 `skills/` 下各 `SKILL.md` 为准。


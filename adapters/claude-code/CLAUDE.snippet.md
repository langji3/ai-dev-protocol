# AI Dev Protocol

本项目使用 AI Dev Protocol 作为 AI 辅助开发流程规约。

当任务涉及需求实现、代码修改、bug fix、提交或交付时，Claude Code 必须遵守本协议的阶段化 workflow：

- 需求进入：先澄清需求，确保一个 AI 分支只处理一个明确 requirement。
- 分支检查：AI 分支必须从开发者个人分支创建，命名为 `ai/{yyyyMMdd}-{developer}-{short-desc}`。
- Spec：实现前必须写中文 spec，并等待用户确认。
- 实现：只修改当前需求相关内容，不混入无关重构、格式化、依赖升级或 workflow 产物。
- 提交：`ai/...` 分支 commit message 使用中文，需求用 `feat:`，修改用 `fix:`。
- 交付：最终交付包含验证结果；API 变更包含 Apifox sync summary。

代码标识符、API 路径、表名、配置键保持英文。

完整规则以本仓库 `skills/` 下各 `SKILL.md` 为准。


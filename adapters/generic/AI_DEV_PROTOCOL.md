# AI Dev Protocol

AI Dev Protocol is a team workflow protocol for AI-assisted software development.

AI Dev Protocol 是一套面向团队的 AI 辅助开发流程规约，用于统一 AI 编程工具在需求、分支、规格、实现、提交和交付环节中的行为。

## 使用场景

当 AI 工具处理以下任务时，应遵守本协议：

- 需求实现
- 代码修改
- bug fix
- 实现计划
- commit 准备
- 最终交付

普通问答、代码解释、只读分析不需要强制执行完整流程。

## 阶段化 Workflow

Codex 中本协议拆分为多个 skills：

- `ai-dev-protocol`：总入口和路由。
- `ai-requirement-intake`：需求澄清、一需求一分支。
- `ai-branch-workflow`：个人分支检查、`ai/...` 分支命名。
- `ai-spec-writing`：中文 spec 和实现前确认。
- `ai-implementation-scope`：范围控制，禁止无关改动。
- `ai-commit-rules`：中文 `feat:` / `fix:` commit。
- `ai-handoff`：最终交付和验证说明。
- `ai-apifox-sync`：API 变更后的 Apifox sync summary。

其他 AI 工具可以按同样阶段执行。

## 核心规则

1. 一个 AI 分支只处理一个明确需求。
2. AI 在动手前必须先确认需求范围。
3. AI 分支必须从开发者个人分支创建。
4. AI 分支命名遵循 `ai/{yyyyMMdd}-{developer}-{short-desc}`。
5. spec 使用中文，代码标识符、API 路径、表名、配置键保持英文。
6. `ai/...` 分支 commit message 使用中文，需求用 `feat:`，修改用 `fix:`。
7. 不混入无关重构、格式化、依赖变更。
8. 不提交单独 plan 文件或 `.superpowers/` 工作流产物，除非明确要求。
9. 最终交付必须包含测试/验证说明。
10. 如有 API 变更，最终交付必须包含 Apifox sync summary。

## 标准流程

1. 需求进入：判断需求是否清楚，是否是一个独立 requirement。若范围不清，必须先提问。
2. 分支检查：检查当前是否在开发者个人分支，并建议从个人分支创建 `ai/...` 分支。
3. 规格说明：先写中文 spec，明确目标、范围、非目标、影响文件、验证方式。
4. 实现前确认：用户确认 spec 后，才进入实现或修改阶段。
5. 范围控制：只改与当前需求相关的内容，不做无关重构、格式化、依赖升级。
6. 验证：根据项目情况运行测试、构建、静态检查，不能运行时要说明原因。
7. 提交规则：若在 `ai/...` 分支提交，commit message 使用中文，并按 `feat:` / `fix:` 分类。
8. 最终交付：输出变更摘要、验证结果、风险说明、后续建议。若有 API 变更，附 Apifox sync summary。

## 权威规则

如果该通用文档与仓库中的 skill 规则不一致，以 `skills/` 下各 `SKILL.md` 为准。


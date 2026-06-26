# AI Dev Protocol

AI Dev Protocol is a team workflow protocol for AI-assisted software development.

AI Dev Protocol 是一套面向团队的 AI 辅助开发流程规约，用于统一 AI 编程工具在需求、分支、规格、实现、提交和交付环节中的行为。

## 项目定位

`ai-dev-protocol` 是一个可独立维护、可通过 GitHub 拉取、可被多个 AI 编程工具复用的 workflow skills/plugin 仓库。它不是单个项目里的提示词，也不是普通规范文档。

本仓库采用类似 Superpowers 的组织方式：

- `.codex-plugin/plugin.json` 声明 Codex plugin。
- `skills/` 下每个子目录都是一个独立 skill。
- `ai-dev-protocol` 是总入口和路由 skill。
- 其他 `ai-*` skills 分别负责需求、分支、spec、范围控制、提交、交付和 Apifox 同步。

## Codex 安装后的 Skills

Codex 以 plugin 形式安装后，会从 `skills/` 加载多个 workflow skills：

```text
ai-dev-protocol
ai-requirement-intake
ai-branch-workflow
ai-spec-writing
ai-implementation-scope
ai-commit-rules
ai-handoff
ai-apifox-sync
```

在 Codex plugin 环境中，它们可能显示为带插件前缀的名称，例如 `ai-dev-protocol:ai-spec-writing`。

## 核心目标

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

## 目录结构

```text
ai-dev-protocol/
  README.md
  CHANGELOG.md
  docs/
    iteration-guide.md
  .codex-plugin/
    plugin.json

  skills/
    ai-dev-protocol/
      SKILL.md
    ai-requirement-intake/
      SKILL.md
    ai-branch-workflow/
      SKILL.md
    ai-spec-writing/
      SKILL.md
      templates/
        requirement-spec.md
    ai-implementation-scope/
      SKILL.md
    ai-commit-rules/
      SKILL.md
    ai-handoff/
      SKILL.md
      templates/
        handoff-summary.md
    ai-apifox-sync/
      SKILL.md
      templates/
        apifox-sync-summary.md

  adapters/
    codex/
      AGENTS.snippet.md
      install.md
    claude-code/
      CLAUDE.snippet.md
      install.md
    cursor/
      ai-dev-protocol.mdc
      install.md
    generic/
      AI_DEV_PROTOCOL.md
```

## Workflow Routing

1. 需求进入：使用 `ai-requirement-intake` 判断需求是否清楚，是否是一个独立 requirement。若范围不清，必须先提问。
2. 分支检查：使用 `ai-branch-workflow` 检查当前是否在开发者个人分支，并建议从个人分支创建 `ai/...` 分支。
3. 规格说明：使用 `ai-spec-writing` 写中文 spec，明确目标、范围、非目标、影响文件、验证方式。
4. 实现前确认：用户确认 spec 后，AI 才进入实现或修改阶段。
5. 范围控制：使用 `ai-implementation-scope` 控制改动范围，不做无关重构、格式化、依赖升级。
6. 验证：根据项目情况运行测试、构建、静态检查，不能运行时要说明原因。
7. 提交规则：使用 `ai-commit-rules` 检查 `ai/...` 分支中文 commit message，并按 `feat:` / `fix:` 分类。
8. 最终交付：使用 `ai-handoff` 输出变更摘要、验证结果、风险说明、后续建议。
9. API 变更：使用 `ai-apifox-sync` 输出 Apifox sync summary。

## 安装方式

### Codex Plugin

本仓库已经包含 `.codex-plugin/plugin.json`，可以作为 Codex plugin 分发。团队可通过个人或团队 marketplace、本地 plugin 目录、或 Codex 支持的 plugin 安装流程接入。

Codex 读取 plugin 后，会加载 `plugin.json` 中声明的：

```json
{
  "skills": "./skills/"
}
```

因此安装的是一个 plugin，但可用的是多个 workflow skills。

详细说明见 `adapters/codex/install.md`。

### Codex Skills 直装

如果暂时不使用 plugin，也可以把 `skills/` 下的每个 skill 子目录分别安装到 `~/.codex/skills/`。这种方式同样会得到多个 skills，但没有 plugin 卡片和 marketplace 分发能力。

### Claude Code

将 `adapters/claude-code/CLAUDE.snippet.md` 合并到目标项目的 `CLAUDE.md`。

### Cursor

复制 `adapters/cursor/ai-dev-protocol.mdc` 到目标项目的 `.cursor/rules/`。

### 通用 AI 工具

引用 `adapters/generic/AI_DEV_PROTOCOL.md`，并要求 AI 在代码修改、需求实现、修复、提交和交付场景遵守协议。

## 阶段计划

### 第一阶段：最小可用版本

完成 Codex plugin manifest、多阶段 workflow skills、模板和 Codex/Claude Code/Cursor 适配文件。

### 第二阶段：真实项目试点

选择 1-2 个需求，用 Codex 或 Claude Code 跑完整流程，记录 AI 是否能稳定遵守规则。

### 第三阶段：规则收敛

根据试点结果优化触发条件、检查清单、模板措辞和交付格式。

### 第四阶段：团队推广

把仓库接入团队项目，形成复制/安装说明，约定版本更新方式，并视需要接入团队 plugin marketplace。

## 可持续迭代

- 使用 `CHANGELOG.md` 记录版本变化。
- 使用 `docs/iteration-guide.md` 约定反馈收集、版本号、发布检查和新增 skill 判断标准。
- 每次真实项目试点后，优先修改最小相关 skill，避免把规则堆回总入口。
- 当新增独立阶段时再创建新 skill；阶段内规则变化优先更新已有 skill。

## 验收标准

1. 团队成员可以通过 GitHub 拉取并使用 `ai-dev-protocol`。
2. Codex 能以 plugin 方式读取多个 workflow skills。
3. Claude Code 和 Cursor 能通过适配文件读取核心规则。
4. AI 能稳定做到一需求一分支、一 spec 一范围。
5. 最终交付包含验证结果，API 变更包含 Apifox sync summary。
6. 规则可在多个项目复用，不依赖单个业务仓库。

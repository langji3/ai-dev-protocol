# Codex 安装说明

## 推荐方式：作为 Plugin 安装

本仓库包含 Codex plugin manifest：

```text
.codex-plugin/plugin.json
```

manifest 中声明：

```json
{
  "skills": "./skills/"
}
```

因此 Codex 安装的是 `ai-dev-protocol` 这个 plugin，加载的是 `skills/` 下的多个 workflow skills。

安装后应能看到或触发：

```text
ai-dev-protocol
ai-requirement-intake
ai-branch-workflow
ai-spec-writing
ai-implementation-scope
ai-commit-rules
ai-merge-back
ai-handoff
ai-apifox-sync
```

在 plugin 命名空间下，它们可能显示为 `ai-dev-protocol:<skill-name>`。

## Marketplace 安装方式

如果团队已经发布了 marketplace 仓库，例如：

```text
https://github.com/langji3/ai-dev-protocol-marketplace
```

在 Codex App 中：

1. 打开插件页面。
2. 点击“添加插件市场”。
3. 输入或选择 marketplace 仓库。
4. 在该市场中安装 `AI Dev Protocol`。
5. 重启 Codex 或新开 thread 验证。

维护者可以从当前插件仓库生成 marketplace 仓库内容：

```powershell
.\scripts\build-marketplace.ps1
```

生成结果位于：

```text
dist/ai-dev-protocol-marketplace
```

## 团队接入

将 `adapters/codex/AGENTS.snippet.md` 合并到目标项目的 `AGENTS.md`。

如果项目已有 `AGENTS.md`，保留原有项目规则，并追加 AI Dev Protocol 段落。若规则冲突：

- 项目业务、架构、代码风格规则优先。
- 需求澄清、分支模式、spec、范围控制、提交、merge-back 和交付流程遵守 AI Dev Protocol。

## 备用方式：直接安装多个 Skills

如果暂时不使用 Codex plugin，可将 `skills/` 下每个子目录分别复制到 `~/.codex/skills/`。

这种方式也会得到多个 skills，但没有 plugin 卡片、统一插件元数据或 marketplace 分发能力。

## 验证

在目标项目中发起一个代码修改任务，确认 Codex 会：

- 使用 `ai-requirement-intake` 先确认需求范围。
- 使用 `ai-branch-workflow` 判断默认 AI 分支模式或直接需求分支兼容模式。
- 使用 `ai-spec-writing` 写中文 spec。
- 使用 `ai-merge-back` 在默认模式下 squash merge 回开发者个人分支。
- 使用 `ai-handoff` 在交付时包含验证结果、merge-back 状态和开发者接管说明。
- API 变更时使用 `ai-apifox-sync` 输出 Apifox sync summary。

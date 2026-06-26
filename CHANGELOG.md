# Changelog

All notable changes to AI Dev Protocol are documented here.

版本号遵循语义化版本：

- `MAJOR`：破坏性流程调整，例如阶段顺序、skill 命名或安装方式不兼容。
- `MINOR`：新增 workflow skill、模板或重要规则，但保持已有使用方式兼容。
- `PATCH`：文案修正、说明补充、模板微调或维护性更新。

## [0.1.1] - 2026-06-26

### Added

- Added `CHANGELOG.md` to record protocol evolution.
- Added `docs/iteration-guide.md` to define the sustainable iteration workflow for skills, templates, adapters, and plugin metadata.

### Changed

- Bumped plugin version from `0.1.0` to `0.1.1`.

## [0.1.0] - 2026-06-26

### Added

- Added Codex plugin manifest at `.codex-plugin/plugin.json`.
- Added multi-skill workflow structure:
  - `ai-dev-protocol`
  - `ai-requirement-intake`
  - `ai-branch-workflow`
  - `ai-spec-writing`
  - `ai-implementation-scope`
  - `ai-commit-rules`
  - `ai-handoff`
  - `ai-apifox-sync`
- Added requirement spec, handoff summary, and Apifox sync summary templates.
- Added Codex, Claude Code, Cursor, and generic AI tool adapters.


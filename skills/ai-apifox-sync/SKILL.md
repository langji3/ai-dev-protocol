---
name: ai-apifox-sync
description: Create Apifox sync summaries for AI Dev Protocol API changes. Use when a task changes endpoints, request parameters, response schemas, status codes, error codes, authentication, permissions, headers, examples, or observable API behavior.
---

# AI Apifox Sync

Use whenever API behavior or contracts changed.

## Triggers

- Endpoint added, removed, or changed.
- Request path/query/header/cookie/body changed.
- Response body, status code, error code, or error response changed.
- Auth, permission, example, field meaning, compatibility, or observable behavior changed.

## Include

Use `templates/apifox-sync-summary.md` when structure helps.

- 变更类型
- 受影响 API
- Request 变更
- Response 变更
- 错误码或 status code 变更
- 权限或认证变化
- 兼容性说明
- Apifox 中需同步的文档、示例、Mock、测试用例

## Apifox Ready List

When the user asks for an Apifox-ready artifact, or when final delivery should provide a directly transferable API document, use the template to produce a complete "接口清单 + 数据模型" instead of only a short sync summary.

The output should be convenient for an Apifox maintainer to copy into Apifox:

- 公共信息：模块、Base Path、认证方式、返回结构、时间格式、变更类型、兼容性
- 接口清单：接口名称、Method、Path、权限、请求类型、响应模型、变更类型
- 接口详情：说明、权限、Path / Query / Body、请求示例、响应示例、错误场景
- 数据模型：请求模型、响应模型、分页模型、通用响应模型
- 枚举说明：字段、枚举值、含义
- Apifox 同步结论：新增 / 修改 / 删除接口数量，模型、权限、错误码、Mock、测试用例同步项

## No API Change

Use:

```text
Apifox sync summary：无 API 变更，无需同步。
```

# 行为验证

scenarios.json 保留 16 个原始场景，另有 4 个跨对话兼容性场景，共 20 个。评估者只接收 scripts/evaluate.py prompt <id> 输出、当前 Router 路径及必要原始材料，不接收 expect 或已知问题。

评估关注路由和动作/状态，不匹配最终回复措辞。actions 使用诸如 edit-file、write-spec、request-spec-approval、merge、read-apifox、write-apifox 的操作标识；evidence 记录依据的原始状态或实际工具结果。

记录 JSON 顶层字段：
mode（independent-simulation 或 live）、tool、toolVersion、pluginVersion、date、cases。
每例字段：id、route、actions、evidence。人工发现事实或行为错误时加 reviewIssues，计入失败。live 额外提供 artifacts 数组，每项含 path（相对记录文件的真实日志/差异/状态文件）和 sha256（原始字节摘要）；评分器验证文件存在、未越界且摘要相同。

~~~shell
python scripts/evaluate.py list
python scripts/evaluate.py prompt merge_ok
python scripts/evaluate.py score evals/results/<run>.json
~~~

score 检查提交的行为记录；缺少的场景列为 unverified。工具不调用模型、不连接 API。评分器通过或模拟通过不等于真实平台运行通过。

真实回归应在一次性 Git 项目、隔离工具配置中进行，保存操作日志和前后文件/分支状态。Apifox 使用模拟响应，不连接真实项目。每次运行记录工具和插件版本；涉及授权的用例应包含完整前置对话。检查结果文件与原始证据一致后才能作为发布证据。

脚本单元测试只验证评分器会拒绝错误动作/缺失证据；它们不验证模型行为。实际记录放在 results/，区分独立演练与真实运行，敏感内容脱敏。

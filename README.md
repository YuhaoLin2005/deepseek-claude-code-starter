# Claude Code Pro Config

> 把 Claude Code 配置到大神级别——DeepSeek v4 Pro 驱动，7 个 MCP 服务，9 个专业 Agent，6 套代码规则。

## 这是什么？

一套经过实战打磨的 Claude Code 配置方案，面向**用 DeepSeek API 替代 Anthropic API** 的用户。核心思路：用 DeepSeek v4 Pro 的百万上下文 + 极低价格，搭配 Claude Code 的 Agent 体系，实现 10-50 倍成本优势。

## 适用谁？

| 水平 | 能不能用 | 说明 |
|------|---------|------|
| 🟢 新手 | ✅ | 跟着 SETUP.md 一步步来就行，10 分钟搞定 |
| 🔵 进阶 | ✅ | 可按需裁剪，关掉不需要的 MCP/Agent |
| 🟣 大神 | ✅ | 拿去魔改，欢迎 PR 回来 |

## 核心特性

- **模型**：DeepSeek v4 Pro（1M 上下文，思考模式），配置了缓存前缀以最大化缓存命中率
- **MCP 服务**：文件系统、Playwright 浏览器、GitHub API、PostgreSQL、Context7 文档、DuckDuckGo 搜索、Vision 图片分析
- **自定义 Agent**：senior-dev（高级工程师）、code-reviewer、security-reviewer、tdd-guide、architect、planner、build-error-resolver、rust-reviewer、doc-updater
- **代码规则**：代码质量、安全、测试、工作流、性能、模式——6 套专业规则
- **Token 优化**：RTK CLI 代理（60-90% Bash 命令 token 节省）、ECC 插件
- **快捷键**：Ctrl+R 审查 / Ctrl+G 提交 / Ctrl+Shift+P 计划模式 / Ctrl+L 查看日志 / Ctrl+Shift+V 视觉分析

## 快速开始

```bash
# 1. 注册 DeepSeek API（https://platform.deepseek.com）
# 2. 获取 API Key
# 3. 克隆本仓库
git clone https://github.com/YuhaoLin2005/claude-code-pro-config.git
# 4. 复制到 Claude Code 配置目录
cp -r claude-code-pro-config/.claude/* ~/.claude/
cp claude-code-pro-config/templates/mcp.json.example ~/.mcp.json
cp claude-code-pro-config/templates/settings.local.json.example ~/.claude/settings.local.json
# 5. 编辑配置文件，填入你的路径和 Key
# 6. 设置环境变量（见 SETUP.md）
# 7. 重启 Claude Code
```

**详细步骤见 [SETUP.md](SETUP.md)**

## 文件结构

```
~/.claude/
├── CLAUDE.md              # 规则入口（引用 rules/ 下的文件）
├── RTK.md                 # RTK 使用指南
├── settings.json          # 主配置（模型、hooks、插件）
├── settings.local.json    # 本地权限（不提交到 Git）⚠️
├── keybindings.json       # 快捷键
├── ecc_config.json        # ECC 插件策略
├── rules/                 # 6 套代码规范
│   ├── code-quality.md
│   ├── security.md
│   ├── testing.md
│   ├── workflow.md
│   ├── performance.md
│   └── patterns.md
└── agents/                # 9 个专业 Agent
    ├── senior-dev.md
    ├── code-reviewer.md
    ├── security-reviewer.md
    ├── tdd-guide.md
    ├── architect.md
    ├── planner.md
    ├── build-error-resolver.md
    ├── rust-reviewer.md
    └── doc-updater.md
```

## 需要额外安装的

| 工具 | 用途 | 安装 |
|------|------|------|
| DeepSeek API Key | 模型驱动 | [platform.deepseek.com](https://platform.deepseek.com) |
| RTK | Token 优化（可选） | `cargo install rtk` |
| GitHub CLI | GitHub 操作 | `winget install GitHub.cli` |
| uv | mcp-vision 运行 | `pip install uv` 或 [astral.sh](https://astral.sh) |
| PostgreSQL | postgres MCP（可选） | [postgresql.org](https://www.postgresql.org) |
| DashScope API Key | Vision 图片分析（可选） | [dashscope.aliyun.com](https://dashscope.aliyun.com) |

## 常见问题

**Q: 我是 Anthropic API 用户，能直接用吗？**
A: 需要改 `settings.json` 里的 `ANTHROPIC_BASE_URL` 和模型名。搜索 `deepseek` 全部替换为 `claude-sonnet-4-6` 之类的即可。

**Q: 为什么用 DeepSeek 而不是 Claude 原版？**
A: DeepSeek v4 Pro 百万上下文 + ¥1/百万 token vs Claude Sonnet $3/百万 token。10-50 倍成本差距。

**Q: 安全吗？**
A: 本仓库不含任何密钥。所有敏感信息通过环境变量注入（`${VAR}` 语法）。`settings.local.json` 已加入 `.gitignore`。

## 署名

站在这巨人肩膀上：[完整署名列表](ATTRIBUTIONS.md)

## 许可证

MIT — 随便用，署名更好。

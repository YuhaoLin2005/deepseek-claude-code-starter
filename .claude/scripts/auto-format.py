#!/usr/bin/env python3
"""
Claude Code PostToolUse 自动格式化 hook。
Write/Edit 后对 web 前端文件自动运行 prettier。
"""

import json
import os
import subprocess
import sys

WEB_EXTENSIONS = (".vue", ".js", ".jsx", ".ts", ".tsx", ".css", ".scss", ".html", ".json", ".md")


def main():
    tool_input_raw = os.environ.get("CLAUDE_TOOL_INPUT", "{}")
    try:
        tool_input = json.loads(tool_input_raw)
    except json.JSONDecodeError:
        tool_input = {}

    file_path = tool_input.get("file_path", "") or tool_input.get("path", "")
    if not file_path:
        sys.exit(0)

    # 只格式化 web 前端文件
    if not file_path.endswith(WEB_EXTENSIONS):
        sys.exit(0)

    # 排除 node_modules
    if "node_modules" in file_path:
        sys.exit(0)

    # 尝试本地 prettier（项目 node_modules），然后全局
    for cmd in [
        ["npx", "--no", "prettier", "--write", file_path],
        ["prettier", "--write", file_path],
    ]:
        try:
            result = subprocess.run(cmd, timeout=10, capture_output=True, text=True)
            if result.returncode == 0:
                sys.exit(0)
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue

    # prettier 不可用，安静跳过
    sys.exit(0)


if __name__ == "__main__":
    main()

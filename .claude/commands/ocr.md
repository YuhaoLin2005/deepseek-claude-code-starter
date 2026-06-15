---
description: 用 EasyOCR 识别截图中的文字
---

# /ocr — 截图文字识别

使用 EasyOCR（离线，免 API Key）识别截图中的文字。

## 使用方法

用户提供图片路径后，执行：

```bash
python ~/.claude/scripts/ocr.py <image_path>
```

如果用户提供的是目录，识别目录下所有图片。

## 参数

- `--raw`：只输出纯文本，不带置信度
- `--lang ch_sim,en`：指定语言（默认中英文）

## 备选方案

如果 EasyOCR 脚本不可用，用 Python 内联执行：
```python
import easyocr
reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
results = reader.readtext('<image_path>')
for (_, text, prob) in results:
    print(f"[{prob:.2f}] {text}")
```

## 输出

格式化显示每个识别区域的文本和置信度。

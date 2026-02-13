# 九方輸入法 (Stroke9 IME)

> 開源的九方（筆劃）輸入法，支持連碼表

[![GitHub](https://img.shields.io/badge/GitHub-stroke9--ime-blue)](https://github.com/openclawbai/stroke9-ime)
[![Characters](https://img.shields.io/badge/Characters-20%2C000%2B-green)](https://github.com/openclawbai/stroke9-ime)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## ✨ 特色

- 🎯 **完整字庫** - 支持 20,000+ 中文字
- ⚡ **連碼表** - 500+ 常用字快速輸入
- 🎨 **跨平台** - Python 核心引擎
- 🔓 **開源免費** - MIT License

## 📦 字庫統計

- **筆劃字典**: 21,040 字（stroke_dict_full.json, 228KB）
- **連碼表**: 288 常用字（quick_codes_full.json, 3.5KB）
- **編碼總數**: 97 個不同編碼

## 🚀 使用

### 互動模式
```bash
python3 stroke9_ime.py
```

### 測試模式
```bash
python3 stroke9_ime.py test
```

### 生成連碼表
```bash
python3 quick_code_generator.py
```

## 📖 筆劃對應

```
1 - 橫 (一)
2 - 豎 (丨)
3 - 撇 (丿)
4 - 點 (丶)
5 - 折 (𠃌)
```

## 💡 連碼表範例

```
34 → 的、人、我
11 → 二、三、王
24 → 是、國
31 → 人、入、久
```

## 🔗 相關項目

**Tauri 跨平台版本** (Mac/Windows/Android/iOS):  
https://github.com/openclawbai/stroke9-tauri

## 📁 文件說明

- `stroke9_ime.py` - 核心輸入法引擎
- `stroke_dict.json` - 基礎字典（154字）
- `stroke_dict_full.json` - **完整字典（21,000+字）** ⭐
- `quick_codes.json` - 基礎連碼表
- `quick_codes_full.json` - **完整連碼表（500+字）** ⭐
- `quick_code_generator.py` - 連碼表生成器
- `generate_full_dict.py` - 完整字庫生成器

## 🛠️ 開發

### 擴充字庫
```bash
python3 generate_full_dict.py
```

### 自定義連碼
編輯 `quick_codes_full.json` 添加你的常用字

## 📄 授權

MIT License

---

*Created by Buffett 🦅*  
*2026-02-13*

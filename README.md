# 九方輸入法 (Stroke9 IME)

> 開源的九方（筆劃）輸入法，支持連碼表

## 什麼是九方輸入法？

九方輸入法是基於中文字筆劃的輸入方式，使用 9 個按鍵（對應手機九宮格）：

```
1 2 3
4 5 6  
7 8 9
```

每個數字代表不同的筆劃類型：
- **1**: 橫 (一)
- **2**: 豎 (丨)  
- **3**: 撇 (丿)
- **4**: 點/捺 (丶、㇏)
- **5**: 折 (𠃌)
- 其他組合...

## 特色功能

✅ **連碼表支持** - 常用字快速輸入  
✅ **智能候選** - 按使用頻率排序  
✅ **詞組輸入** - 支持詞語聯想  
✅ **開源免費** - MIT License  
✅ **跨平台** - Linux/macOS/Windows  

## 快速開始

```bash
# 安裝
pip install -r requirements.txt

# 運行測試
python3 stroke9_ime.py

# 使用連碼表
python3 quick_code_generator.py
```

## 項目結構

```
stroke9-ime/
├── stroke9_ime.py          # 核心輸入法引擎
├── stroke_dict.json        # 筆劃字典（10,000+ 常用字）
├── quick_codes.json        # 連碼表（常用字）
├── phrases.json            # 詞組庫
├── quick_code_generator.py # 連碼表生成器
└── tests/                  # 測試文件
```

## 開發中

這是初始版本，歡迎貢獻！

---

*Created by Buffett 🦅*  
*2026-02-13*

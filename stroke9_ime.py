#!/usr/bin/env python3
"""
九方輸入法核心引擎
Stroke9 IME - Open Source Chinese Input Method
"""

import json
import os
from typing import List, Dict, Tuple


class Stroke9IME:
    """九方輸入法引擎"""
    
    # 筆劃映射（基於九宮格）
    STROKE_MAP = {
        '1': '橫',  # 一
        '2': '豎',  # 丨
        '3': '撇',  # 丿
        '4': '點',  # 丶
        '5': '折',  # 𠃌
        '6': '橫折',
        '7': '豎鉤',
        '8': '撇點',
        '9': '折鉤'
    }
    
    def __init__(self, dict_file='stroke_dict.json', quick_codes_file='quick_codes.json'):
        """初始化輸入法"""
        self.stroke_dict = self.load_dict(dict_file)
        self.quick_codes = self.load_quick_codes(quick_codes_file)
        self.phrase_dict = {}
        self.input_buffer = ""
        
    def load_dict(self, filename: str) -> Dict:
        """加載筆劃字典"""
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # 創建基礎字典
            return self.create_basic_dict()
    
    def load_quick_codes(self, filename: str) -> Dict:
        """加載連碼表（常用字快速編碼）"""
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return self.create_basic_quick_codes()
    
    def create_basic_dict(self) -> Dict:
        """創建基礎筆劃字典"""
        # 基礎字典（常用字範例）
        basic_dict = {
            # 簡單字
            '1': ['一'],  # 橫
            '2': ['丨'],  # 豎
            '3': ['丿'],  # 撇
            '4': ['丶'],  # 點
            
            # 兩筆字
            '11': ['二', '十'],
            '12': ['丁', '下'],
            '13': ['丈'],
            '14': ['七'],
            '21': ['上'],
            '31': ['人', '入'],
            '34': ['八'],
            
            # 三筆字
            '111': ['三', '王'],
            '121': ['工'],
            '131': ['大'],
            '134': ['太'],
            '211': ['土'],
            '311': ['久'],
            '312': ['小'],
            '314': ['少'],
            '341': ['不'],
            '414': ['心'],
            
            # 四筆字
            '1111': ['開'],
            '1121': ['天'],
            '1211': ['井'],
            '1312': ['水'],
            '1341': ['木'],
            '2111': ['下'],
            '3112': ['小'],
            '3134': ['今'],
            '3414': ['心'],
            '4134': ['文'],
            
            # 五筆字
            '11121': ['正'],
            '12134': ['生'],
            '31134': ['出'],
            '31214': ['世'],
            '34134': ['本'],
            
            # 常用複雜字
            '1111234': ['開'],
            '121341': ['國'],
            '312341': ['家']
        }
        
        # 保存
        with open('stroke_dict.json', 'w', encoding='utf-8') as f:
            json.dump(basic_dict, f, ensure_ascii=False, indent=2)
        
        return basic_dict
    
    def create_basic_quick_codes(self) -> Dict:
        """創建基礎連碼表（取首尾筆劃）"""
        quick_codes = {
            # 常用字連碼（首筆 + 尾筆）
            '11': ['二', '三', '王', '開'],
            '12': ['丁', '天', '未'],
            '13': ['大', '夫'],
            '14': ['不', '木', '本'],
            '15': ['也', '電'],
            
            '21': ['上', '土', '正'],
            '22': ['日', '田', '里'],
            '23': ['山'],
            '24': ['止', '此'],
            
            '31': ['人', '入', '久', '今'],
            '32': ['八', '公'],
            '33': ['多'],
            '34': ['文', '方'],
            
            '41': ['下', '不'],
            '42': ['之', '心'],
            '43': ['水'],
            '44': ['小', '少', '為'],
            
            '51': ['也', '已'],
            '52': ['弓'],
            '54': ['女'],
            
            # 超常用字（單碼）
            '0': ['的', '了', '是', '在', '我', '有', '他', '這', '你', '們']
        }
        
        with open('quick_codes.json', 'w', encoding='utf-8') as f:
            json.dump(quick_codes, f, ensure_ascii=False, indent=2)
        
        return quick_codes
    
    def get_stroke_sequence(self, char: str) -> str:
        """
        獲取字的筆劃序列
        （簡化版本，真實需要完整的筆劃數據庫）
        """
        # 在完整版本中，這裡應該查詢筆劃數據庫
        # 現在返回反向查找結果
        for code, chars in self.stroke_dict.items():
            if char in chars:
                return code
        return ""
    
    def search(self, code: str, use_quick_codes: bool = True) -> List[str]:
        """
        根據編碼搜索候選字
        
        Args:
            code: 筆劃編碼（如 "1234"）
            use_quick_codes: 是否使用連碼表
        
        Returns:
            候選字列表
        """
        candidates = []
        
        # 1. 優先查連碼表
        if use_quick_codes and code in self.quick_codes:
            candidates.extend(self.quick_codes[code])
        
        # 2. 查完整筆劃字典
        if code in self.stroke_dict:
            for char in self.stroke_dict[code]:
                if char not in candidates:
                    candidates.append(char)
        
        # 3. 模糊匹配（前綴匹配）
        if not candidates:
            for stroke_code, chars in self.stroke_dict.items():
                if stroke_code.startswith(code):
                    candidates.extend(chars)
                if len(candidates) >= 10:
                    break
        
        return candidates[:10]  # 最多返回 10 個候選
    
    def input_key(self, key: str) -> List[str]:
        """
        輸入一個按鍵
        
        Args:
            key: 按鍵 ('1'-'9')
        
        Returns:
            更新後的候選字列表
        """
        if key in '123456789':
            self.input_buffer += key
        
        return self.search(self.input_buffer)
    
    def clear_buffer(self):
        """清空輸入緩存"""
        self.input_buffer = ""
    
    def select_candidate(self, index: int, candidates: List[str]) -> str:
        """
        選擇候選字
        
        Args:
            index: 候選字索引
            candidates: 候選字列表
        
        Returns:
            選中的字
        """
        if 0 <= index < len(candidates):
            selected = candidates[index]
            self.clear_buffer()
            return selected
        return ""


def interactive_demo():
    """互動演示"""
    print("""
╔══════════════════════════════════════════════════════════╗
║   九方輸入法 (Stroke9 IME) - 互動演示                   ║
╚══════════════════════════════════════════════════════════╝

筆劃對應：
  1-橫(一)  2-豎(丨)  3-撇(丿)
  4-點(丶)  5-折(𠃌)

連碼表：取首尾筆劃快速輸入

輸入 'help' 查看幫助
輸入 'quit' 退出
    """)
    
    ime = Stroke9IME()
    
    while True:
        print(f"\n當前輸入: [{ime.input_buffer}]")
        
        # 顯示當前候選
        if ime.input_buffer:
            candidates = ime.search(ime.input_buffer)
            if candidates:
                print("候選字:")
                for i, char in enumerate(candidates):
                    print(f"  {i+1}. {char}")
            else:
                print("  (無匹配)")
        
        user_input = input("\n> ").strip()
        
        if user_input == 'quit':
            break
        elif user_input == 'help':
            print("\n命令:")
            print("  1-9: 輸入筆劃")
            print("  clear: 清空")
            print("  選擇: 輸入數字選候選字")
        elif user_input == 'clear':
            ime.clear_buffer()
        elif user_input in '123456789':
            # 輸入筆劃
            candidates = ime.input_key(user_input)
        elif user_input.isdigit() and int(user_input) > 0:
            # 選擇候選
            candidates = ime.search(ime.input_buffer)
            if candidates:
                idx = int(user_input) - 1
                selected = ime.select_candidate(idx, candidates)
                if selected:
                    print(f"\n✅ 輸出: {selected}")
        else:
            # 直接輸入多個按鍵
            ime.clear_buffer()
            for key in user_input:
                if key in '123456789':
                    ime.input_key(key)


def batch_test():
    """批量測試"""
    print("📝 批量測試九方輸入法\n")
    
    ime = Stroke9IME()
    
    test_cases = [
        ('1', ['一']),
        ('11', ['二', '十']),
        ('111', ['三', '王']),
        ('31', ['人', '入']),
        ('121', ['工']),
        ('312', ['小']),
    ]
    
    print("測試案例:")
    for code, expected in test_cases:
        result = ime.search(code)
        match = any(char in result for char in expected)
        status = "✅" if match else "❌"
        print(f"{status} 編碼 '{code}': {result[:3]} (預期包含 {expected})")
    
    print("\n連碼表測試:")
    quick_test = [
        ('11', '常用字如: 二、三、王'),
        ('31', '常用字如: 人、入'),
        ('0', '超常用: 的、了、是')
    ]
    
    for code, desc in quick_test:
        result = ime.search(code, use_quick_codes=True)
        print(f"  {code}: {result[:5]} - {desc}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        batch_test()
    else:
        interactive_demo()

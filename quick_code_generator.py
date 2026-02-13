#!/usr/bin/env python3
"""
連碼表生成器
自動為常用字生成快速編碼（首筆 + 尾筆）
"""

import json
from typing import Dict, List


class QuickCodeGenerator:
    """連碼表生成器"""
    
    # 最常用的 500 個繁體中文字
    TOP_500_CHARS = """
的一是不了人我在有他這為之大來以個中上們到說國和地也子時道出而要於就下得可你年生自會那後能對著事其裡所去行過家十用發天如然作方成者多日都三小軍二無同麼經法當起與好看學進種將還分此心前面又定見只主沒公從
"""
    
    def __init__(self):
        self.quick_codes = {}
        self.stroke_map = {
            '一': '1', '丨': '2', '丿': '3', '丶': '4', '𠃌': '5',
            '橫': '1', '豎': '2', '撇': '3', '點': '4', '折': '5'
        }
    
    def get_first_stroke(self, char: str) -> str:
        """
        獲取字的首筆
        （簡化版，實際需要完整筆劃庫）
        """
        # 常見字的首筆映射（需要擴展）
        first_stroke_map = {
            '一': '1', '二': '1', '三': '1', '王': '1', '天': '1', '正': '1',
            '上': '2', '下': '1', '中': '2', '土': '1', '工': '1',
            '人': '3', '入': '3', '八': '3', '大': '1', '小': '2',
            '不': '1', '木': '1', '本': '1', '日': '2', '月': '3',
            '的': '3', '了': '5', '是': '2', '我': '3', '你': '3',
            '他': '3', '們': '3', '這': '4', '有': '1', '在': '1',
            '國': '2', '家': '4', '中': '2', '文': '4', '字': '4'
        }
        
        return first_stroke_map.get(char, '1')
    
    def get_last_stroke(self, char: str) -> str:
        """
        獲取字的尾筆
        （簡化版）
        """
        # 常見字的尾筆映射
        last_stroke_map = {
            '一': '1', '二': '1', '三': '1', '王': '1', '天': '4',
            '上': '1', '下': '4', '中': '2', '工': '1', '土': '1',
            '人': '4', '入': '4', '八': '4', '大': '4', '小': '3',
            '不': '4', '木': '4', '本': '4', '日': '2', '月': '1',
            '的': '4', '了': '2', '是': '4', '我': '4', '你': '2',
            '他': '2', '們': '2', '這': '2', '有': '5', '在': '1',
            '國': '4', '家': '4', '中': '2', '文': '4', '字': '4'
        }
        
        return last_stroke_map.get(char, '1')
    
    def generate_quick_code(self, char: str) -> str:
        """
        生成連碼（首筆 + 尾筆）
        
        例如: '國' = 豎(2) + 點(4) = '24'
        """
        first = self.get_first_stroke(char)
        last = self.get_last_stroke(char)
        
        return first + last
    
    def build_quick_codes(self, chars: List[str]) -> Dict:
        """為字符列表建立連碼表"""
        quick_codes = {}
        
        for char in chars:
            if char.strip():
                code = self.generate_quick_code(char)
                
                if code not in quick_codes:
                    quick_codes[code] = []
                
                if char not in quick_codes[code]:
                    quick_codes[code].append(char)
        
        return quick_codes
    
    def save_quick_codes(self, filename='quick_codes_generated.json'):
        """保存生成的連碼表"""
        # 使用常用字生成
        common_chars = list(self.TOP_500_CHARS)
        quick_codes = self.build_quick_codes(common_chars)
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(quick_codes, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 連碼表已生成: {filename}")
        print(f"📊 共 {len(quick_codes)} 個編碼")
        print(f"📝 覆蓋 {sum(len(chars) for chars in quick_codes.values())} 個字")
        
        # 顯示部分
        print(f"\n範例（前 10 個）:")
        for i, (code, chars) in enumerate(list(quick_codes.items())[:10]):
            print(f"  {code}: {chars[:5]}")
        
        return quick_codes


def main():
    """主程序"""
    print("""
╔══════════════════════════════════════════════════════════╗
║   九方連碼表生成器                                       ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    generator = QuickCodeGenerator()
    
    print("生成連碼表...\n")
    quick_codes = generator.save_quick_codes()
    
    print(f"\n使用方法:")
    print(f"  1. 查看 quick_codes_generated.json")
    print(f"  2. 複製到 quick_codes.json")
    print(f"  3. 重啟輸入法即可使用")


if __name__ == "__main__":
    main()

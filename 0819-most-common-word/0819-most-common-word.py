import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # 1. Chuyển danh sách banned thành 'set' để tìm kiếm nhanh hơn (O(1))
        banned_set = set(banned)
        
        # 2. Làm sạch đoạn văn: 
        # - re.sub(r'[^\w\s]', ' ', paragraph): Thay thế mọi ký tự không phải chữ/số bằng khoảng trắng
        # - .lower(): Chuyển tất cả thành chữ thường
        clean_paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()
        
        # 3. Tách đoạn văn thành danh sách các từ
        words = clean_paragraph.split()
        
        # 4. Đếm tần suất các từ KHÔNG nằm trong danh sách bị cấm
        counts = Counter(word for word in words if word not in banned_set)
        
        # 5. Trả về từ xuất hiện nhiều nhất (most_common(1) trả về list [(từ, số lần)])
        return counts.most_common(1)[0][0]
class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        # Khởi tạo biến đếm số lượng từ có chứa tiền tố 'pref'
        count = 0
        
        # Duyệt qua từng từ (word) trong danh sách 'words'
        for word in words:
            # Hàm startswith() sẽ trả về True nếu 'word' bắt đầu bằng 'pref'
            if word.startswith(pref):
                # Nếu đúng, tăng biến đếm lên 1
                count += 1
                
        # Trả về kết quả cuối cùng
        return count
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        
        result = []
        for word in words:
            # Bước 2: Kiểm tra độ dài của từng từ
            if len(word) <= 2:
                # Nếu từ ngắn (<= 2), viết thường toàn bộ
                result.append(word.lower())
            else:
                # Nếu từ dài (>= 3), viết hoa chữ đầu, còn lại viết thường
                # Hàm .capitalize() dùng để chuyển đổi ký tự đầu tiên của chuỗi thành chữ hoa và tất cả các ký tự còn lại thành chữ thường
                result.append(word.capitalize())
        
        # Bước 3: Nối các từ lại bằng dấu cách
        return " ".join(result)
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counts = {}
        
        # Bước 1: Đếm tần suất từng ký tự
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        # Bước 2: Lấy danh sách các giá trị tần suất
        frequencies = counts.values()
        
        # Bước 3: Kiểm tra xem tất cả các giá trị có bằng nhau không
        # Chuyển list frequencies thành set sẽ loại bỏ các giá trị trùng lặp
        return len(set(frequencies)) == 1
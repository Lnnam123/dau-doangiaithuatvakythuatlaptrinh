class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Bước 1: Lấy tất cả các chữ số duy nhất có trong chuỗi
        digits = set()
        for char in s:
            if char.isdigit():
                digits.add(int(char))
        
        # Bước 2: Chuyển set thành list và sắp xếp giảm dần
        sorted_digits = sorted(list(digits), reverse=True)
        
        # Bước 3: Nếu có ít nhất 2 chữ số khác nhau, trả về số thứ hai
        if len(sorted_digits) >= 2:
            return sorted_digits[1]
        
        # Ngược lại trả về -1
        return -1
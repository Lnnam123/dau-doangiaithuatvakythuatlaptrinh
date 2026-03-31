class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # BƯỚC 1: LÀM SẠCH CHUỖI
        chuoi_sach = []
        for ky_tu in s:
            # Hàm isalnum() kiểm tra xem ký tự có phải là chữ cái hoặc số không
            if ky_tu.isalnum():
                chuoi_sach.append(ky_tu.lower()) # Đổi thành chữ thường rồi cho vào mảng
                
        # BƯỚC 2: SO SÁNH VỚI CHUỖI ĐẢO NGƯỢC
        # Trong Python, cú pháp [::-1] dùng để đảo ngược mảng
        return chuoi_sach == chuoi_sach[::-1]
        
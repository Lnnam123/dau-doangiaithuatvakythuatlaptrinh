class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Chuyển chuỗi thành list để có thể sửa đổi từng phần tử
        a = list(s)
        
        # Duyệt qua các chỉ số lẻ (1, 3, 5...)
        for i in range(1, len(a), 2):
            # Lấy ký tự đứng trước: a[i-1]
            # Lấy giá trị số của chữ số hiện tại: int(a[i])
            # Tính ký tự mới bằng cách dùng mã ASCII
            prev_char = a[i-1]
            shift_amount = int(a[i])
            
            new_char = chr(ord(prev_char) + shift_amount)
            
            # Thay thế chữ số bằng ký tự mới
            a[i] = new_char
            
        # Nối lại thành chuỗi hoàn chỉnh
        return "".join(a)
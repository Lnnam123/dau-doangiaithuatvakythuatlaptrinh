class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Xác định dấu của số
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        res = 0
        while x != 0:
            # Lấy chữ số cuối
            digit = x % 10
            # Cập nhật số x
            x //= 10
            
            # Đẩy vào kết quả
            res = res * 10 + digit
            
        # Kiểm tra giới hạn 32-bit
        # 2^31 - 1 = 2147483647
        if res > 2**31 - 1:
            return 0
            
        return res * sign
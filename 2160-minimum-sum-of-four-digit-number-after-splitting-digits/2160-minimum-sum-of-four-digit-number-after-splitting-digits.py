class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Bước 1: Tách các chữ số ra và cho vào một danh sách
        # Chuyển số thành chuỗi, sau đó chuyển từng ký tự ngược lại thành số
        digits = sorted([int(d) for d in str(num)])
        
        # Bước 2: Sau khi sắp xếp, digits sẽ có dạng [a, b, c, d]
        # a, b là hai số nhỏ nhất -> cho làm hàng chục
        # c, d là hai số lớn hơn -> cho làm hàng đơn vị
        
        # Công thức: (a * 10 + c) + (b * 10 + d)
        # Tương đương với: (a + b) * 10 + (c + d)
        
        ans = (digits[0] + digits[1]) * 10 + (digits[2] + digits[3])
        
        return ans
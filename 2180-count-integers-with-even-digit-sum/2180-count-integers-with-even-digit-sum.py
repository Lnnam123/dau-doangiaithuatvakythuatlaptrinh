class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        # Duyệt qua từng số từ 1 đến num
        for i in range(1, num + 1):
            # Tính tổng các chữ số của i
            digit_sum = 0
            temp = i
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            
            # Nếu tổng là chẵn, tăng biến đếm
            if digit_sum % 2 == 0:
                count += 1
                
        return count
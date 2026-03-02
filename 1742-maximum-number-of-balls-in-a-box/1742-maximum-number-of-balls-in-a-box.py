class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = {} # Dictionary lưu trữ {số_hiệu_hộp: số_lượng_bóng}
        
        for n in range(lowLimit, highLimit + 1):
            # Tính tổng các chữ số của n
            digit_sum = 0
            temp = n
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            
            # Thêm bóng vào hộp tương ứng
            if digit_sum in boxes:
                boxes[digit_sum] += 1
            else:
                boxes[digit_sum] = 1
                
        # Trả về số lượng bóng lớn nhất trong một hộp
        return max(boxes.values())
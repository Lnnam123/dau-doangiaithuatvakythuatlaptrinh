class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        trai = 0
        phai = len(numbers) - 1
        
        while trai < phai:
            tong_hien_tai = numbers[trai] + numbers[phai]
            
            if tong_hien_tai == target:
                # Đề bài yêu cầu index bắt đầu từ 1 (1-indexed) thay vì 0, 
                # nên ta phải cộng 1 vào kết quả trả về.
                return [trai + 1, phai + 1]
                
            elif tong_hien_tai < target:
                # Tổng còn thiếu -> Cần số lớn hơn
                trai += 1
                
            else:
                # Tổng bị dư -> Cần số nhỏ hơn
                phai -= 1
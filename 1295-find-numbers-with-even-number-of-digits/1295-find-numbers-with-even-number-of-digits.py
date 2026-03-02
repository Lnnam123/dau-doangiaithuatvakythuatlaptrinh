class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        for num in nums:
            # Bước 1: Chuyển số thành chuỗi, ví dụ: 121 -> "121"
            s = str(num)
            
            # Bước 2: Kiểm tra độ dài chuỗi có chia hết cho 2 không
            if len(s) % 2 == 0:
                count += 1
                
        return count
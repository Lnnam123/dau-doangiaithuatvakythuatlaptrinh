class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        
        # Bước 1: Đếm tần suất
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        # Bước 2: Tính tổng các số có tần suất bằng 1
        total_sum = 0
        for num in counts:
            if counts[num] == 1:
                total_sum += num
                
        return total_sum
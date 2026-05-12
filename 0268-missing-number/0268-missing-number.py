class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Tổng lý thuyết từ 0 đến n
        expected_sum = n * (n + 1) // 2
        # Tổng thực tế trong mảng
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum
class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bước 1: Tìm giá trị nhỏ nhất và lớn nhất
        min_val = min(nums)
        max_val = max(nums)
        
        count = 0
        # Bước 2: Đếm các phần tử nằm "kẹp" ở giữa
        for x in nums:
            if min_val < x < max_val:
                count += 1
                
        return count
class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Sắp xếp từ bé đến lớn
        nums.sort()
        
        # Duyệt qua từng cặp 2 số
        for i in range(0, len(nums), 2):
            # Tráo đổi vị trí: Số của Bob lên trước, số của Alice ra sau
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            
        # Trả về chính mảng gốc đã được tráo đổi
        return nums
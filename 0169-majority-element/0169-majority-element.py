class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        
        for num in nums:
            # Nếu số phiếu về 0, chọn ứng cử viên mới
            if count == 0:
                candidate = num
            
            # Nếu gặp người ủng hộ thì +1, gặp người phản đối thì -1
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate
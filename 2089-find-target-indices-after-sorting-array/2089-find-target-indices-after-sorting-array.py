class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #B1: Sap xep mang tang dan
        nums.sort()

        res = []
        #B2: Duyet qua mang da sap xep
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)

        return res
class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        
        # Vòng lặp i chạy từ 0 đến n-2
        for i in range(n):
            # Vòng lặp j chạy từ i+1 đến n-1
            for j in range(i + 1, n):
                # điều kiện 1: Giá trị bằng nhau
                if nums[i] == nums[j]:
                    # điều kiện 2: Tích chỉ số chia hết cho k
                    if (i * j) % k == 0:
                        count += 1
                        
        return count
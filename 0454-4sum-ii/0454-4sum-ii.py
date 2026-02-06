class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # 1. Tạo dictionary để lưu tổng của nums1 và nums2
        # Key: Tổng (sum), Value: Số lần xuất hiện của tổng đó
        sum_map = {}
        
        # 2. Vòng lặp tính tổng các cặp (a, b)
        for a in nums1:
            for b in nums2:
                current_sum = a + b
                # Tăng biến đếm cho tổng này trong map
                if current_sum in sum_map:
                    sum_map[current_sum] += 1
                else:
                    sum_map[current_sum] = 1
        
        count = 0
        
        # 3. Vòng lặp tính tổng các cặp (c, d) và tìm số đối
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                
                # Nếu số đối (target) tồn tại trong map, cộng dồn số lần xuất hiện
                if target in sum_map:
                    count += sum_map[target]
                    
        return count
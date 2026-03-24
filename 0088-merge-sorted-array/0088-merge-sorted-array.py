class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Ghi đè phần đuôi của nums1 (từ vị trí m đến hết) bằng toàn bộ nums2
        nums1[m:] = nums2

        # Sắp xếp lại toàn bộ mảng nums1 từ bé đến lớn
        nums1.sort()
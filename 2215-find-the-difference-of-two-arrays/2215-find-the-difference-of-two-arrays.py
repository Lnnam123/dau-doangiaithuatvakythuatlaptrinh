class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # Chuyển đổi mảng thành tập hợp (set). Việc này tự động loại bỏ các số trùng lặp.
        tap_hop_1 = set(nums1)
        tap_hop_2 = set(nums2)
        
        # tap_hop_1 - tap_hop_2: Lấy các số có trong mảng 1 nhưng KHÔNG có trong mảng 2
        # Ép kiểu về lại thành danh sách (list) vì đề bài yêu cầu trả về list
        ket_qua_1 = list(tap_hop_1 - tap_hop_2)
        
        # tap_hop_2 - tap_hop_1: Lấy các số có trong mảng 2 nhưng KHÔNG có trong mảng 1
        ket_qua_2 = list(tap_hop_2 - tap_hop_1)
        
        # Gộp 2 danh sách lại thành một danh sách lớn chứa 2 danh sách con
        return [ket_qua_1, ket_qua_2]
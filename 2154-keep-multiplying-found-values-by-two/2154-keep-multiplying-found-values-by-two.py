class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        # Bước 1: Chuyển mảng thành Set để tìm kiếm cực nhanh
        num_set = set(nums)
        
        # Bước 2: Lặp cho đến khi không tìm thấy 'original' trong Set nữa
        while original in num_set:
            # Nếu tìm thấy, nhân đôi giá trị
            original *= 2
            
        # Bước 3: Trả về kết quả cuối cùng
        return original
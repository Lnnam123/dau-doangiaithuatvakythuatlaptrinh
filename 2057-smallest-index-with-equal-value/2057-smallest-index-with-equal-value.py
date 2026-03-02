class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Duyệt qua từng chỉ số i từ 0 đến hết mảng
        for i in range(len(nums)):
            # Kiểm tra điều kiện: i chia 10 lấy dư có bằng nums[i] không
            if i % 10 == nums[i]:
                # Vì duyệt từ 0 nên phần tử đầu tiên thỏa mãn chính là số nhỏ nhất
                return i
        
        # Nếu đi hết vòng lặp mà không tìm thấy kết quả
        return -1
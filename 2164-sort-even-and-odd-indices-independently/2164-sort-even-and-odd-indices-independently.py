class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Bước 1: Tách và Sắp xếp
        # nums[0::2] lấy các phần tử từ chỉ số 0, bước nhảy là 2 (0, 2, 4...)
        even = sorted(nums[0::2])
        
        # nums[1::2] lấy các phần tử từ chỉ số 1, bước nhảy là 2 (1, 3, 5...)
        # reverse=True để sắp xếp giảm dần
        odd = sorted(nums[1::2], reverse=True)
        
        # Bước 2: Gộp lại vào mảng kết quả
        res = [0] * len(nums)
        
        # Gán lại các phần tử chẵn vào vị trí chẵn
        res[0::2] = even
        # Gán lại các phần tử lẻ vào vị trí lẻ
        res[1::2] = odd
        
        return res
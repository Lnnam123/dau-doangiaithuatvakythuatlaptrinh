class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Giả sử số đầu tiên trong mảng là số gần 0 nhất (quán quân tạm thời)
        ket_qua = nums[0]
        
        # Duyệt qua từng số trong mảng để so sánh
        for so in nums:
            khoang_cach_hien_tai = abs(so)
            khoang_cach_nho_nhat = abs(ket_qua)
            
            # TH1: Tìm thấy số có khoảng cách gần 0 hơn
            if khoang_cach_hien_tai < khoang_cach_nho_nhat:
                ket_qua = so  # Cập nhật kq mới
                
            # TH2: Khoảng cách bằng nhau, nhưng số hiện tại LỚN HƠN (ưu tiên số dương)
            elif khoang_cach_hien_tai == khoang_cach_nho_nhat and so > ket_qua:
                ket_qua = so  # Cập nhật kết quả mới
                
        # Trả về kết quả cuối cùng sau khi đã duyệt hết mảng
        return ket_qua
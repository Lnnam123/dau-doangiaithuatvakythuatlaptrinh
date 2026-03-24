class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Đặt 2 con trỏ ở 2 đầu của mảng
        trai = 0
        phai = len(nums) - 1
        
        # Lặp chừng nào vùng tìm kiếm vẫn còn hợp lệ (con trỏ trái chưa vượt quá con trỏ phải)
        # chú ý: Phải có dấu bằng (<=) để xét nốt trường hợp mảng chỉ còn đúng 1 phần tử
        while trai <= phai:
            
            # Tìm vị trí chính giữa
            # (Dùng phép chia nguyên // để lấy phần nguyên, ví dụ 5 // 2 = 2)
            giua = (trai + phai) // 2
            
            # TH1: Bắt trúng đích ngay tại điểm giữa!
            if nums[giua] == target:
                return giua
                
            # TH2: Số ở giữa nhỏ hơn mục tiêu
            # -> Mục tiêu phải nằm ở nửa bên phải. Xóa sổ nửa bên trái.
            elif nums[giua] < target:
                trai = giua + 1  # Nhích con trỏ trái qua khỏi điểm giữa
                
            # TH3: Số ở giữa lớn hơn mục tiêu
            # -> Mục tiêu phải nằm ở nửa bên trái. Xóa sổ nửa bên phải.
            else:
                phai = giua - 1  # Lùi con trỏ phải qua khỏi điểm giữa
                
        # Lật tung cả mảng (trai > phai) mà vẫn không thấy mục tiêu đâu
        return -1
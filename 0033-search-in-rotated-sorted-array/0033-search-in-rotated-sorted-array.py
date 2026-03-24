class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        trai = 0
        phai = len(nums) - 1
        
        while trai <= phai:
            giua = (trai + phai) // 2
            
            # Khớp lệnh ngay tại điểm giữa
            if nums[giua] == target:
                return giua
                
            # TH1: Nửa bên trái là mảng tăng dần chuẩn
            if nums[trai] <= nums[giua]:
                # Kiểm tra target có nằm trong khoảng chuẩn này không
                if nums[trai] <= target < nums[giua]:
                    phai = giua - 1  # Có -> Thu hẹp về bên trái
                else:
                    trai = giua + 1  # Không -> Bỏ qua nửa trái, đi tìm nửa phải
                    
            # TH2: Nửa bên trái bị gãy -> Nửa bên phải chuẩn
            else:
                # Kiểm tra target có nằm trong khoảng chuẩn của nửa phải không
                if nums[giua] < target <= nums[phai]:
                    trai = giua + 1  # Có -> Thu hẹp về bên phải
                else:
                    phai = giua - 1  # Không -> Bỏ qua nửa phải, đi tìm nửa trái
                    
        # Lật tung cả mảng mà không thấy
        return -1
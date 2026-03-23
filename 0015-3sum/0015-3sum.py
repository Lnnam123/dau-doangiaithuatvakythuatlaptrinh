class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # BƯỚC 1: Bắt buộc phải sắp xếp mảng từ bé đến lớn
        nums.sort()
        ket_qua = []
        n = len(nums)
        
        # BƯỚC 2: Duyệt qua mảng để chọn số thứ nhất (chỉ cần chạy đến n-2)
        for i in range(n - 2):
            # Tối ưu: Nếu số nhỏ nhất mà đã lớn hơn 0, thì tổng 3 số chắc chắn > 0, dừng luôn
            if nums[i] > 0:
                break
                
            # Tránh trùng lặp cho số thứ nhất: Bỏ qua nếu giống số liền trước
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # BƯỚC 3: Đặt 2 con trỏ ở đoạn mảng phía sau số thứ nhất
            trai = i + 1
            phai = n - 1
            
            while trai < phai:
                tong = nums[i] + nums[trai] + nums[phai]
                
                if tong == 0:
                    # Tìm thấy một bộ 3 số thỏa mãn
                    ket_qua.append([nums[i], nums[trai], nums[phai]])
                    
                    # Thu hẹp cả 2 con trỏ để tiếp tục tìm các bộ số khác
                    trai += 1
                    phai -= 1
                    
                    # Tránh trùng lặp cho số thứ hai và thứ ba
                    while trai < phai and nums[trai] == nums[trai - 1]:
                        trai += 1
                    while trai < phai and nums[phai] == nums[phai + 1]:
                        phai -= 1
                        
                elif tong < 0:
                    # Tổng đang bị âm (nhỏ hơn 0), cần số lớn hơn -> Nhích con trỏ trái
                    trai += 1
                else:
                    # Tổng đang dương (lớn hơn 0), cần số nhỏ hơn -> Nhích con trỏ phải
                    phai -= 1
                    
        return ket_qua
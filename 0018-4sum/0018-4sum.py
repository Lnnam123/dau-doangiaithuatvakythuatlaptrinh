class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #B1: sắp xếp mảng từ bé đến lớn
        nums.sort()
        n = len(nums)
        ket_qua = []
        
        #B2: Vòng lặp chốt số thứ nhất (chỉ chạy đến n-3 vì cần chừa chỗ cho 3 số sau)
        for i in range(n - 3):
            # Né trùng lặp cho số thứ nhất
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # B3: Vòng lặp chốt số thứ hai (chạy từ sau i, chừa chỗ cho 2 số cuối)
            for j in range(i + 1, n - 2):
                # Né trùng lặp cho số thứ hai 
                # Lưu ý: j > i + 1 để đảm bảo ta chỉ xét trùng lặp với các số CÙNG LƯỢT chạy của j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # B4: Hai con trỏ cho đoạn mảng còn lại
                trai = j + 1
                phai = n - 1
                
                while trai < phai:
                    tong = nums[i] + nums[j] + nums[trai] + nums[phai]
                    
                    if tong == target:
                        # Tìm thấy bộ 4 số thỏa mãn
                        ket_qua.append([nums[i], nums[j], nums[trai], nums[phai]])
                        
                        trai += 1
                        phai -= 1
                        
                        # Né trùng lặp cho số thứ ba và thứ tư
                        while trai < phai and nums[trai] == nums[trai - 1]:
                            trai += 1
                        while trai < phai and nums[phai] == nums[phai + 1]:
                            phai -= 1
                            
                    elif tong < target:
                        # Tổng đang nhỏ hơn mục tiêu -> Cần số lớn hơn -> Nhích con trỏ trái
                        trai += 1
                    else:
                        # Tổng đang lớn hơn mục tiêu -> Cần số nhỏ hơn -> Nhích con trỏ phải
                        phai -= 1
                        
        return ket_qua
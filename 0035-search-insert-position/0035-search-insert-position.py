class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        trai = 0
        phai = len(nums) - 1
        
        while trai <= phai:
            giua = (trai + phai) // 2
            
            # Nếu tìm thấy đích danh con số đó, trả về vị trí luôn
            if nums[giua] == target:
                return giua
                
            # Nếu số ở giữa nhỏ hơn mục tiêu -> Phải tìm ở nửa bên phải
            elif nums[giua] < target:
                trai = giua + 1
                
            # Nếu số ở giữa lớn hơn mục tiêu -> Phải tìm ở nửa bên trái
            else:
                phai = giua - 1
                
        # Nếu vòng lặp kết thúc mà vẫn không tìm thấy, 
        # con trỏ 'trai' lúc này chính là vị trí chèn hoàn hảo nhất.
        return trai
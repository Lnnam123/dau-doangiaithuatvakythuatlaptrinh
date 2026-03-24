class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        # Mốc ban đầu (Mảng luôn có >= 3 phần tử theo yêu cầu đề bài)
        tong_gan_nhat = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            trai = i + 1
            phai = n - 1
            
            while trai < phai:
                tong_hien_tai = nums[i] + nums[trai] + nums[phai]
                
                if tong_hien_tai == target:
                    return tong_hien_tai
                    
                if abs(tong_hien_tai - target) < abs(tong_gan_nhat - target):
                    tong_gan_nhat = tong_hien_tai
                    
                if tong_hien_tai < target:
                    trai += 1
                else:
                    phai -= 1
                    
        return tong_gan_nhat
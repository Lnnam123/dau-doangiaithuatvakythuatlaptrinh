class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cuon_so = {}
        # Lay chieu dai cua mang de lam diem dung cho vong lap
        chieu_dai = len(nums)
        
        # Su dung range de tao ra cac chi so vi tri tu 0 tro di
        for vi_tri_hien_tai in range(chieu_dai):
            
            # Tu minh lay con so ra khoi mang thong qua chi so vi tri
            so = nums[vi_tri_hien_tai]
            
            # Kiem tra xem con so nay da duoc ghi vao so hay chua
            if so in cuon_so:
                # Lay vi tri cu roi cong them k, giong y het logic cu
                vi_tri_cu = cuon_so[so]
                if vi_tri_hien_tai <= vi_tri_cu + k:
                    return True
                    
            # Cap nhat vi tri moi nhat vao cuon so
            cuon_so[so] = vi_tri_hien_tai
            
        return False
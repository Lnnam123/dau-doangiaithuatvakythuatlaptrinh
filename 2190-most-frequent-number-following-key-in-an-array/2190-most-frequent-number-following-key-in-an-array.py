class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        cuon_so_dem = {} # Tạo một từ điển rỗng (như một cuốn sổ tay)
        
        # BƯỚC 1: ĐI TÌM VÀ ĐẾM
        # Duyệt qua từng số trong mảng (trừ số cuối cùng)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                so_lien_sau = nums[i + 1] # Lấy số đứng ngay sau key
                
                # Ghi chép vào sổ
                if so_lien_sau in cuon_so_dem:
                    cuon_so_dem[so_lien_sau] += 1 # Nếu đã có trong sổ, cộng thêm 1
                else:
                    cuon_so_dem[so_lien_sau] = 1  # Nếu chưa có, ghi vào sổ là 1
                    
        # BƯỚC 2: TÌM RA SỐ XUẤT HIỆN NHIỀU NHẤT TRONG SỔ
        so_quan_quan = 0     # Lưu lại cái tên (con số) chiến thắng
        so_lan_nhieu_nhat = 0 # Lưu lại kỷ lục số lần xuất hiện
        
        # Lật từng trang sổ ra xem
        for so, so_lan in cuon_so_dem.items():
            if so_lan > so_lan_nhieu_nhat:
                so_lan_nhieu_nhat = so_lan # Cập nhật kỷ lục mới
                so_quan_quan = so          # Cập nhật nhà vô địch mới
                
        return so_quan_quan
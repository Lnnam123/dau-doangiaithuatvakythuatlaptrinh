class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cuon_so_dem = {} # Vẫn là cuốn sổ tay để ghi chép
        
        # BƯỚC 1: ĐI ĐẾM SỐ LẦN XUẤT HIỆN CỦA TỪNG SỐ
        for so in nums:
            if so in cuon_so_dem:
                cuon_so_dem[so] += 1 # Đã có thì cộng thêm 1
            else:
                cuon_so_dem[so] = 1  # Chưa có thì ghi trang mới là 1
                
        # BƯỚC 2: KIỂM TRA SỐ CHẴN LẺ
        # Lật sổ ra, kiểm tra số lần xuất hiện (so_lan) của từng con số
        for so_lan in cuon_so_dem.values():
            if so_lan % 2 != 0: # Dấu % là chia lấy phần dư. Dư khác 0 nghĩa là số lẻ.
                return False    # Phát hiện chiếc "vớ" bị lẻ tẻ! Trả về False ngay.
                
        # Nếu kiểm tra hết cuốn sổ mà không có số nào bị lẻ, nghĩa là ghép đôi thành công!
        return True
class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # BƯỚC 1: RÚT GỌN MẢNG
        # Tạo một mảng mới, bỏ sẵn số đầu tiên vào
        mang_rut_gon = [nums[0]] 
        
        # Duyệt từ số thứ hai đến hết. Nếu khác số liền trước thì mới cho vào mảng.
        # Thao tác này giúp loại bỏ hoàn toàn các đoạn "bằng phẳng".
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                mang_rut_gon.append(nums[i])
                
        # BƯỚC 2: TÌM ĐỒI VÀ THUNG LŨNG
        dem = 0
        
        # Duyệt qua mảng mới (bỏ qua số đầu và số cuối vì chúng không thể là đồi/thung lũng)
        for i in range(1, len(mang_rut_gon) - 1):
            truoc = mang_rut_gon[i - 1]
            hien_tai = mang_rut_gon[i]
            sau = mang_rut_gon[i + 1]
            
            # Kiểm tra Đồi (đỉnh cao hơn hai bên)
            if truoc < hien_tai and hien_tai > sau:
                dem += 1
            # Kiểm tra Thung lũng (đáy thấp hơn hai bên)
            elif truoc > hien_tai and hien_tai < sau:
                dem += 1
                
        return dem
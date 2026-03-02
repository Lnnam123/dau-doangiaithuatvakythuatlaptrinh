class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        # Bước 1: Làm sạch chuỗi - xóa dấu cách và dấu gạch ngang
        clean_num = number.replace(" ", "").replace("-", "")
        
        res = []
        i = 0
        n = len(clean_num)
        
        # Bước 2: Duyệt chuỗi và lấy các nhóm 3 chữ số
        # Chúng ta chỉ làm điều này khi phần còn lại lớn hơn 4 chữ số
        while n - i > 4:
            res.append(clean_num[i:i+3])
            i += 3
            
        # Bước 3: Xử lý phần dư (4, 3 hoặc 2 chữ số cuối)
        remaining = n - i
        
        if remaining == 4:
            # Nếu còn 4 số, chia thành 2+2
            res.append(clean_num[i:i+2])
            res.append(clean_num[i+2:i+4])
        else:
            # Nếu còn 2 hoặc 3 số, giữ nguyên nhóm đó
            res.append(clean_num[i:])
            
        # Nối các nhóm lại bằng dấu gạch ngang "-"
        return "-".join(res)
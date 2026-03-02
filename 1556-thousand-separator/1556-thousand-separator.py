class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 1. Chuyển số n thành chuỗi để có thể duyệt từng ký tự
        n = str(n)
        s = ""      # Chuỗi kết quả tạm thời (sẽ bị ngược)
        count = 0   # Biến đếm để biết khi nào đã đủ 3 chữ số

        # 2. n[::-1] giúp đảo ngược chuỗi. 
        # Ví dụ: "1234" thành "4321"
        for i in n[::-1]:
            # Nếu đã đếm đủ 3 chữ số, thêm dấu chấm trước khi thêm chữ số tiếp theo
            if count == 3:
                s += "."
                count = 0 # Reset biến đếm về 0
            
            count += 1
            s += i # Thêm chữ số hiện tại vào chuỗi s

        # 3. Vì s đang bị ngược (ví dụ "432.1"), ta đảo ngược lại lần nữa
        return s[::-1]
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        trai = 0
        # Bức tường bên phải luôn được đặt ở vị trí lớn hơn x một đơn vị
        # Điều này đảm bảo 'phai' luôn là một đáp án sai (quá lớn)
        phai = x + 1
        
        # Vòng lặp chỉ chạy khi hai bức tường còn cách nhau nhiều hơn 1 bước
        # Sử dụng phép cộng thay vì phép trừ!
        while trai + 1 < phai:
            giua = (trai + phai) // 2
            
            # Nếu bình phương của số ở giữa vẫn nhỏ hơn hoặc bằng x
            if giua * giua <= x:
                # Nó là một đáp án hợp lệ, đẩy tường trái lên đây
                trai = giua
            else:
                # Nó quá lớn, kéo tường phải về đây
                phai = giua
                
        # Khi vòng lặp kết thúc, tường trái đứng ngay tại số nguyên lớn nhất thỏa mãn
        return trai  
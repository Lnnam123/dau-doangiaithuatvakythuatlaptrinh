class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ngan_xep = [] # Ống chứa các ngoặc mở
        
        # Cuốn sổ tra cứu: Lấy ngoặc đóng làm chìa khóa (key), ngoặc mở làm giá trị (value)
        tu_dien_ngoac = {')': '(', ']': '[', '}': '{'}
        
        for ngoac in s:
            # TH1: Ký tự hiện tại là ngoặc đóng (có trong cuốn sổ)
            if ngoac in tu_dien_ngoac:
                
                # Lấy ngoặc nằm trên cùng của ống ra. 
                # Nếu ống đang rỗng (thiếu ngoặc mở), ta trả về một ký tự rác (ví dụ '#')để so sánh thì bị False.
                ngoac_tren_cung = ngan_xep.pop() if ngan_xep else '#'
                
                # Tra sổ: Xem cái ngoặc đóng này có khớp với cái ngoặc mở trên cùng không?
                if tu_dien_ngoac[ngoac] != ngoac_tren_cung:
                    return False # Khớp trật lất -> Sai!
                    
            # TH2: Ký tự hiện tại là ngoặc mở
            else:
                ngan_xep.append(ngoac) # Cứ vô tư thả vào ống
                
        # Duyệt xong hết rồi. Nếu ống rỗng (len == 0) thì là chuỗi hợp lệ!
        return len(ngan_xep) == 0
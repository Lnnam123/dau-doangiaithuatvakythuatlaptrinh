class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cuon_so = {}
        trai = 0
        max_tan_suat = 0
        ket_qua = 0
        chieu_dai = len(s)
        giam = [0]
        giam_gia_tri = 0
        # Vong lap chay bang bien tam de xay dung bang tra cuu
        for vong_lap in range(chieu_dai + 2):
            giam.append(giam_gia_tri)
            giam_gia_tri += 1
            
        # DUYET MANG
        for phai in range(chieu_dai):
            ky_tu_phai = s[phai]
            
            # Ghi chep tan suat
            if ky_tu_phai in cuon_so:
                cuon_so[ky_tu_phai] += 1
            else:
                cuon_so[ky_tu_phai] = 1
                
            # Cap nhat tan suat lon nhat hien co
            if cuon_so[ky_tu_phai] > max_tan_suat:
                max_tan_suat = cuon_so[ky_tu_phai]
                
            # Chuyen ve doi dau de ne phep tru khi kiem tra kich thuoc
            if phai + 1 > max_tan_suat + k + trai:
                # Cua so vo ly, phai dich chuyen tuong trai va dung bang tra cuu de giam tan suat
                ky_tu_trai = s[trai]
                cuon_so[ky_tu_trai] = giam[cuon_so[ky_tu_trai]]
                trai += 1
            else:
                # Cua so hop le va phinh to, ta ghi nhan them chieu dai
                ket_qua += 1
                
        return ket_qua
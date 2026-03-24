# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Phạm vi đoán số bắt đầu từ 1 cho đến n
        trai = 1
        phai = n
        
        while trai <= phai:
            # Luôn đoán con số nằm ở chính giữa phạm vi hiện tại
            giua = (trai + phai) // 2
            
            # Hỏi quản trò xem con số 'giua' này đúng hay sai
            goi_y = guess(giua)
            
            if goi_y == 0:
                # Quản trò báo đúng (0) -> Chốt đơn, trả về kết quả!
                return giua
                
            elif goi_y == -1:
                # Quản trò báo -1 (Số bí mật NHỎ HƠN số ta đoán)
                # -> Loại bỏ nửa bên phải, thu hẹp phạm vi về bên trái
                phai = giua - 1
                
            else:
                # Quản trò báo 1 (Số bí mật LỚN HƠN số ta đoán)
                # -> Loại bỏ nửa bên trái, thu hẹp phạm vi về bên phải
                trai = giua + 1
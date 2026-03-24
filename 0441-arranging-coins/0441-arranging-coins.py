class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Buc tuong trai bat dau tu 0 (luon luon hop le vi luc nao cung xep duoc 0 hang)
        trai = 0
        
        # Buc tuong phai dat o vi tri chac chan thieu xu de tao thanh khoang vo ly
        phai = n + 1
        
        # Vong lap chi dung phep cong, chay den khi hai tuong sat vao nhau
        while trai + 1 < phai:
            giua = (trai + phai) // 2
            
            # Tinh xem neu muon xep 'giua' hang thi can bao nhieu xu
            so_xu_can_thiet = giua * (giua + 1) // 2
            
            # Kiem tra xem so xu dang co (n) co du de xep khong
            if so_xu_can_thiet <= n:
                # Neu du xu hoac vua khit, day tuong trai len de thu mo rong them hang
                trai = giua
            else:
                # Neu thieu xu, keo tuong phai ve day de gioi han lai
                phai = giua
                
        # Khi hai tuong sat vao nhau, tuong trai chinh la so hang hoan chinh lon nhat
        return trai
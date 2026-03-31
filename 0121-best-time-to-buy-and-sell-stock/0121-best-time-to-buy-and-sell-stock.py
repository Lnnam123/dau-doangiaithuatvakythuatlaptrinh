class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Muc loi nhuan thap nhat chac chan dat duoc la 0 (khong mua ban gi ca)
        trai = 0
        
        # Gia co phieu toi da la 10000, nen muc loi 10001 la chac chan vo ly
        phai = 10001
        
        # Kep tuong tim muc loi nhuan bang phep cong
        while trai + 1 < phai:
            giua = (trai + phai) // 2
            
            co_the_dat_duoc = False
            
            # Dat gia thap nhat ban dau la mot so lon hon moi gia co phieu
            gia_thap_nhat = 10001 
            
            # Duyet qua tung cot moc gia
            for gia in prices:
                # Cap nhat muc gia mua re nhat
                if gia < gia_thap_nhat:
                    gia_thap_nhat = gia
                    
                # Chuyen ve doi dau: gia >= gia_thap_nhat + loi_nhuan_mong_muon
                # Hoan toan khong co phep tru!
                if gia >= gia_thap_nhat + giua:
                    co_the_dat_duoc = True
                    break
                    
            if co_the_dat_duoc:
                # Neu dat duoc, day tuong trai len de thu tham lam muc loi cao hon
                trai = giua
            else:
                # Neu khong dat duoc, keo tuong phai ve de ha ky vong xuong
                phai = giua
                
        # Tuong trai dung lai o muc loi nhuan cao nhat co the dat duoc
        return trai
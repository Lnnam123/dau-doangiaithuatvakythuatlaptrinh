# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        trai = 1
        phai = n
        
        # Vong lap chay den khi hai buc tuong chap vao lam mot
        while trai < phai:
            giua = (trai + phai) // 2
            
            # Kiem tra xem phien ban o giua co bi loi khong
            if isBadVersion(giua):
                # Neu loi, keo tuong phai ve day de khoanh vung nua dau
                phai = giua
            else:
                # Neu tot, day tuong trai qua khoi diem nay de tim o nua sau
                trai = giua + 1
                
        # Khi hai tuong dung chung mot cho, do chinh la kq
        return trai
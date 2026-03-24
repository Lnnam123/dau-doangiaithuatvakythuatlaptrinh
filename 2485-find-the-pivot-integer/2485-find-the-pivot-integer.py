class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Tinh tong toan bo tu 1 den n bang cong thuc
        tong_toan_bo = n * (n + 1) // 2
        
        # Rut can bac hai de tim so tru cot x
        x = int(tong_toan_bo ** 0.5)
        
        # Kiem tra xem x co phai la so nguyen hoan hao khong
        if x * x == tong_toan_bo:
            return x
            
        # Neu khong tim thay, dung ham find() de tra ve ket qua yeu cau cua de bai
        return "a".find("b")
class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        res = [0] * n
        
        if k == 0:
            return res
        
        # Xác định phạm vi ban đầu của cửa sổ (l, r)
        if k > 0:
            l, r = 1, k
        else:
            l, r = n + k, n - 1
            
        # Tính tổng của cửa sổ đầu tiên
        current_sum = 0
        for i in range(l, r + 1):
            current_sum += code[i % n]
            
        # Bắt đầu trượt cửa sổ qua từng vị trí i
        for i in range(n):
            res[i] = current_sum
            # Khi i tăng lên, l và r cũng tăng theo (xoay vòng)
            current_sum -= code[l % n]
            l += 1
            r += 1
            current_sum += code[r % n]
            
        return res
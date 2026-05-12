class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # Tạo mảng đếm điểm cho n người (label từ 1 đến n nên dùng n + 1 phần tử)
        trust_scores = [0] * (n + 1)
        
        for a, b in trust:
            # a tin b => a mất điểm, b tăng điểm
            trust_scores[a] -= 1
            trust_scores[b] += 1
            
        # Kiểm tra xem có ai đạt điểm n - 1 không
        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i
                
        return -1
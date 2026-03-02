class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        t = []
        p = n // 2

        for i in range (1, p + 1):
            t.append(i)
            t.append(-i)
        if n % 2 !=0:
            t.append(0)
        return t
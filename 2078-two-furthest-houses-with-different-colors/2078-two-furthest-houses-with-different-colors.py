class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        res = 0

        # B1: So sánh nhà đầu tiên với các nhà khác từ cuối lên
        for i in range (n-1, 0, -1):
            if colors[i] != colors[0]:
                res = max (res, i)
                break

        #B2: So sánh nhà cuối cùng với các nhà khác từ đầu xuống
        for i in range (n-1):
            if colors[i] != colors[n-1]:
                res = max (res, n - 1 - i)
                break
        return res

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        n = len(timeSeries)

        if n == 0:
            return 0

        for i in range(n - 1):
            d = timeSeries[i + 1] - timeSeries[i]
            
            # Nếu khoảng cách giữa 2 lần đánh lớn hơn thời gian độc
            if d > duration:
                res += duration
            # Nếu đánh dồn dập (khoảng cách nhỏ hơn thời gian độc)
            else: 
                res += d 
        
        # Cộng thêm thời gian độc của lần đánh cuối cùng (luôn luôn là full duration)
        return res + duration
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        # Chạy vòng lặp cho đến khi n thành 1 hoặc rơi vào vòng lặp cũ
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
            
        return n == 1
class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Trường hợp 1: num là 0 -> True
        # Trường hợp 2: num không chia hết cho 10 (không kết thúc bằng 0) -> True
        return num == 0 or num % 10 != 0
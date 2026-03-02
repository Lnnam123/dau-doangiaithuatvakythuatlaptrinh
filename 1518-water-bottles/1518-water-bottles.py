class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # Tổng = Số chai ban đầu + Số lượng chai có thể đổi thêm bằng toán học
        # Chúng ta trừ 1 ở tử số và mẫu số để tính toán số lượt đổi tối đa mà vẫn giữ lại ít nhất 1 vỏ chai cuối cùng.
        return numBottles + (numBottles - 1) // (numExchange - 1)
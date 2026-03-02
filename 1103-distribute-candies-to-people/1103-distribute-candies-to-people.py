class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int (Tổng số kẹo)
        :type num_people: int (Số người)
        :rtype: List[int] (Danh sách kẹo mỗi người nhận được)
        """
        # Khởi tạo danh sách kết quả với toàn số 0
        res = [0] * num_people
        
        give = 1  # Số kẹo sẽ trao ở lượt đầu tiên
        i = 0     # Chỉ số của người nhận kẹo (bắt đầu từ người 0)
        
        while candies > 0:
            # Người hiện tại sẽ nhận giá trị nhỏ hơn giữa (số kẹo cần trao) và (số kẹo còn lại)
            amount_to_give = min(give, candies)
            
            # Cộng kẹo cho người ở vị trí i % num_people (để quay vòng lại đầu hàng)
            res[i % num_people] += amount_to_give
            
            # Trừ đi số kẹo đã trao khỏi tổng kho kẹo
            candies -= amount_to_give
            
            # Tăng số kẹo cho lượt sau và chuyển sang người tiếp theo
            give += 1
            i += 1
            
        return res
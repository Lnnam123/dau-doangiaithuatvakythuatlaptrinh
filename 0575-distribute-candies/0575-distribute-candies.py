class Solution(object):
    def distributeCandies(self, candyType):
        # Alice chỉ được ăn n / 2 viên kẹo
        limit = len(candyType) // 2
        
        # Tìm số lượng các loại kẹo khác nhau (loại bỏ trùng lặp)
        unique_candies = len(set(candyType))
        
        # Kết quả bị giới hạn bởi số nhỏ hơn trong 2 số này
        return min(unique_candies, limit)
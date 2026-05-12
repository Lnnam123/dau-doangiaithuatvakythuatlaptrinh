class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        
        # Nếu màu gốc đã là màu mới, trả về luôn để tránh lặp vô hạn
        if original_color == color:
            return image
        
        def dfs(r, c):
            # Kiểm tra biên giới và màu sắc
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            
            # Đổi màu ô hiện tại
            image[r][c] = color
            
            # Lan sang 4 hướng
            dfs(r + 1, c) # Xuống
            dfs(r - 1, c) # Trên
            dfs(r, c + 1) # Phải
            dfs(r, c - 1) # Trái
            
        dfs(sr, sc)
        return image
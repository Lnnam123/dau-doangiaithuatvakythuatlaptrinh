class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        
        def dfs(r, c):
            # Điều kiện dừng: 
            # - Ra ngoài biên của lưới
            # - Ô hiện tại là nước ('0')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Đánh dấu ô này là '0' (đã thăm/nhấn chìm) để không đếm lại
            grid[r][c] = '0'
            
            # Loang ra 4 hướng: Trên, Dưới, Trái, Phải
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Duyệt qua toàn bộ bản đồ
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c) # Bắt đầu loang để "xóa" hòn đảo này
                    
        return num_islands
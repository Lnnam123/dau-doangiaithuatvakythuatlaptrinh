class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Mỗi ô đất ban đầu đóng góp 4 cạnh
                    perimeter += 4
                    
                    # Nếu phía trên là đất, trừ đi 2 (cạnh chung)
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    
                    # Nếu bên trái là đất, trừ đi 2 (cạnh chung)
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
                        
        return perimeter
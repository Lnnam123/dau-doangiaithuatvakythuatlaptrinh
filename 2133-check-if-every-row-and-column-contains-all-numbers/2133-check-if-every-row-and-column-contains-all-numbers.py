class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        
        for i in range(n):
            row_set = set()
            col_set = set()
            
            for j in range(n):
                # Kiểm tra phần tử ở hàng i, cột j
                row_val = matrix[i][j]
                # Kiểm tra phần tử ở hàng j, cột i (để kiểm tra cột i)
                col_val = matrix[j][i]
                
                # Nếu giá trị đã tồn tại trong Set tức là bị lặp
                if row_val in row_set or col_val in col_set:
                    return False
                
                row_set.add(row_val)
                col_set.add(col_val)
                
        return True
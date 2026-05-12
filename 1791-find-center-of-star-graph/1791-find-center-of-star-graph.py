class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # Lấy ra 2 đỉnh của cạnh đầu tiên
        u1, v1 = edges[0]
        # Lấy ra 2 đỉnh của cạnh thứ hai
        u2, v2 = edges[1]
        
        # Nếu u1 xuất hiện ở cạnh thứ hai, nó là trung tâm
        if u1 == u2 or u1 == v2:
            return u1
        
        # Ngược lại, v1 phải là trung tâm
        return v1
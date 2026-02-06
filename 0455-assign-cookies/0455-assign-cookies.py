class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int] 
        :rtype: int 
        """
        # 1. Sắp xếp cả hai danh sách từ nhỏ đến lớn
        g.sort()
        s.sort()
        
        child_i = 0  # Con trỏ cho trẻ em
        cookie_j = 0 # Con trỏ cho bánh quy
        
        # 2. Duyệt qua danh sách bánh và trẻ
        while child_i < len(g) and cookie_j < len(s):
            # Kiểm tra xem bánh hiện tại (s[cookie_j]) có đủ cho trẻ hiện tại (g[child_i]) không
            if s[cookie_j] >= g[child_i]:
                # Nếu đủ, đứa trẻ này đã hài lòng -> Chuyển sang đứa trẻ tiếp theo
                child_i += 1
            
            # Dù bánh có vừa hay không, ta cũng chuyển sang chiếc bánh tiếp theo
            # (Nếu vừa thì bánh đã bị ăn, nếu không vừa thì bánh quá nhỏ, vứt bỏ để tìm bánh to hơn)
            cookie_j += 1
            
        # child_i chính là số lượng trẻ đã được thỏa mãn
        return child_i
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # TRƯỜNG HỢP 1: Cả hai cây đều trống hoặc ta đã duyệt hết nhánh
        if not p and not q:
            return True
        
        # TRƯỜNG HỢP 2: Một trong hai cây trống (nhưng cây kia thì không)
        # Hoặc giá trị tại nút hiện tại không giống nhau
        if not p or not q or p.val != q.val:
            return False
        
        # TRƯỜNG HỢP 3: Nếu nút hiện tại đã khớp, ta "ủy quyền" cho đệ quy
        # Kiểm tra đồng thời cả nhánh trái và nhánh phải.
        # Chỉ khi CẢ HAI nhánh đều True thì kết quả cuối cùng mới là True.
        
        check_left = self.isSameTree(p.left, q.left)
        check_right = self.isSameTree(p.right, q.right)
        
        return check_left and check_right
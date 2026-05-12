# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        # 1. Nếu cây gốc trống, chắc chắn không chứa subRoot (vì subRoot ít nhất có 1 nút)
        if not root:
            return False
        
        # 2. Nếu cây bắt đầu từ root hiện tại giống hệt subRoot, trả về True
        if self.isSameTree(root, subRoot):
            return True
        
        # 3. Nếu không khớp ở nút hiện tại, đi tìm tiếp ở nhánh trái HOẶC nhánh phải
        # Chỉ cần một trong hai nhánh chứa subRoot là đủ (Toán tử 'or')
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Hàm phụ hỗ trợ so khớp 2 cây (Logic bài 100)
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
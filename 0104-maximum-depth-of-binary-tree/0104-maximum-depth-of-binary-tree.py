# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Điều kiện dừng: Nếu nút rỗng thì chiều cao là 0
        if not root:
            return 0
        
        # Đệ quy tính chiều cao bên trái và bên phải
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Chiều cao của nút hiện tại = 1 + max(trái, phải)
        return 1 + max(left_depth, right_depth)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        # Nếu nhánh trái trống, phải đi tìm ở nhánh phải
        if not root.left:
            return self.minDepth(root.right) + 1

        # Nếu nhánh phải trống, phải đi tìm ở nhánh trái
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # Nếu có cả hai, lấy giá trị nhỏ nhất
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
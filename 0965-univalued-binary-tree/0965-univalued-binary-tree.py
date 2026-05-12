# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        # Nếu có con trái, nó phải bằng cha VÀ nhánh trái phải ổn
        if root.left and root.left.val != root.val:
            return False
        
        # Nếu có con phải, nó phải bằng cha VÀ nhánh phải phải ổn
        if root.right and root.right.val != root.val:
            return False
        
        # Đệ quy xuống dưới
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
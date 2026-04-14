# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []

        def helper(node):
            if not node:
                return

            helper(node.left) # di sang trai
            res.append(node.val) # ghi lai gia tri goc
            helper(node.right) # di sang phai

        helper(root)
        return res
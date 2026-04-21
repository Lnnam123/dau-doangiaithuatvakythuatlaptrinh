# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        res = []

        def dfs(node):
            if not node:
                return

            # tham goc
            res.append(node.val)
            # di sang trai
            dfs(node.left)
            # di sang phai
            dfs(node.right)
        
        dfs(root)
        return res

        
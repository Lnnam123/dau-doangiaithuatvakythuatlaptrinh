# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # 1. Nếu không tìm thấy (root là None) hoặc đã tìm thấy nút cần tìm
        if not root or root.val == val:
            return root
        
        # 2. Nếu giá trị cần tìm nhỏ hơn nút hiện tại -> Sang trái
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # 3. Nếu giá trị lớn hơn -> Sang phải
        return self.searchBST(root.right, val)
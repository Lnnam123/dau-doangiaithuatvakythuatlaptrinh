# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # Nếu cây trống, không bao giờ có tổng
        if not root:
            return False

        # Nếu là nút lá, kiểm tra xem giá trị nút có bằng target còn lại không
        if not root.left and not root.right:
            return root.val == targetSum

        # Tiếp tục tìm kiếm ở 2 nhánh với target đã trừ đi giá trị nút hiện tại
        new_target = targetSum - root.val
        return self.hasPathSum(root.left, new_target) or self.hasPathSum(root.right, new_target)
        
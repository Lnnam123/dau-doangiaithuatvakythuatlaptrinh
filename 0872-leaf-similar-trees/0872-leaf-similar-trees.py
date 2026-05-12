# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def get_leaves(node):
            leaves = []
            stack = [node]
            while stack:
                curr = stack.pop()
                # Nếu là nút lá (không có con trái và phải)
                if not curr.left and not curr.right:
                    leaves.append(curr.val)
                
                # Đẩy con phải vào trước để con trái được xử lý trước (LIFO)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
            return leaves
        
        # So sánh hai danh sách lá thu được
        return get_leaves(root1) == get_leaves(root2)
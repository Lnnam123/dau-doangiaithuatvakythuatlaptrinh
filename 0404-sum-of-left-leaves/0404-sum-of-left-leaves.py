# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        total = 0
        
        # Kiểm tra xem con bên TRÁI có phải là một nút LÁ không
        if root.left:
            if not root.left.left and not root.left.right:
                # Nếu đúng là lá bên trái, lấy giá trị của nó
                total += root.left.val
            else:
                # Nếu chưa phải là lá, đi sâu xuống tiếp nhánh trái
                total += self.sumOfLeftLeaves(root.left)
        
        # Luôn luôn phải đi xuống nhánh PHẢI để tìm các lá bên trái tiềm năng ở đó
        total += self.sumOfLeftLeaves(root.right)
        
        return total
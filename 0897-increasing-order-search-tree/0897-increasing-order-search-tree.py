# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Bước 1: Thu thập các nút theo thứ tự tăng dần
        nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
        # Bước 2: Nối các nút lại theo yêu cầu
        # Dùng một nút giả (dummy) để làm mốc bắt đầu
        dummy = TreeNode(0)
        curr = dummy
        
        for node in nodes:
            node.left = None    # Cây mới không được có nhánh trái
            curr.right = node   # Nối vào bên phải
            curr = node         # Di chuyển con trỏ tới nút vừa nối
            
        return dummy.right
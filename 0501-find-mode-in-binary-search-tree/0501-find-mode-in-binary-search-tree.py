# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.max_count = 0
        self.curr_count = 0
        self.curr_val = None
        self.modes = []

        def inorder(node):
            if not node:
                return

            # 1. Duyệt nhánh trái
            inorder(node.left)

            # 2. Xử lý nút hiện tại
            # Kiểm tra xem có trùng với số trước đó không
            if node.val == self.curr_val:
                self.curr_count += 1
            else:
                self.curr_val = node.val
                self.curr_count = 1
            
            # Cập nhật danh sách modes
            if self.curr_count > self.max_count:
                self.max_count = self.curr_count
                self.modes = [node.val] # Kỷ lục mới, bỏ hết cái cũ
            elif self.curr_count == self.max_count:
                self.modes.append(node.val) # Bằng kỷ lục, thêm vào danh sách

            # 3. Duyệt nhánh phải
            inorder(node.right)

        inorder(root)
        return self.modes
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Điều kiện dừng: Nếu mảng rỗng thì không có nút nào cả
        if not preorder or not inorder:
            return None

        # 1. Nút đầu tiên của preorder luôn là Root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 2. Tìm vị trí của root trong inorder để biết độ dài nhánh trái
        mid = inorder.index(root_val)

        # 3. Chia để trị:
        # Nhánh trái: 
        # - preorder: lấy từ phần tử thứ 1 đến mid+1
        # - inorder: lấy từ đầu đến mid
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # Nhánh phải:
        # - preorder: lấy từ mid+1 đến hết
        # - inorder: lấy từ sau mid đến hết
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
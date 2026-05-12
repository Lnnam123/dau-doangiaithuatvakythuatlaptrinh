# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, low, high):
            # Nếu nút rỗng, coi như hợp lệ
            if not node:
                return True
            
            # Giá trị nút hiện tại phải nằm trong khoảng (low, high)
            if not (low < node.val < high):
                return False
            
            # Đệ quy sang trái: giới hạn trên mới là node.val
            # Đệ quy sang phải: giới hạn dưới mới là node.val
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        # Bắt đầu với khoảng âm vô cực đến dương vô cực
        return validate(root, float('-inf'), float('inf'))
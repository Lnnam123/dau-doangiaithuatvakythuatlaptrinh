# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if not root:
            return []
        
        res = []
        # Stack lưu cặp: (nút_hiện_tại, chuỗi_đường_đi_tới_nút_đó)
        stack = [(root, str(root.val))]
        
        while stack:
            node, path = stack.pop()
            
            # Nếu là nút lá, thêm con đường hoàn chỉnh vào kết quả
            if not node.left and not node.right:
                res.append(path)
            
            # Đẩy con phải vào trước, con trái vào sau để duyệt trái trước (tùy chọn)
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
                
        return res    
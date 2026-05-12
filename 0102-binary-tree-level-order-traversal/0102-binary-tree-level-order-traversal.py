# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        queue = deque([root]) # Bắt đầu với nút gốc
        
        while queue:
            level_size = len(queue) # Số lượng nút thuộc tầng hiện tại
            current_level = []      # Danh sách chứa giá trị tầng này
            
            for _ in range(level_size):
                node = queue.popleft() # Lấy nút ở đầu hàng đợi
                current_level.append(node.val)
                
                # Đưa các con của nó vào hàng đợi cho tầng sau
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Kết thúc một tầng, cho vào kết quả tổng
            result.append(current_level)
            
        return result
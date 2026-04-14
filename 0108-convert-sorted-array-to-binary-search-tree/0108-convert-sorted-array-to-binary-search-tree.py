# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        
        # 1. Tìm chỉ số ở giữa
        mid = len(nums) // 2
        
        # 2. Tạo nút gốc từ phần tử ở giữa
        root = TreeNode(nums[mid])
        
        # 3. Đệ quy xây dựng cây con bên trái và bên phải
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
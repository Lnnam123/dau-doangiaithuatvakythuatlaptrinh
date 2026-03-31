# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Nếu danh sách rỗng hoặc chỉ có 1 node, chắc chắn không thể tạo thành vòng lặp
        if not head or not head.next:
            return False
            
        # Cả hai cùng xuất phát tại vạch đích
        rua = head
        tho = head
        
        # Lặp chừng nào Thỏ và bước tiếp theo của Thỏ chưa chạm đến ngõ cụt (None)
        while tho and tho.next:
            rua = rua.next           # Rùa tiến 1 bước
            tho = tho.next.next      # Thỏ tiến 2 bước
            
            # Nếu hai con trỏ trỏ về cùng một vùng nhớ (cùng một node)
            if rua == tho:
                return True          # Bắt quả tang có chu kỳ!
                
        # Thỏ đã chạy đến tận cùng danh sách mà không gặp Rùa
        return False
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Tao nut gia con tro
        dummy = ListNode(0)
        dummy.next = head

        # con tro duyet
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                # nảy qua nút cần xoá
                curr.next = curr.next.next
            else:
                # chỉ tiến lên nếu không cần xoá
                curr = curr.next
        return dummy.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head

        # Duyet khi nut hien tai va nut ke tiep deu ton tai
        while current and current.next:
            if current.val == current.next.val:
                #Bo qua nut trung lap
                current.next = current.next.next
            else:
                # Chi di chuyen neu khong co su trung lap
                current = current.next
        return head
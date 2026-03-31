# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        truoc = None
        hien_tai = head
        
        # Lap cho den khi xet het tat ca moi nguoi trong danh sach
        while hien_tai:
            # Buoc 1: Ghi nho lai nguoi dung sau de khong bi dut day
            tiep_theo = hien_tai.next
            
            # Buoc 2: Dao chieu mui ten, quay lai bat tay voi nguoi dung truoc
            hien_tai.next = truoc
            
            # Buoc 3: Chuan bi cho luot tiep theo bang cach di chuyen ca hai len mot buoc
            truoc = hien_tai
            hien_tai = tiep_theo
            
        # Khi 'hien_tai' chay ra khoi hang (thanh None), 
        # 'truoc' se dung dung o vi tri cua nguoi cuoi cung ban dau.
        # Nguoi nay bay gio se tro thanh nguoi dan dau moi cua danh sach!
        return truoc

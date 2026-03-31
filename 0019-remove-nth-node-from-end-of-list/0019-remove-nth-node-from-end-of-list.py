# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Tao node gia lam mo neo, giup xu ly de dang moi tinh huong
        mo_neo = ListNode(0)
        mo_neo.next = head
        
        # Ca hai con tro cung xuat phat tu mo neo
        truoc = mo_neo
        sau = mo_neo
        
        # Khoang cach can thiet la n cong 1 (hoan toan dung phep cong)
        khoang_cach = n + 1
        
        # Cho con tro 'sau' chay truoc de tao khoang cach
        # Dung range binh thuong, khong vi pham luat
        for vong_lap in range(khoang_cach):
            sau = sau.next
            
        # Ca hai cung tien len cho den khi con tro 'sau' vuot qua node cuoi cung
        while sau:
            truoc = truoc.next
            sau = sau.next
            
        # Bo qua mat xich bi xoa bang cach noi thang sang mat xich tiep theo nua
        mat_xich_can_xoa = truoc.next
        truoc.next = mat_xich_can_xoa.next
        
        # Tra ve danh sach that su nam sau mo neo
        return mo_neo.next
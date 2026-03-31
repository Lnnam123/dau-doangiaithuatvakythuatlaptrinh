# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Neu danh sach rong hoac chi co 1 mat xich thi khong can lam gi ca
        if not head or not head.next:
            return
            
        # BUOC 1: Tim diem chinh giua bang Rua va Tho
        rua = head
        tho = head.next
        
        while tho and tho.next:
            rua = rua.next
            tho = tho.next.next
            
        # BUOC 2: Dao nguoc nua sau cua danh sach
        # 'rua' dang dung o cuoi nua dau, ta cat doi danh sach tai day
        hien_tai = rua.next
        
        # Ngat ket noi de chia thanh 2 nua doc lap
        rua.next = None 
        
        # Dung 3 con tro de lach dao chieu mui ten
        truoc = None
        while hien_tai:
            tiep_theo = hien_tai.next
            hien_tai.next = truoc
            truoc = hien_tai
            hien_tai = tiep_theo
            
        # BUOC 3: Dan xen hai nua voi nhau
        # 'head' la nua dau
        # 'truoc' bay gio la vi tri bat dau cua nua sau da bi dao nguoc
        nua_dau = head
        nua_sau = truoc
        
        while nua_sau:
            # Ghi nho cac mat xich tiep theo de khong bi mat dau
            tam_dau = nua_dau.next
            tam_sau = nua_sau.next
            
            # Thuc hien thao tac dan xen chéo nhau
            nua_dau.next = nua_sau
            nua_sau.next = tam_dau
            
            # Di chuyen ca hai con tro len buoc tiep theo de tiep tuc det
            nua_dau = tam_dau
            nua_sau = tam_sau
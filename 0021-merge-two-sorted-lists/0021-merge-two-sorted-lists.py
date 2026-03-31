# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Tạo node giả làm mỏ neo để tránh các rắc rối với node đầu tiên
        head = ListNode(0)
        
        # Con trỏ tail làm nhiệm vụ đi dệt các mắt xích lại với nhau
        tail = head
        
        # Lặp chừng nào cả hai danh sách ĐỀU CÒN mắt xích
        while list1 and list2:
            
            # So sánh hai giá trị hiện tại
            if list1.val <= list2.val:
                # Nối mắt xích của list1 vào đuôi kết quả
                tail.next = list1
                # list1 tiến lên bước tiếp theo
                list1 = list1.next
            else:
                # Nối mắt xích của list2 vào đuôi kết quả
                tail.next = list2
                # list2 tiến lên bước tiếp theo
                list2 = list2.next
                
            # tail tiến lên để chuẩn bị đón mắt xích mới
            tail = tail.next
            
        # Nối nốt phần đuôi của danh sách nào vẫn còn dư
        # (Chỉ một trong hai dòng if dưới đây thực sự nối thêm dữ liệu)
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        # Trả về danh sách thật nằm ngay sau mỏ neo
        return head.next
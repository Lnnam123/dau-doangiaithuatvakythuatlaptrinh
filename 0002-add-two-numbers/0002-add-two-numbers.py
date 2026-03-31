# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Tạo một node giả (dummy node) làm mỏ neo. 
        # Việc này giúp ta không phải viết thêm logic phức tạp để xử lý riêng node đầu tiên.
        head = ListNode(0) 
        
        # Con trỏ 'tail' sẽ đóng vai trò người thợ xây, bắt đầu từ mỏ neo 
        # và liên tục nối thêm các node mới vào đuôi danh sách kết quả.
        tail = head 
        
        # Biến 'carry' dùng để lưu giá trị nhớ mang sang hàng tiếp theo (ví dụ 8+7=15 thì nhớ 1)
        carry = 0 

        # Lặp chừng nào một trong hai danh sách vẫn còn số, 
        # HOẶC vẫn còn số dư (carry) từ phép tính trước chưa được cộng vào.
        while l1 or l2 or carry:
            # Lấy giá trị hiện tại của l1. Nếu l1 đã cạn (None) thì mặc định là 0.
            x = l1.val if l1 else 0
            
            # Lấy giá trị hiện tại của l2. Nếu l2 đã cạn (None) thì mặc định là 0.
            y = l2.val if l2 else 0

            # Tính tổng 2 chữ số hiện tại và cộng thêm phần nhớ từ hàng trước
            sum = x + y + carry
            
            # Tính toán phần nhớ mới cho bước tiếp theo (chia lấy phần nguyên)
            # Ví dụ: sum = 18 -> carry = 1
            carry = sum // 10
            
            # Lấy chữ số hàng đơn vị của tổng (chia lấy phần dư) để nhét vào node mới.
            # Sau đó nối thẳng node mới này vào đuôi danh sách kết quả.
            tail.next = ListNode(sum % 10)
            
            # Dịch chuyển người thợ xây 'tail' tiến lên node vừa xây xong
            tail = tail.next

            # Nếu l1 vẫn còn mắt xích, cho l1 tiến lên một bước
            if l1:
                l1 = l1.next
                
            # Nếu l2 vẫn còn mắt xích, cho l2 tiến lên một bước
            if l2:
                l2 = l2.next

        # Cuối cùng, trả về danh sách thực sự bắt đầu từ sau node mỏ neo
        return head.next
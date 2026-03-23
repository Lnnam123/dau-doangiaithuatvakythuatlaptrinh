class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Nếu mảng rỗng, không có gì để xử lý
        if not nums:
            return 0
            
        # Vị trí đầu tiên (index 0) luôn luôn là số độc nhất đầu tiên.
        # Nên "người ghi chép" (slow) sẽ bắt đầu làm việc từ vị trí số 1.
        slow = 1
        
        # "Người trinh sát" (fast) cũng bắt đầu đi từ vị trí số 1 để so sánh với số ở vị trí 0
        for fast in range(1, len(nums)):
            
            # Nếu trinh sát phát hiện con số hiện tại KHÁC với con số ngay sau lưng nó
            # -> Đây là một con số mới hoàn toàn!
            if nums[fast] != nums[fast - 1]:
                
                # Người ghi chép chép số mới này vào vị trí đang đứng
                nums[slow] = nums[fast]
                
                # Người ghi chép nhích sang ô tiếp theo để chuẩn bị cho lần ghi tới
                slow += 1
                
        # Giá trị của biến 'slow' lúc này cũng chính là TỔNG SỐ LƯỢNG các số không trùng lặp
        return slow
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0   # Con trỏ đánh dấu điểm bắt đầu của chuỗi số 1
        right = 0  # Con trỏ dùng để duyệt qua từng phần tử
        ans = 0    # Biến lưu kết quả độ dài lớn nhất tìm được
        n = len(nums)

        # Bắt đầu vòng lặp duyệt từ đầu đến cuối mảng
        while right < n:
            # TRƯỜNG HỢP 1: Gặp số 0 -> Chuỗi số 1 bị đứt đoạn
            if nums[right] == 0:
                # Tính độ dài chuỗi vừa kết thúc (right - left) 
                # và so sánh với kỷ lục cũ (ans) để lấy số lớn hơn
                ans = max(ans, right - left)
                
                # Vòng lặp nhỏ này để nhảy qua tất cả các số 0 liên tiếp (nếu có)
                # Ví dụ: ...1, 1, 0, 0, 0, 1... -> right sẽ chạy qua 3 số 0
                while right < n and nums[right] == 0:
                    right += 1
                
                # Sau khi qua hết số 0, đặt lại mốc 'left' bằng 'right' 
                # để bắt đầu tính cho chuỗi số 1 mới
                left = right
            
            # TRƯỜNG HỢP 2: Gặp số 1 -> Tiếp tục mở rộng chuỗi
            else:
                right += 1
        
        # QUAN TRỌNG: Sau khi thoát vòng lặp, cần kiểm tra lần cuối.
        # Lý do: Nếu mảng kết thúc bằng số 1 (vd: [0, 1, 1]), vòng lặp while chính 
        # sẽ dừng mà chưa kịp tính toán 'ans' cho chuỗi cuối cùng này.
        return max(ans, right - left)
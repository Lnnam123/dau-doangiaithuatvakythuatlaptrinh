class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_alt = 0      # Lưu độ cao lớn nhất tìm được (kết quả)
        current_alt = 0  # Lưu độ cao hiện tại của người đạp xe
        
        for g in gain:
            # Cộng dồn độ chênh lệch vào độ cao hiện tại
            current_alt += g
            
            # Cập nhật độ cao lớn nhất nếu độ cao hiện tại cao hơn
            if current_alt > max_alt:
                max_alt = current_alt
                
        return max_alt
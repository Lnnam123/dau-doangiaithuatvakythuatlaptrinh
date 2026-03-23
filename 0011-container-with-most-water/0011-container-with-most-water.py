class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        trai = 0
        phai = len(height) - 1
        dien_tich_max = 0
        
        # Hai con trỏ tiến lại gần nhau cho đến khi chạm mặt
        while trai < phai:
            # Chiều rộng là khoảng cách giữa 2 vị trí (index)
            chieu_rong = phai - trai
            
            # Chiều cao tính theo thanh ngắn hơn
            chieu_cao = min(height[trai], height[phai])
            
            # Tính diện tích hiện tại và so sánh để cập nhật kỷ lục
            dien_tich_hien_tai = chieu_rong * chieu_cao
            if dien_tich_hien_tai > dien_tich_max:
                dien_tich_max = dien_tich_hien_tai
            
            # Vách nào thấp hơn thì nhích con trỏ ở vách đó vào trong để thử vận may
            if height[trai] < height[phai]:
                trai += 1
            else:
                phai -= 1
                
        return dien_tich_max
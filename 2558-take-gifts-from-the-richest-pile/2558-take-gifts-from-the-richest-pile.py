class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        # Lặp lại đúng k lần
        for _ in range(k):
            # Tìm đống quà to nhất trong mảng hiện tại
            dong_to_nhat = max(gifts)
            
            # Tìm xem đống quà đó nằm ở vị trí thứ mấy
            vi_tri = gifts.index(dong_to_nhat)
            
            # Cập nhật lại vị trí đó bằng căn bậc hai (dùng int() để làm tròn xuống)
            gifts[vi_tri] = int(dong_to_nhat ** 0.5)
            
        # Cuối cùng, trả về tổng số quà còn lại
        return sum(gifts)
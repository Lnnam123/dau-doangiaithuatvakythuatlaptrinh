class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # BƯỚC 1: Sắp xếp cân nặng từ nhẹ đến nặng
        people.sort()
        
        trai = 0
        phai = len(people) - 1
        so_thuyen = 0
        
        # BƯỚC 2: Dùng 2 con trỏ ghép cặp từ 2 đầu
        # Lưu ý dùng <= vì khi 2 con trỏ chập vào làm 1 (chỉ còn 1 người cuối cùng), 
        # người đó vẫn cần được cấp 1 chiếc thuyền.
        while trai <= phai: 
            
            # Thử ghép cặp người nhẹ nhất (trái) và nặng nhất (phải) hiện tại
            if people[trai] + people[phai] <= limit:
                # Ghép thành công! Người nhẹ bước lên thuyền.
                trai += 1 
                
            # Dù ghép cặp thành công hay thất bại, người nặng nhất (phải) 
            # chắc chắn phải bước lên chiếc thuyền này.
            phai -= 1
            
            # Đếm thêm 1 chiếc thuyền vừa rời bến
            so_thuyen += 1
            
        return so_thuyen
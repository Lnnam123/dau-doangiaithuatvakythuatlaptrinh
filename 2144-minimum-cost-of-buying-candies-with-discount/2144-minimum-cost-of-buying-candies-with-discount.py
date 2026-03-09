class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Bước 1: Sắp xếp giá kẹo giảm dần
        cost.sort(reverse=True)
        
        total_cost = 0
        n = len(cost)
        
        # Bước 2: Duyệt qua danh sách kẹo
        for i in range(n):
            # Cứ mỗi viên thứ 3 (chỉ số 2, 5, 8...) thì bỏ qua không tính tiền
            # Chỉ số i bắt đầu từ 0, nên viên thứ 3 có (i + 1) chia hết cho 3
            if (i + 1) % 3 == 0:
                continue
            
            total_cost += cost[i]
            
        return total_cost
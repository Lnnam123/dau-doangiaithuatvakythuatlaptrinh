class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0  # Số lượng tờ 5$ đang có
        ten = 0   # Số lượng tờ 10$ đang có

        for bill in bills:
            if bill == 5:
                # Khách đưa 5$, không cần thối, nhận thêm 1 tờ 5$
                five += 1
            
            elif bill == 10:
                # Khách đưa 10$, phải thối lại 1 tờ 5$
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            
            else: # Khách đưa 20$, phải thối 15$
                # Ưu tiên cách 1: Thối 1 tờ 10$ và 1 tờ 5$ (Chiến thuật tham lam)
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                # Nếu không có tờ 10$, dùng cách 2: Thối 3 tờ 5$
                elif five >= 3:
                    five -= 3
                # Nếu không đủ tiền thối
                else:
                    return False
                    
        return True
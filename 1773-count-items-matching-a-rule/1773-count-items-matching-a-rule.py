class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        # Bước 1: Xác định chỉ số cột dựa trên ruleKey
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else: # ruleKey == "name"
            index = 2
            
        count = 0
        
        # Bước 2: Duyệt qua từng item và kiểm tra điều kiện
        for item in items:
            if item[index] == ruleValue:
                count += 1
                
        return count
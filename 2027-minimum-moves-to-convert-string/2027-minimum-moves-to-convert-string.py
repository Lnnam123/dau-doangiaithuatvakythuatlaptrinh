class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        moves = 0
        i = 0
        n = len(s)
        
        while i < n:
            # Nếu gặp 'X', bắt buộc phải tốn 1 nước đi
            if s[i] == 'X':
                moves += 1
                # Nước đi này bao phủ 3 ô liên tiếp (i, i+1, i+2)
                # Vậy nên ta nhảy thẳng tới ô i + 3
                i += 3
            else:
                # Nếu là 'O', chỉ cần sang ô kế tiếp
                i += 1
                
        return moves
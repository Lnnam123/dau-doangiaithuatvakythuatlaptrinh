class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        h = dict()

        for i in magazine:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        
        for i in ransomNote:
            if i not in h or h[i] == 0:
                return False
            h[i] -= 1
        
        return True
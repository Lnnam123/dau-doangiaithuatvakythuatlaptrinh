class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        string = s.strip()
        i = len(string) - 1
        while i >= 0:
            if string[i] == " ":
                return count
            else:
                count += 1
                i -= 1
        return count

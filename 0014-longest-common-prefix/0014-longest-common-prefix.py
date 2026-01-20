class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str=strs[0]
        len_str=len(str)
        for i in strs[1:]:
            while str != i[0:len_str]:
                len_str -= 1
                if len_str == 0:
                    return ""
                str = str[0:len_str]
        return str




class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str=strs[0]
        len_str=len(str)
        for i in strs[1:]: #vòng lặp tiền tố hiện tại (str) với từng chuỗi i
        # bắt đầu từ chuỗi 2
            while str != i[0:len_str]: #lấy prefix (tiền tố) độ dài len_str cua chuoi i
                len_str -= 1 #giảm độ dài prefix đi 1 ký tự
                if len_str == 0:
                    return ""
                str = str[0:len_str] #cập nhật tiền tố mới
        return str




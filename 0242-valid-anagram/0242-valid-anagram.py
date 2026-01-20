class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return sorted(s)==sorted(t) #ham dung de sap xep cac phan tu va tra ve mot danh sach (list) moi

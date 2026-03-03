class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        dict1 = {}
        for w in words1:
            dict1[w] = dict1.get(w, 0) + 1
        
        dict2 = {}
        for w in words2:
            dict2[w] = dict2.get(w, 0) + 1
        
        count = 0
        for w in dict1:
            if dict1[w] == 1 and dict2.get(w, 0) == 1:
                count += 1
        return count
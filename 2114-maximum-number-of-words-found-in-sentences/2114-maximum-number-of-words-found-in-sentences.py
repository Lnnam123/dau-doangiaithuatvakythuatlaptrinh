class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words = 0
        
        for sentence in sentences:
            # Tách câu thành danh sách các từ
            words = sentence.split()
            # Lấy số lượng từ
            count = len(words)
            
            # Cập nhật số lượng lớn nhất
            if count > max_words:
                max_words = count
                
        return max_words
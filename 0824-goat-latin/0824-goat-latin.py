class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        words = sentence.split()
        result = []

        for i in range(len(words)):
            word = words[i]

            # Nếu bắt đầu bằng nguyên âm
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                # Nếu bắt đầu bằng phụ âm
                new_word = word[1:] + word[0] + "ma"

            # Thêm 'a' theo vị trí (i bắt đầu từ 0 nên +1)
            new_word += "a" * (i + 1)

            result.append(new_word)

        return " ".join(result)

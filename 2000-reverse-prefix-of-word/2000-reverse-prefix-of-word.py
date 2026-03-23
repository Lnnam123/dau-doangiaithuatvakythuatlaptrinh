class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        # Tìm vị trí (index) xuất hiện đầu tiên của ký tự ch
        vi_tri = word.find(ch)
        
        # Hàm find() sẽ tự động trả về -1 nếu không tìm thấy ký tự đó
        if vi_tri == -1:
            return word
            
        # BƯỚC CẮT VÀ GHÉP CHUỖI:
        # word[:vi_tri + 1] -> Cắt lấy phần tiền tố (từ đầu đến vị trí tìm thấy)
        # [::-1] -> Lật ngược phần tiền tố vừa cắt
        phan_dao_nguoc = word[:vi_tri + 1][::-1]
        
        # word[vi_tri + 1:] -> Cắt lấy phần đuôi còn lại (từ sau vị trí đó đến hết chữ)
        phan_con_lai = word[vi_tri + 1:]
        
        # Ghép lại làm một
        return phan_dao_nguoc + phan_con_lai
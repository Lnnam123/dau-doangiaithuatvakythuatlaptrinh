class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        ngan_xep = [] # Ống chứa chữ cái
        
        # Duyệt qua từng chữ cái trong chuỗi ban đầu
        for chu_cai in s:
            
            # Kiểm tra triệt tiêu
            # Nếu ống có đồ và chữ đang cầm giống chữ trên cùng của ống (ngan_xep[-1])
            if ngan_xep and ngan_xep[-1] == chu_cai:
                ngan_xep.pop() # lấy chữ trên cùng (lấy ra khỏi ống)
                
            else:
                # Nếu khác, hoặc ống đang rỗng, thì thả chữ này vào ống
                ngan_xep.append(chu_cai)
                
        # Sau khi duyệt hết, các chữ cái còn sót lại trong ống chính là kết quả.
        # Dùng hàm join() để ghép các ký tự rời rạc trong list thành 1 chuỗi hoàn chỉnh
        return "".join(ngan_xep)
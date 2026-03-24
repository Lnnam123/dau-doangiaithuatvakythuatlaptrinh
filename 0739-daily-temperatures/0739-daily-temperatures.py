class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        # Khởi tạo mảng kết quả với toàn số 0. 
        # Những ngày không tìm thấy ngày nóng hơn sẽ tự động giữ nguyên là 0.
        ket_qua = [0] * n 
        
        # Ngăn xếp này chỉ lưu VỊ TRÍ (index) của các ngày đang chờ thời tiết nóng lên
        ngan_xep = [] 
        
        # Dùng enumerate để lấy cả vị trí 'i' (ngày thứ mấy) và 'nhiet_do_hien_tai'
        for i, nhiet_do_hien_tai in enumerate(temperatures):
            
            # Nếu ống có người VÀ nhiệt độ hôm nay NÓNG HƠN ngày nằm trên cùng của ống
            while ngan_xep and nhiet_do_hien_tai > temperatures[ngan_xep[-1]]:
                # Lấy ngày lạnh đó ra khỏi ống
                ngay_truoc = ngan_xep.pop() 
                
                # Tính khoảng cách thời gian và ghi vào mảng kết quả
                khoang_cach = i - ngay_truoc
                ket_qua[ngay_truoc] = khoang_cach
                
            # Dù có vừa giải quyết xong ai hay không, ngày hôm nay cũng phải 
            # chui vào ống để chờ một ngày trong tương lai nóng hơn nó.
            ngan_xep.append(i)
            
        return ket_qua
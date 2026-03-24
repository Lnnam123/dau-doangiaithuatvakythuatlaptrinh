class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        trai = 0
        # Đặt thẳng phai bằng độ dài mảng, bỏ qua phép trừ
        phai = len(arr)
        
        while trai < phai:
            giua = (trai + phai) // 2
            
            # KIỂM TRA TRÀN MẢNG
            # Nếu vị trí đối diện nằm tít ngoài mảng -> Ta đang ở quá xa về bên phải
            if giua + k >= len(arr):
                phai = giua # Ép giới hạn phải lùi lại
                
            else:
                # Nếu cửa sổ nằm gọn trong mảng, ta so sánh bình thường
                vi_tri_doi_dien = giua + k
                
                # Công thức so sánh khoảng cách "x * 2 <= a + b" (không dùng dấu trừ)
                if x * 2 <= arr[giua] + arr[vi_tri_doi_dien]:
                    # x gần đầu cửa sổ hơn -> Nửa phải không tốt, thu hẹp về bên trái
                    phai = giua
                else:
                    # x gần cuối cửa sổ hơn -> Nửa trái không tốt, nhích sang bên phải
                    trai = giua + 1
                    
        # Trả về đúng k phần tử, bắt đầu từ vị trí trai
        # Cú pháp cắt mảng [a : a + b] hoàn toàn chỉ dùng phép cộng!
        return arr[trai : trai + k]
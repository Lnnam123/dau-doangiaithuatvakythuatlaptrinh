class Solution:
    def duplicateZeros(self, arr):
        i = 0
        n = len(arr)  # Lưu lại độ dài cố định của mảng ban đầu
        
        # Duyệt qua mảng. Điều kiện i < n đảm bảo không duyệt quá độ dài cho phép
        while i < n:
            # Nếu gặp số 0
            if arr[i] == 0:
                # 1. Xóa phần tử cuối cùng của mảng đi
                # Việc này để giữ độ dài mảng không đổi sau khi chèn
                arr.pop()
                
                # 2. Chèn số 0 vào vị trí hiện tại (i)
                # Các phần tử phía sau (bao gồm số 0 gốc) sẽ bị đẩy lùi về sau 1 bước
                arr.insert(i, 0)
                
                # 3. Tăng i thêm 1 lần nữa (bước nhảy cóc)
                # Lý do: Sau khi chèn, tại vị trí i là số 0 mới, tại i+1 là số 0 gốc.
                # Ta cần bỏ qua vị trí i+1 để không xét lại số 0 gốc đó nữa.
                i += 1
            
            # Tăng i để tiếp tục duyệt phần tử tiếp theo
            i += 1
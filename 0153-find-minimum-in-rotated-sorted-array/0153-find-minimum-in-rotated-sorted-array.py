class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        trai = 0
        phai = len(nums) - 1
        
        # Lưu ý: Điều kiện là trai < phai (không có dấu bằng)
        # Vì khi trai và phai chập vào nhau, đó chính là con số nhỏ nhất cần tìm.
        while trai < phai:
            giua = (trai + phai) // 2
            
            # So sánh số ở giữa với số ở cuối cùng của vùng tìm kiếm
            if nums[giua] > nums[phai]:
                # Chắc chắn số nhỏ nhất nằm ở nửa phải
                trai = giua + 1
            else:
                # Số nhỏ nhất nằm ở nửa trái (hoặc chính là vị trí 'giua')
                phai = giua
                
        # Khi vòng lặp kết thúc (trai == phai), ta đã ép 2 con trỏ vào đúng số nhỏ nhất
        return nums[trai]
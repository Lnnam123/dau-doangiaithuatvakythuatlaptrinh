class MinStack(object):

    def __init__(self):
        # Khởi tạo một mảng rỗng để làm ngăn xếp
        # Mỗi phần tử trong này sẽ là một tuple: (giá_trị_thực, giá_trị_min_hiện_tại)
        self.ngan_xep = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.ngan_xep:
            # Nếu ống rỗng, số nhỏ nhất (min) chính là 'val'
            self.ngan_xep.append((val, val))
        else:
            # Nếu ống đã có đồ, lấy số min cũ ở trên cùng ra so sánh
            min_cu = self.ngan_xep[-1][1]
            min_moi = min(val, min_cu)
            
            # Gói cả giá trị thực và min mới lại rồi nhét vào ống
            self.ngan_xep.append((val, min_moi))

    def pop(self):
        """
        :rtype: None
        """
        # Lấy phần tử trên cùng ra khỏi ống (vứt bỏ cả cặp)
        self.ngan_xep.pop()

    def top(self):
        """
        :rtype: int
        """
        # Trả về giá trị thực (nằm ở vị trí đầu tiên [0] của tuple)
        return self.ngan_xep[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        # Trả về số nhỏ nhất (nằm ở vị trí thứ hai [1] của tuple)
        return self.ngan_xep[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
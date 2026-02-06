class Solution(object):
    def fizzBuzz(self, n):
        # 1. Khởi tạo một danh sách rỗng để chứa kết quả
        result = []
        
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz") # 3. Dùng append để thêm vào list 
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
                
        # 4. Trả về toàn bộ danh sách sau khi vòng lặp kết thúc
        return result
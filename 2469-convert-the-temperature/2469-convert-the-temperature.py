class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        # Tính toán theo công thức
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        
        # Trả về kết quả dưới dạng mảng
        return [kelvin, fahrenheit]
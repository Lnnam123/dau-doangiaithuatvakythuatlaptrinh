class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        planted = 0
        for i in range (0, len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0): 
            #ĐK1: Ô hiện tại trống
            #ĐK2: Ô bên trái trống hoặc đang ở đầu mảng
            #ĐK3: Ô bên phải trống hoặc đang ở cuối mảng
                planted += 1
                flowerbed[i] = 1
        return planted >= n
from ast import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        l = len(flowerbed)
        if l == 1:
            if flowerbed[0] == 1:
                count = 0
            else: count += 1
        else:
            if flowerbed[1] == 0 and flowerbed[0] == 0:
                flowerbed[0] = 1
                count += 1

            for i in range(1, len(flowerbed)-2):
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    count += 1
            if flowerbed[l-2] == 0 and flowerbed[l-1] == 0:
                flowerbed[l-1] = 1
                count += 1
            
        if n <= count:
            return True
        else:
            return False
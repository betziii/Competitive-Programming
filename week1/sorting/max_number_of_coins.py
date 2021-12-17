class Solution:
    def maxCoins(self, piles: List[int]) -> int:
#         ls = []
#         sum = 0
#         i = 0
#         if len(piles)%3 == 0:
#             print(piles.sort())
#             while i<=len(piles)+1:
#                 print(piles)
#                 # print(x)
                
#                 piles.remove(max(piles, default=0))
#                 # print(piles)
#                 ls.append(max(piles, default=0))
#                 piles.remove(max(piles, default=0))
#                 piles.remove(min(piles, default=0))
#                 i-=1
#                 print(piles)
#             print(ls)
#             for i in ls:
#                 sum +=i
#         return sum
        n = len(piles)//3
        piles.sort()
        sums = 0
        for i in range(n, len(piles), 2):
            sums += piles[i]    

        return sums
            
            
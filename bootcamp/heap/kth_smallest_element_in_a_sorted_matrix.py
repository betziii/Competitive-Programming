import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range (len(matrix)):
            for j in range (len(matrix)):
                heapq.heappush(heap, matrix[i][j])
        small = heapq.nsmallest(k, heap)
        return small[len(small)-1]
        
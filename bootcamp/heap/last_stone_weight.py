import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for i in stones:
            heapq.heappush(heap, -i )
        if len(stones) == 1:
            return stones[0]
        while len(heap) > 1:
            a = -(heapq.heappop(heap)) 
            b = -(heapq.heappop(heap))

            if a > b:
                x = a - b
                heapq.heappush(heap,-x)
            elif a == b:
                x = a - b
                heapq.heappush(heap,x)
                
            
        if len(heap) == 1:
            if heap[0] <0:
                return -(heap[0])
            return heap[0]
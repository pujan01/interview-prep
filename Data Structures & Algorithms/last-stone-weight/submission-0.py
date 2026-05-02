import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for x in stones:
            heapq.heappush(heap, -x)

        while len(heap) > 1:
            h1, h2 = heapq.heappop(heap), heapq.heappop(heap)
            heapq.heappush(heap, h1 - h2)
        return abs(heap[0])

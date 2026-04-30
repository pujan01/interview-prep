"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minRooms = 0 
        intervals.sort(key = lambda x: x.start)
        # [(0,40),(5,10),(15,20), (18,30), (30,50), (40,50), (41,44)]
        # room1: 0, 40, 40, 50 
        # room2: 5, 10, 15, 20, 44 
        # room3: 18, 30, 30, 50, 
        #  if smaller value than x.start exists, then pop it and add the x.end to the heap
        # else just add x.end to the heap 
        heap = []
        rooms = 0
        for x in intervals:
            if heap and heap[0] <= x.start: 
                heapq.heappop(heap)
                rooms -= 1
            heapq.heappush(heap, x.end)
            rooms += 1
            minRooms = max(minRooms, rooms)
        return minRooms
        
        

        

        





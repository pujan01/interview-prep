"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        if intervals:
            prevFin = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < prevFin:
                return False
            prevFin = intervals[i].end
        return True
            


            

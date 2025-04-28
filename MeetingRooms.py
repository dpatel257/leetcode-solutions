"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        size = len(intervals)
        
        intervals.sort(key = lambda i:i.start)

        for i in range(1, size):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True


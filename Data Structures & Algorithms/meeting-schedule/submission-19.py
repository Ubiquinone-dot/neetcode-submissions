"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(intervals)):
            prev, cur = intervals[i-1], intervals[i]
            if prev.end > cur.start:
                return False
        return True

        # n = len(intervals)
        # for i in range(n):
        #     s1, e1 = intervals[i].start, intervals[i].end

        #     for j in range(i+1, n):
        #         s, e = intervals[j].start, intervals[j].end
        #         if s1 >= s:
        #             if e > s1:
        #                 return False
        #         elif s1 < s:
        #             if e1 > s:
        #                 return False

        # return True

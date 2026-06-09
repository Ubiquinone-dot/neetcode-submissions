"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        for i in range(n):
            s1, e1 = intervals[i].start, intervals[i].end

            for j in range(i+1, n):
                s, e = intervals[j].start, intervals[j].end
                print(s1, e1, '\t', s, e)
                if s1 >= s:
                    if e > s1:
                        print('1')
                        return False
                elif s1 < s:
                    if e1 > s:
                        print('2')
                        return False

        return True

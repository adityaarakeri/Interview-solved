"""
57. Insert Interval
-------------------
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        idx = -1
        
        for idx, (x,y) in enumerate(intervals):
            if y < newInterval[0]:
                ans.append([x,y])
            elif newInterval[1] < x:
                idx-=1
                break
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)
        
        return ans + [newInterval] + intervals[idx+1:]
        
"""
Runtime: 56 ms, faster than 96.90% of Python online submissions for Insert Interval.
Memory Usage: 16.2 MB, less than 31.60% of Python online submissions for Insert Interval.
"""
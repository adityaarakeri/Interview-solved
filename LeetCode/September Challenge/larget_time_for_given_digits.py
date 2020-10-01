"""
949. Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:
Input: [1,2,3,4]
Output: "23:41"
"""
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        max_time = -1
        for h, i, j, k in itertools.permutations(A):
            hour = h*10 + i
            minute = j*10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)

        
"""
Runtime: 24 ms, faster than 79.77% of Python online submissions for Largest Time for Given Digits.
Memory Usage: 12.8 MB, less than 42.75% of Python online submissions for Largest Time for Given Digits.
"""
"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        lastIndex = {}
        for idx, char in enumerate(S):
            lastIndex[char] = idx
        start = end = 0
        
        for idx, char in enumerate(S):
            end = max(end, lastIndex[char])
            if idx == end:
                ans.append(idx - start + 1)
                start = idx + 1
                
        return ans                
    
"""
Runtime: 20 ms, faster than 98.32% of Python online submissions for Partition Labels.
Memory Usage: 12.7 MB, less than 83.64% of Python online submissions for Partition Labels.
"""
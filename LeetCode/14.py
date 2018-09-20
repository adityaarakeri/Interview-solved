"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        if len(strs) == 0:
            return ''
        i = 0
        d = {i: len(v) for i,v in enumerate(strs)}
        count = min(d.values())
        
        for i in range(1, count+1):
            prefix = strs[0][:i]
            for s in strs:
                if s[:i] != prefix:
                    return result
            
            result = prefix
        
        return result


    def optimized(self, strs):
        result = ""
        for n in zip(*strs):
            if (len(set(n))) == 1:
                result = result + n[0]
            else:
                return result

        return result

s = Solution()
# print(s.longestCommonPrefix(raw_input().split()))
print(s.optimized(raw_input().split()))

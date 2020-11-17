"""
459. Repeated Substring Pattern
-------------------------------
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
"""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        n = len(s)

        if n < 1:
            return False
        temp = ''

        idx = 0
        while idx <= (n//2) and idx != (n-1):
            temp+=s[idx]
            if n % (idx+1) == 0 and temp * (n/(idx+1)) == s:
                    return True
            idx+=1
            
        return False

"""
-> Runtime: 108 ms, faster than 53.80% of Python online submissions for Repeated Substring Pattern.
-> Memory Usage: 12.9 MB, less than 91.17% of Python online submissions for Repeated Substring Pattern.
"""
"""
Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type x: int
        :rtype: bool
        """
        result = ""
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                x = s[i:j]
                if x == x[::-1]:
                    if len(x) > len(result):
                        result = x
        return result


S = Solution()
print(S.isPalindrome("babad"))
print(S.isPalindrome("cbbd"))

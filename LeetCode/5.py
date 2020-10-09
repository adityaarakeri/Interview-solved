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
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if len(str(x)) % 2 == 0:
            return int(str(x)[:len(str(x))//2]) == int(str(x)[len(str(x))//2:][::-1])
        else:
            return int(str(x)[:len(str(x))//2+1]) == int(str(x)[len(str(x))//2:][::-1])


a = Solution().isPalindrome(+2147447412)
print(a)

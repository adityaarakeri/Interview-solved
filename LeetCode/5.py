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
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = len(s)
        if last <= 1:
            return s
        
        res = ""
        for i in range(last):
            # odd number of characters, like "aba"
            cur = self.helper(s, i, i)
            if len(cur) > len(res):
                res = cur
            # even number of characters, like "abba"
            cur = self.helper(s, i, i+1)
            if len(cur) > len(res):
                res = cur
        return res
 
# get the longest palindrome
# l and r are the middle indexes   
# from inner to outer for the current i
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
        

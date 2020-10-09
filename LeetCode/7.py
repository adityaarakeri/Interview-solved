"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""


class Solution(object):
    def matchChar(self, sc, pc):
        return sc == pc or pc == '.'

    def isEndOfStar(self, p):
        while p != '':
            if len(p) == 1 or len(p) > 1 and p[1] != '*':
                return False
            p = p[2:]
        return True

    def isMatch(self, s, p):
        if p == '':
            return s == ''

        if s == '':
            return self.isEndOfStar(p)

        if (len(p) > 1 and p[1] != '*') or len(p) == 1:
            # without *
            if not self.matchChar(s[0], p[0]):
                return False
            else:
                return self.isMatch(s[1:], p[1:])

        else:
            # with *
            # try see x* is empty
            if self.isMatch(s[0:], p[2:]):
                return True

            while self.matchChar(s[0], p[0]):
                s = s[1:]

                if self.isMatch(s, p[2:]):
                    return True

                if s == '':
                    return self.isEndOfStar(p)
            return False

#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = '1'
        for _ in range(n - 1):
            count = 1
            result = ''
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    result += str(count) + s[i-1]
                    count = 1
            result += str(count) + s[-1]
            s = result

        return s

    def count_and_say_improved(self, n):
        if n == 1:
            return '1'
        # counter = 0
        s = '1'  # Start know one == '1'
        result = []
        for _ in range(n - 1):
            counter, current_val = 0, s[0]
            for v in s:
                if v == current_val:
                    counter += 1
                else:
                    result.append(str(counter))
                    result.append(current_val)
                    current_val = v
                    counter = 1
            result.append(str(counter))
            result.append(current_val)
            s = "".join(result)
            result = []
        return s


s = Solution()
a = 4
print(s.countAndSay(a))
print(s.count_and_say_improved(a))

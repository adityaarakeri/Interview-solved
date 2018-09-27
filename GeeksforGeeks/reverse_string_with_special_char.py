#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Reverse an array without affecting special characters
Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that special characters are not affected.

Examples:

Input:   str = "a,b$c"
Output:  str = "c,b$a"
Note that $ and , are not moved anywhere.  
Only subsequence "abc" is reversed

Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"

"""

def reverse(s):
    # convert string to array
    s = list(s)
    # left index
    l = 0
    # right index
    r = len(s) - 1

    while l < r:
        if not isAlphabet(s[l]):
            l += 1
        elif not isAlphabet(s[r]):
            r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    
    return ''.join(s)

# helper func
def isAlphabet(x):
    return x.isalpha()

# A = 'abc,$d'
# print(reverse(A))

import unittest

class Test(unittest.TestCase):
    def test_assert_true(self):
        self.assertEqual("i!!!h.g.f,e'd,cba", reverse("a!!!b.c.d,e'f,ghi") )

if __name__ == '__main__':
    unittest.main()	
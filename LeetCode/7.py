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
class Solution:
    def reverse(self, x: int) -> int:
        x=int(x)
        if(x>=0):
            x=str(x)
            x=x[::-1]
            x=int(x)
            if(x<-1*(2**31))or(x>=2**31):
                return 0
            else:
                return x
        else:
            x=x*(-1)
            x=str(x)
            x=x[::-1]
            x=int(x)
            x=-1*x
            if(x<-1*(2147483648))or(x>=2147483648):
                return 0
            else:
                return x
print(Solution.reverse(int(input()))

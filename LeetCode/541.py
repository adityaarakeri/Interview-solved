"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Ex:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) == 1:
            return s
        if len(s) == k:
            return s[::-1]
        if len(s) == k + 1:
            return s[::-1]+s[-1]
        else:
            i = 0
            result = ''
            while (i+k < len(s)):
                temp = ''
                for n in range(i, k):
                    temp = temp + s[n]

                result = result + temp[::-1]
                i = i + k
            
            return result
        

s = Solution()
input_string = raw_input("string to reverse: ")
integer = int(raw_input("enter the integer: "))
print(s.reverseStr(input_string, integer))
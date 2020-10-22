'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Note: do not use string functions

Input: "Hello"
Output: "hello"

'''


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        new = ''
        for i in range(len(str)):
            if ord(str[i]) < 97 and ord(str[i]) > 64:
                new = new + chr(ord(str[i]) + 32)
            else:
                new = new + str[i]

        return new


s = Solution()
print(s.toLowerCase('HeLLo'))

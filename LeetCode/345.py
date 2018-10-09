"""
Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example1:
Input: "hello"
Output: "holle"

Example2:
Input: "leetcode"
Output: "leotcede"

"""

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        n = len(s)
        l = 0
        r = len(s) - 1
        vowels = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
        
        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
                
        return ''.join(s)

s = Solution()
S = 'hello'
print(s.reverseVowels(S))
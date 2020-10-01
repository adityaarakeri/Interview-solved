"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        words = str.split(' ')
        if len(set(list(pattern))) != len(set(words)):
            return False
                
        wordDict = {}
        index = 0
        length = len(pattern)
        for i in words:
            if index >= length:
                return False
            key = pattern[index]
            if key in wordDict and wordDict[key] != i:
                return False
            elif key not in wordDict:
                wordDict[key] = i
            index += 1
        return True
        
            
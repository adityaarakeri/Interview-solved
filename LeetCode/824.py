# -*- coding: utf-8 -*-

"""
🐐 Latin

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 

Example:
Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

"""

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = ('a','e','i','o','u', 'A', 'E', 'I', 'O', 'U')
        
        def goatStr(word, count):
            if word[0] in vowels:
                return "".join(word + goat + count * 'a')
            else:
                return "".join(word[1:] + word[0] +goat + count * 'a')
        
        if len(S) == 1:
            return goatStr(S, 1)
        
        count = 1
        goat = 'ma'
        
        S = S.split(" ")
        
        result = []
        for word in S:
            result.append(goatStr(word, count) + " ")
            count += 1
            
        return "".join(result).rstrip()
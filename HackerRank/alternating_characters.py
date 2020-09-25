
# Hackerrank Problem Alternating characters

# https://www.hackerrank.com/challenges/alternating-characters/problem?h_r=internal-search

"""

You are given a string containing characters A and B only. Your task is to change it 
into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, given the string s = AABAAB, remove an A at positions 0 
and 3 to make s= ABAB in 2 deletions.

"""


def alternatingCharacters(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count +=1
    return count
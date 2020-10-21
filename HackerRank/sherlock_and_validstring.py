# Hackerrank Problem Sherlock and the Valid String

# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

"""

Sherlock considers a string to be valid if all characters of the string 
appear the same number of times. It is also valid if he can remove just 1 
character at 1 index in the string, and the remaining characters will occur 
the same number of times. Given a string , determine if it is valid. If so, 
return YES, otherwise return NO.

For example, if s= abc, it is a valid string because frequencies are {a:1,b:1,c:1}.
 So is s = abcc because we can remove one c and have 1 of each character in the remaining 
 string. If s= abccc however, the string is not valid as we can only remove 1 occurrence of c.
  That would leave character frequencies of {a:1,b:1, c:2}.

"""


def isSame(x):
    z = x[0]
    for i in x:
        if i == 0:
          continue
        if i == z:
            continue
        else :
            return False
    return True
def isValid(s):
    freq = []
    aRepeatingNumberExist = False
    noOfCharacters = 0
    alphaNumeric = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25,

    }
    for i in range(26):
        freq.append(0)

    for x in s:
        freq[alphaNumeric[x]] += 1
    
    if isSame(freq):
        return "YES"
    else:
        for e in range(len(freq)):
            freq[e] -= 1
            if isSame(freq):
                return "YES"
            else:
                freq[e] +=1
    return "NO"  
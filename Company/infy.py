# -*- coding: utf-8 -*-
"""
Given a string, find the substring based on following conditions:

 1. The substring must be the longest one of all the possible substring in the given string.
 2. There must not be any repeating characters in the substring.
 3. If there is more than one substring satisfying the above two conditions, then print the substring which occurs first.
 4. Length of the substring must be minimum

If there is no substring satisfying all the aforementioned conditions then print -1.


"""

def test_1(string=""):
    substring = ""
    test_list = []
    initial = 0
    for char in string:
        for i in range(initial,len(string)):
            substring+=string[i]
            if substring.count(string[i])>1:
                test_list.append(substring[:-1])
                initial+=1
                substring = ""
                break
    maxi=""
    for word in test_list:

        if len(word)>len(maxi):
            maxi = word
    if len(maxi)<3:
        return "-1"
    else:
        return maxi

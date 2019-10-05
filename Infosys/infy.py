# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 08:41:26 2019

@author: Keshu
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

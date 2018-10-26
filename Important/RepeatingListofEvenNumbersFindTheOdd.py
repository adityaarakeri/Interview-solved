# Find from alist of numbers where each number is repeating
# even number of times except one. Find that number ?
# Input:
# [1,1,2,2,3,4,4,5,6,5,6]
#
# Output:
# 3
from timeit import timeit as ti

def RepeatingEvenList(aList):
    s=ti(number=10000)

    res=0
    for i in aList:
        res ^= i

    e=ti(number=10000)

    return  res, s-e

def UsingDict(aList):

    s=ti(number=10000)

    #d={i: aList.count(i) for i in aList }

    d={}

    for i in aList:
        if i in d:
            d[i]+=1
        else:
            d[i]=1


    res=0
    for k,v in d.items():
        if v==1:
            res=k

    e=ti(number=10000)

    return res, s-e



a=[1,1,2,2,3,4,4,5,6,5,6]
print RepeatingEvenList(a)
print UsingDict(a)


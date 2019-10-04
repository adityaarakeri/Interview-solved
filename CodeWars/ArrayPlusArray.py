#!/usr/bir/#!/usr/bin/#!/usr/bin/env python
"""
PROBLEM:
I'm new to coding and now I want to get the sum of two arrays
...actually the sum of all their elements.
I'll appreciate for your help.
P.S. Each array includes only integer numbers. Output is a number too.

TEST:
Some test cases can be found in the test folder

Answer by @mauricerivers
"""
print("Code Wars - Array Plus Array!")

# function defition
def array_plus_array(arr1,arr2):
    # variable used to add the array membeers
    sum = 0

    # loop through arr1 and add each item to sum
    for item in arr1:
        sum += item

    # loop through arr2 and add each item to sum
    for item in arr2:
        sum += item

    return sum

# simple terminal function call
# should print 21
print(array_plus_array([1, 2, 3], [4, 5, 6]))

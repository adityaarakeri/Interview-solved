"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

"""
from functools import reduce


def brute_force(arr):
    new = []
    # t = 1
    # for i in arr:
    #     t *= i
    t = reduce((lambda x, y: x*y), arr)

    for i in arr:
        if i == 0:
            return [0]*len(arr)
        new.append(t/i)

    return new


print(brute_force([2, 3, 1]))

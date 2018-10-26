"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

2,3,4,-1,1 => 2
1,2,3,0 => 3

"""

def func(arr):

    A = set(arr)
    A1 = set([i for i in range(min(A), max(A)+1)])
    
    diff = A1.difference(A)
    if len(diff) == 0:
        return max(A)+1
    for i in diff:
        if i > 0:
            return i

A = [3, 4, -1, 1]
# A = [1, 2, 0]
print(func(A))
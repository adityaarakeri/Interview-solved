"""
This problem was asked by Google.

A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
"""

def regularNumbers(N):
    if N <= 0:
        return []
    result = [1]
    for i in range(1, N):
        if i%2==0 and i%3==0 and i%5==0:
            result.append(i)

    return result

print(regularNumbers(60))
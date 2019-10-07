"""
The Fibonacci numbers, commonly denoted F(n) form a sequence,
called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N (N-th number in fibonacci sequence), calculate F(N).

Input: 6
Output: 8
Explanation: F(6) = 0, 1, 1, 2, 3, 5, 8
             F(6) = F(5) + F(4) = 5 + 3 = 8.
"""

def fibonacci_recursive(N: int) -> int:
    if N <= 1:
        return N
    return fibonacci_recursive(N - 1) + fibonacci_recursive(N - 2)

def fibonacci_iterative(N: int) -> int:
    a, b = 0, 1
    if N <= 1:
        return N
    for i in range(N):
        a, b = b, a + b
    return a

if __name__=='__main__':
    print(fibonacci_recursive(10))
    print(fibonacci_iterative(10))

'''
Fibonacci series: 1 1 2 3 5 8 13 ...

Write a function to spit out the nth Fibonacci number 
input:
5

output:
5
'''


def fib(limit):

    a, b = 0, 1
    for i in range(limit):
        a, b = b, a+b

    return a


print(fib(10))

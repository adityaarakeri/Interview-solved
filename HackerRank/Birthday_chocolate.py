'''

Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares s = [2,2,1,3,2], .
 She wants to find segments summing to Ron's birth day,d = 4  with a length equalling his birth month, m = 2. 
 In this case, there are two segments meeting her criteria: [2,2,] and [1,3].

Function Description

Complete the birthday function in the editor below. It should return an integer denoting the number of ways Lily can divide the chocolate bar.

birthday has the following parameter(s):

s: an array of integers, the numbers on each of the squares of chocolate
d: an integer, Ron's birth day
m: an integer, Ron's birth month



Input Format

The first line contains an integern , the number of squares in the chocolate bar.
The second line contains n space-separated integers s[i], the numbers on the chocolate squares where 0<= i <n.
The third line contains two space-separated integers, d and m, Ron's birth day and his birth month.


Sample Input 0

5
1 2 1 3 2
3 2
Sample Output 0

2


'''

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):

    tot_p = (len(s)-m)+1
    return len([1 for i in range(tot_p) if sum(s[i:i+m])  == d])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

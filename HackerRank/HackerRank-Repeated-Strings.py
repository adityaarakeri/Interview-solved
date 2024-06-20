#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    string = ''
    if (len(s) == 1 and s == 'a'):
        return n
    elif (len(s) == 1 and s != 'a'):
        return 0
    else:
        r = n%len(s)
        q = int(n / len(s))
        count = s.count('a')
        count = (count*q)
        for i in range(r):
            string = string + s[i]
        for j in string:
            if j == 'a':
                count = count + 1
        return(count)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

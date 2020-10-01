#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    dictionary = dict()
    ls = []
    for i in arr:
        try:
            dictionary[i] += 1
        except:
            dictionary[i] = 1
    
    max_val = max(dictionary.values())
    for key, item in dictionary.items():
        if(max_val == item):
            ls.append(key)
    ls.sort()
    return ls[0]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
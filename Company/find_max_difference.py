"""
Asked at box

# Maximum difference between two elements such that larger element appears after the smaller number

# Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element appears after the smaller number.

#Input : arr = {2, 3, 10, 6, 4, 8, 1}
#Output : 8
#Explanation : The maximum difference is between 10 and 2.

"""

def max_diff(arr):
    n = len(arr)
    if n == 0:
        return -1
    if n == 2 :
        if n[0] < n[1]:
            return n[1] - n[0]
        else:
            return -1
    else:
        result = []
        for i in range(2, n):
            diff = 0
            _slice = arr[:i][:-1] # getting the slice of slice since we will only need the elements except the last element
            last = arr[:i][-1]
            
            if max(_slice) < last:
                diff = last - min(_slice)
                result.append(diff)

        if len(result) != 0:
            return max(result)
        else:
            return -1


A = [2, 3, 10, 6, 4, 8, 1]
print(max_diff(A))
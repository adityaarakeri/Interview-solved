"""
Smallest subarray with sum greater than a given value
Given an array of integers and a number x, 
find the smallest subarray with sum greater than the given value.


Examples:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}

arr[] = {1, 2, 4}
    x = 8
Output : Not Possible
Whole array sum is smaller than 8.
"""


# arr -> provided array
# n -> length of array
# x -> provided integer
def small_sub(arr, n, x):
    
    start = 0
    end = 0
    cur_sum = 0
    min_len = n + 1 

    while (end < n):

        while (cur_sum <= x and end < n):
            cur_sum += arr[end]
            end += 1

        while (cur_sum > x and start < n):
            if (end - start  < min_len):
                min_len = end - start

            cur_sum -= arr[start]
            start += 1

    return min_len


arr = [1, 1, 1, 1, 2, 1,3]
n = len(arr)
x = 4
print(small_sub(arr, n , x))
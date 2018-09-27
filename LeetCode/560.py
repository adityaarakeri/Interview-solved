"""
Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Ex:1
Input:nums = [1,1,1], k = 2
Output: 2

"""

def subarraysum(nums, k):
    sums = {0:1}
    res = 0
    cur_sum = 0
    for n in nums:
        cur_sum += n
        res += sums.get(cur_sum - k, 0) # if it is not found return 0
        sums[cur_sum] = sums.get(cur_sum,0) + 1

    return res

A = [1,2,3]
k = 5
print(subarraysum(A, k))
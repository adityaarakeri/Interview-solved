"""
Shortest Unsorted Continuous Subarray

Given an integer array, you need to find one continuous subarray that 
if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order
to make the whole array sorted in ascending order.
"""

def findUnsortedSubarray(nums):

    temp = sorted(nums)
    l = 0
    r = len(nums) - 1

    while l < r:
        if nums[l] == temp[l]:
            l += 1
        elif nums[r] == temp[r]:
            r -= 1
        else:
            return r - l + 1
    
    if r == l:
        return 0


A = [2, 2, 4, 8, 10, 9, 15]
print(findUnsortedSubarray(A))
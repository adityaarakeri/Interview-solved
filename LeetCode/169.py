"""
169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
from typing import List

def majorityElement(nums: List[int]) -> int:
    # len
        n = len(nums)
        # create an empty dict
        d = {}
        # majority value
        m = n/2
        # iterate over the nums
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        
        # iterate over the dict
        for k,v in d.items():
            if v > m:
                return k

q1 = [3,2,3]
q2 = [2,2,1,1,1,2,2]
print(majorityElement(q1))
print(majorityElement(q2))

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

source: https://leetcode.com/problems/two-sum/description/
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i, e in enumerate(nums):
            if (target - e) in result:
                return [result[target - e], i]
            result[e] = i

s = Solution()
print(s.twoSum([1,2,3,4], 7))
print(s.twoSum([4,4], 8))

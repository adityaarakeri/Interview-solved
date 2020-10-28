'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        di = {}
        x = 0
        while x < len(nums):
            print(x)
            if nums[x] in di.keys():
                nums.remove(nums[x])
                x = x-1
            else:
                di[nums[x]] = 1
            x = x+1
        return len(nums)

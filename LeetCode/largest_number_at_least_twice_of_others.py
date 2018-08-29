'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
'''

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        for n in nums:
            if n > max1:
                max1 = n
        max2 = 0
        for n in nums:
            if n > max2 and n != max1:
                max2 = n
        
        if max1 >= 2 * max2:
            return nums.index(max1)
        else:
            return -1
        
s = Solution()
print(s.dominantIndex([1,3,6,0]))
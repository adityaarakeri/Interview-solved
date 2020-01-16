class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return nums
        mx = max(nums)
        mx = max(mx, len(nums))
        nums = set(nums)
        return [c for c in [x for x in range(1, mx + 1)] if c not in nums]

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

'''
class Solution:
    def canJump(self, nums):
        """
         : type nums: List[int]
         : rtype : bool

        """
        s,k=1,len(nums)
        if k==1:
            return True
        for i in range(1,k):
            if nums[k-1-i]==0:
                s+=1
            elif nums[k-1-i]>=s:
                s=1
            else:
                s+=1
        if s==1:
            return True
        else:
            return False



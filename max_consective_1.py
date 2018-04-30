# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ans = 0
        for num in nums:
            if num == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
        return ans

l = Solution()
print l.findMaxConsecutiveOnes([1,1,0,1,1,1])
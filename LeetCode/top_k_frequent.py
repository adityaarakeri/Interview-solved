'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

'''

class Solution:

    def topKFrequent(self, nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        m,v,ma={},[],0

        for i in nums:

            if i in m:
                m[i]+=1

            else:
                m[i]=1

            if m[i]>ma:
                ma=m[i]

        while k!=0:

            for i in m:

                if k==0:
                    break

                if m[i]==ma:
                    v.append(i)
                    k-=1
            ma-=1
        return v  
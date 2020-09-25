# Given a non-empty array of integers, return the k most frequent elements.

class Solution:
    def topKFrequent(self, nums:List[int], k: int) -> List[int]:
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
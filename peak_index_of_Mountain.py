# Let's call an array A a mountain if the following properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].



class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        peak = 0
        i = 0
        while (i+2 < len(A)):
            firstP = A[i]
            midP = A[i+1]
            lastP = A[i+2]
            
            if firstP < midP > lastP:
                peak = A.index(midP)
            
            i = i + 1 
        
        return peak

s = Solution()
print(s.peakIndexInMountainArray([0,1,2,0]))
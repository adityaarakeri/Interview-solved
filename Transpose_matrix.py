"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
Example:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

"""

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return zip(*A)

    def transpose2(self, A):
        n = len(A)
        l = len(A[0])
        new = [[0]*n for i in range(l)]
        for i in range(n):
            for j in range(l):
                new[j][i] = A[i][j]

        return new

s = Solution()
print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(s.transpose2([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))


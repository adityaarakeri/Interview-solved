"""
Flipping an Image

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].


Example:
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

"""

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        
        for i in range(len(A)):
            temp = []
            for j in A[i][::-1]:
                if j == 0:
                    temp.append(1)
                else:
                    temp.append(0)
            result.append(temp)
            
        return result

    def flip1(self, A):
        return [[row[j]^1 for j in range(len(row)-1, -1, -1)] for row in A]


s = Solution()
_input = [[1,1,0],[1,0,1],[0,0,0]]
final =  [[1,0,0],[0,1,0],[1,1,1]]
output1 =  s.flipAndInvertImage(_input)
output2 = s.flip1(_input)

import unittest

class TestArray(unittest.TestCase):


    def test_array1(self):
        self.assertEqual(final, output1)

    def test_array2(self):
        self.assertEqual(final, output2)


if __name__ == '__main__':
    unittest.main()
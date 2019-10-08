import unittest
from matrixOperations import MatrixOperations
m = MatrixOperations()

class testMatrixOperations(unittest.TestCase):

    #Test to check the transpose of given matrix is correct
    def test_transpose(self):
        transpose = m.transpose([[2, 5, 3], [4, 7, 6],[3, 8, 4]])
        self.assertTrue(transpose, [[2, 4, 3], [5, 7, 8], [3, 6, 4]])
   
    #Test to check the transpose is 3X3 matrix
    def test_transpose_size(self):
        transpose = m.transpose([[2, 5, 3], [4, 7, 6],[3, 8, 4]])
        self.assertTrue(len(transpose),3)   # row size
        self.assertTrue(len(transpose[0]),3)    # column size

    #Test to check the multiplication of given matrix and its transpose is correct
    def test_mult(self):
        mult = m.mult([[2, 5, 3], [4, 7, 6],[3, 8, 4]],[[2, 4, 3], [5, 7, 8], [3, 6, 4]])
        self.assertTrue(mult,[[38, 61, 58], [61, 101, 92], [58, 92, 89]] )

    #Test to check the multiplication of two matrices is 3X3 matrix.
    def test_mult_size(self):
        mult = m.mult([[2, 5, 3], [4, 7, 6],[3, 8, 4]],[[2, 4, 3], [5, 7, 8], [3, 6, 4]])
        self.assertTrue(len(mult),3)    # row size  
        self.assertTrue(len(mult[0]),3) # column size

if __name__ == "__main__":
    unittest.main()
    
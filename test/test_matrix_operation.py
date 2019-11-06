from Company.matrixOperations import MatrixOperations

m = MatrixOperations()
#Test to check the transpose of given matrix is correct
def test_transpose():
    transpose = m.transpose([[2, 5, 3], [4, 7, 6],[3, 8, 4]])
    assert transpose == [[2, 4, 3], [5, 7, 8], [3, 6, 4]]

#Test to check the transpose is 3X3 matrix
def test_transpose_size():
    transpose = m.transpose([[2, 5, 3], [4, 7, 6],[3, 8, 4]])
    assert len(transpose) == 3   # row size
    assert len(transpose[0]) == 3    # column size

#Test to check the multiplication of given matrix and its transpose is correct
def test_mult():
    mult = m.mult([[2, 5, 3], [4, 7, 6],[3, 8, 4]],[[2, 4, 3], [5, 7, 8], [3, 6, 4]])
    assert mult == [[38, 61, 58], [61, 101, 92], [58, 92, 89]]

#Test to check the multiplication of two matrices is 3X3 matrix.
def test_mult_size():
    mult = m.mult([[2, 5, 3], [4, 7, 6],[3, 8, 4]],[[2, 4, 3], [5, 7, 8], [3, 6, 4]])
    assert len(mult) == 3    # row size  
    assert len(mult[0]) == 3 # column size

"""
Provided a 2D n x n matrix, given two coordinates first and the last, return the average of cube 

Ex:
Input: 
3 =>  3 x 3 matrix
[[0,0], [0,1], [0,2]
,[1,0], [1,1], [1,2]
,[2,0], [2,1], [2,2]]

coordinate => 4 => [1,1]
coordinate => 6 => [2,2]

result : 3
average => ([1,1],[1,2],[2,1][2,2])/4 => 3


"""

def create_2d_matrix(n):
    result = []

    for i in xrange(n):
        j = 0
        while j < n:
            result.append((i,j))
            j += 1

    return result

def find_average_2d_matrix(n, i1, i2):

    matrix = create_2d_matrix(n)

    result = [sum(i) for i in matrix]
    print i1, i2
    print result

    if i2 - i1 % n == 0:
        return 0    
    if i1 < 0:
        return 0
    if i2 > len(matrix) - 1:
        return 0

    return result[i2]
    
    
print(find_average_2d_matrix(4, 4, 8))
# # This coding question was asked in Philips Healthcare Campus Interview.
# # Level: Easy.

# # Problem Statement: 
# # 3X3 matrix was given.
# # Find the transpose of that matrix.
# # Multiply the original matrix with transpose.
# # Print the Result.

# #Solution:

class MatrixOperations:

    #Function which returns the transpose of given matrix A
    def transpose(self, A) :
        #T is used to store the transpose of A
        T = [[0, 0, 0], 
            [0, 0, 0], 
            [0, 0, 0]] 

        # iterate through rows
        for i in range(len(A)):
        # iterate through columns
            for j in range(len(A[0])):
                T[j][i] = A[i][j]

        return T

    #Function for multiplication of given matrix A and its transpose T
    def mult(self,A,T) :

        result = [[0, 0, 0], 
                [0, 0, 0], 
                [0, 0, 0]] 

        # iterating by row of A 
        for i in range(len(A)): 

            # iterating by coloum by T 
            for j in range(len(T[0])): 

                # iterating by rows of T
                for k in range(len(T)): 
                    result[i][j] += A[i][k] * T[k][j] 

        return result
 
tmp = MatrixOperations()
#Given matrix A
A = [[2, 5, 3], 
    [4, 7, 6], 
    [3, 8, 4]]
T = tmp.transpose(A)
print ("Transpose of given Matrix is: ",T)

result = tmp.mult(A,T)
print("Solution:    ",result)
 
#Result :
# Transpose:   [[2, 4, 3], [5, 7, 8], [3, 6, 4]]
# Solution:     [[38, 61, 58], [61, 101, 92], [58, 92, 89]]

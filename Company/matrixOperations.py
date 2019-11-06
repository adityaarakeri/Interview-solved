
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
    def mult(self, A,T) :

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
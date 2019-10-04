# This coding question was asked in Philips Healthcare Campus Interview.
# Level: Easy.

# Problem Statement: 
# 3X3 matrix was given.
# Find the transpose of that matrix.
# Multiply the original matrix with transpose.
# Print the Result.

#Solution:

A = [[2, 5, 3], 
    [4, 7, 6], 
    [3, 8, 4]] 

#B is used to store the transpose of A
B = [[0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]] 

# iterate through rows
for i in range(len(A)):
   # iterate through columns
   for j in range(len(A[0])):
       B[j][i] = A[i][j]

result = [[0, 0, 0], 
        [0, 0, 0], 
        [0, 0, 0]] 
  
# iterating by row of A 
for i in range(len(A)): 
  
    # iterating by coloum by B  
    for j in range(len(B[0])): 
  
        # iterating by rows of B 
        for k in range(len(B)): 
            result[i][j] += A[i][k] * B[k][j] 
  
for r in result: 
    print(r) 
    

#Result :
# [38, 61, 58]
# [61, 101, 92]
# [58, 92, 89]
    
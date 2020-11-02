#valid sudoku by anshika gupta

#check if row  is valid
def validrow(arr,row):
    s=set()
    for i in range(9):
        if arr[row][i] in s:
            return False
        if arr[row][i] !='.':
            s.add(arr[row][i])
    return(True)

#check if the column is valid
def validcol(arr,col):
    s=set()
    for j in range(9):
        if arr[j][col] in s:
            return False
        if arr[j][col]!='.':
            s.add(arr[j][col])

    return(True)

#check if the 3x3 box is valid
def validbox(arr,row,col):
    s=set()
    for i in range(3):
        for j in range(3):
            if arr[i+row][j+col] in s:
                return False
            if arr[i+row][j+col] !='.':
                s.add(arr[i+row][j+col])

        return(True)


def check_validity(arr,row,col):
    return(validrow(arr,row) and validcol(arr,col) and validbox(arr,row - row%3,col-col%3))

def sudoku(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if not check_validity(arr,i,j):
                return(False)
    return(True)

# n=int(input("enter order of the matrix"))
matrix=[[ '5', '3', '.', '.', '7', '.', '.', '.', '.' ],
             [ '6', '.', '.', '1', '9', '5', '.', '.', '.' ],
             [ '.', '9', '8', '.', '.', '.', '.', '6', '.' ],
             [ '8', '.', '.', '.', '6', '.', '.', '.', '3' ],
             [ '4', '.', '.', '8', '.', '3', '.', '.', '1' ],
             [ '7', '.', '.', '.', '2', '.', '.', '.', '6' ],
             [ '.', '6', '.', '.', '.', '.', '2', '8', '.' ],
             [ '.', '.', '.', '4', '1', '9', '.', '.', '5' ],
             [ '.', '.', '.', '.', '8', '.', '.', '7', '9' ]]
if sudoku(matrix)==True:
    print("Valid")
else:
    print("Invalid")

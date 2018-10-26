# given the number generate a 2 Dimentional matrix of '*'

def matrix(n, c):

    for i in range(n):
        print n * c


number = int(raw_input("Enter the Dimension of the matrix: "))
character = raw_input("Enter the character to make the matrix: ")
matrix(number, character)

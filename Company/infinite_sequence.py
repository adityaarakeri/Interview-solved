"""
Give an infinite sequence 0, -1, -1 , 0, 1, 1, 0, -1, -1, 0, 1, 1.....

write a function which takes n1, n2 and num
n1 and n2 are part of the sequence
and num is the nth sequence integer in the infinite sequence

Example: 
Input: -1, -1, 5
Output: 1

-1 occurs at position 1 
-1 occurs at position 2
counting from -1, -1, 0 , 1, 1 <-
returning the 5th element i.e 1

0, -1,  -1, 0, 1, 1, 0, -1, -1, 0, 1,   1
0,  1,   2, 3, 4, 5, 6,  7,  8, 9, 10, 11

"""

def sequence(n1, n2, num):

    seq = [0, -1, -1, 0, 1, 1]

    if num%3 == 0:
        return 0
    else:



    return 
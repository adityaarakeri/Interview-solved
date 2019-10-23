'''
  Given an array of integers, write a function that will return the smallest integer.
  
  For an example:
    Given the array [1, 2, 3, 4]
    The code must output 1
'''


def find_smallest_int(arr):
    smallest = arr[0]
    
    for i in range(len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
    return smallest

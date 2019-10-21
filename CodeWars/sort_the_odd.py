"""
URL:
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

DESCRIPTION:
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""

def sort_array(source_array):
    new_arr = [x for x in source_array if x % 2 == 1]
    new_arr.sort(reverse=True)
    for i, elem in enumerate(source_array):
        if elem % 2 == 1:
            source_array[i] = new_arr.pop()
    
    return source_array
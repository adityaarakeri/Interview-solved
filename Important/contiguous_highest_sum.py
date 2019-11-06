"""
Given an array as input, extract the pair of contiguous integers that have the highest sum of all pairs. Return the pair as an array.
I = [5, 2, 4, 6, 3, 1]
O = [4,6]

"""

def contiguous_pair(arr):
    if len(arr) == 2:
        return arr
    elif len(arr) < 2:
        return []
    else:
        pair = []
        highest = 0

        for i in range(len(arr)- 1):
            if highest < arr[i] + arr[i+1]:
                highest = arr[i] + arr[i+1]
                pair = [arr[i], arr[i+1]]
            
        return pair

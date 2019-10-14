"""
Test cases for recursion_all_indices.py 
"""

# function to be tested
def AllIndexesRecursive(input, x, start): 
    if (start == len(input)): 
        ans = [] 
        return ans 
    smallIndex = AllIndexesRecursive(input,x,start + 1) 
    if (input[start] == x): 
        myAns = [0 for i in range(len(smallIndex) + 1)] 
        myAns[0] = start 
        for i in range(len(smallIndex)): 
            myAns[i + 1] = smallIndex[i] 
        return myAns 
    else: 
        return smallIndex 

def AllIndexes(input, x): 
    return AllIndexesRecursive(input, x, 0) 

# function to test All_Indexes
def test_recursion_all_indices():
    assert AllIndexes([15,24,58,61,79,3,97,81,81,45,62,21,72,72,68,45,11,50,87,20,28,77,51,89,58,66],23)==[], "Should be empty"
    assert AllIndexes([34,57,82,41,65,35,82,27,36,12,6,40,66,99,25,29,22,25,12,24,65,15,5,43,28,33,76,32,13,95,22,84,71,23,28,7,65,94,18,47,9,42,61,73],61) ==[42], "Should be 42"
    assert AllIndexes([21,22,46,12,61,25,33,16,99,96,25],25) ==[5,10], "Should be 5 and 10"


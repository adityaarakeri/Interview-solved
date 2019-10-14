"""

Given an array of distinct integers with size N and an integer X 
Display all the indices of the integer X in the array using RECURSION only
If no X occurs in the array no output should be displayed
Examples:
Input:  arr = {10, 12, 11, 12, 13, 12} ,X=12
Output: 1 3 5
Input:  arr = {1, 2, 4, 3} ,X=9
Output: No Output
Input:  arr= {8, 8, 8, 8, 8} ,X=8
Output: 0 1 2 3 4

"""
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

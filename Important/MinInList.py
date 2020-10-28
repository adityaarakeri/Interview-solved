# Linear solution

def findMin(lst):

    minInList = lst[0]

    for i in lst:
        if i < minInList:
            minInList = i

    return minInList


print(findMin([5, 4, 3, 2, 1, 0]))

#implement Binary Search

def BinarySearch(alist, num):
    found = False
    first = 0
    last  = len(alist) - 1

    while first <= last and not found:
        middle = (last + first)//2

        if alist[middle] == num :
            found = True
        elif alist[middle] < num :
            first = middle + 1
        else:
            last = middle - 1

    return found

alist = [x for x in range(15)]
num = int(raw_input("enter the number you want to search > "))
print BinarySearch(alist , num)
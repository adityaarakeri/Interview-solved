# array = [1,2,3,6,3,4,5,6,7,8,4]

def PeakFinder(a):

    L=len(a)
    m=L//2
    a1=[]

    #base case
    try:
        if a[m-1] < a[m] > a[m+1]:
             a1.append(a[m])
    except IndexError:
        return []


    checkLeft = a[m-1] > a[m] > a[m+1]
    checkRight = a[m-1] < a[m] < a[m+1]

    if checkLeft:
        return PeakFinder(a[:m])
    elif checkRight:
        return PeakFinder(a[m:])
    else:
        return a1


a = [1,2,3,6,3,4,5,6,7,8,4]
#a=[]
print PeakFinder(a)

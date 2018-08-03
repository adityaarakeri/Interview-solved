# Question given an array of [0,1,0,2,0,1,0,2,0,1] sort it such that 0's are in the beginning, 1's in the middle and 2's at the end

# input: [0,1,0,2,0,1,0,2,0,1] 
# output: [0,0,0,0,0,1,1,1,2,2]

def sort_this(a):
    lo = 0
    hi = len(a) - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid] 
            hi = hi - 1
    return a

print(sort_this([0,1,0,2,0,1,0,2,0,1]))
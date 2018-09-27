# do the insertion sort algorithm
def insertionSort(A):

    for i in range(1, len(A)):
        currentVal = A[i]
        position = i

        while position > 0 and A[position-1] > currentVal:
            A[position] = A[position-1]
            position = position - 1

        A[position] = currentVal

A = [54,26,93,17,77,31,44,55,20]
insertionSort(A)
print A
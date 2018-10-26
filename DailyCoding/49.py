"""
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.

"""

def findsum(A):
    result = sum(A)
    for i in range(len(A)):
        _sum = max([sum(A[:i]), sum(A[i:])])
        if result < _sum:
            result = _sum

    return result if result > 0 else 0


# A = [34, -50, 42, 14, -5, 86]
A = [-5, -1, -8, -9]
print(findsum(A))

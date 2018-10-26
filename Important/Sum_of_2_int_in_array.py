
"""
You are given an array of n integers and a number k. Determine whether there is
a pair of elements in the array that sums to exactly k. For example, given the
array [1, 3, 7] and k = 8, the answer is "yes", but given k = 6 the answer is
"no."
"""

# time complexity O(n^2)
def two_sum_brute(arr, target):

    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if (arr[i] + arr[j] == target):
                return True
    return False

# time complexity O(n)
def two_sum(arr, target):
    s = set()
    for n in arr:
        if (target - n) in s:
            return True
        s.add(n)
    return False

print(two_sum_brute([1,2,3], 5))
print(two_sum_brute([1], 5))
print(two_sum([1,2,3], 5))
print(two_sum([1], 5))
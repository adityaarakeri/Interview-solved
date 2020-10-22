"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


"""


def sum_brute_force(arr, k):
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if (arr[i] + arr[j] == k):
                return True

    return False


def sum_improved(arr, k):
    s = set()
    for i in arr:
        if (k - i) in s:
            return True
        s.add(i)

    return False


print(sum_brute_force([10, 9, 7, 8, 2, 0, -1], 17))
print(sum_improved([10, 9, 7, 8, 2, 0, -1], 17))

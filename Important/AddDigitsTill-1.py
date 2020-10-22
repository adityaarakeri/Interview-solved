# Given a non-negative integer num, repeatedly add
# all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2.
# Since 2 has only one digit, return it.

# Recursive
def addNum(n):

    s = str(n)
    if len(s) == 1:
        return n
    else:
        res = 0
        for i in s:
            res = res + int(i)

        return addNum(res)

# Non Recursive


def addNum2(n):

    s = str(n)
    res = 0
    while (len(s) > 1):

        for i in s:
            res = res + int(i)

        s = str(res)
        res = 0

    return s

# the same problem for multiplying digits


def multiplyNums(n):

    s = str(n)
    res = 1
    count = 0
    while len(s) > 1:
        for i in s:
            res = res * int(i)

        count += 1
        s = str(res)
        res = 1

    return count


num = input("enter a number to add all digits > ")
num1 = input("enter a number to add all digits > ")

print(addNum(num))
print(addNum2(num1))
print(multiplyNums(num))

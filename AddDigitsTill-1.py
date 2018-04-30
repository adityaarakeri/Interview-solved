# Given a non-negative integer num, repeatedly add
# all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2.
# Since 2 has only one digit, return it.

def addNum(n):

    s = str(n)
    if len(s) == 1:
        return n
    else:
        res = 0
        for i in s:
            res = res + int(i)

        return addNum(res)

num = int(raw_input("enter a number to add all digits > "))
print addNum(num)

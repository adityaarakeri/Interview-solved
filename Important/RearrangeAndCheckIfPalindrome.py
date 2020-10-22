import itertools


def check_if_palindrome(s):

    result = False
    tup_list = []
    for i in itertools.permutations(s, len(s)):
        tup_list.append(i)

    for tup in tup_list:
        if palindrome(tup):
            result = True
            break

    return result


def palindrome(s):
    return s[:] == s[::-1]


print(check_if_palindrome(input(('Enter a string to check if palindrome > '))))

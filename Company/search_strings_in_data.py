"""
asked at Amazon

Provided a large string, and an array of strings. return a dictonary with the number of times each string from the array appears in the large string

# Input: S =>'this is a large string in a file'
# Input: A => ['is', 'a']
# output => {'is': 2, 'a': 3}
# explanation:
#   'is' appears in 'this', 'is' == 2
#   'a' appears in 'a', 'large', 'a' == 3

"""


def return_dict(S, A):

    result = {}
    # if inputs => []
    if len(A) == 0:
        return {}

    for i in range(len(A)):
        result[A[i]] = 0

        if S.count(A[i]):
            result[A[i]] = S.count(A[i])

    return result


S = 'this is a large string in a file'
A = ['is', 'a']
result = return_dict(S, A)
print(result)

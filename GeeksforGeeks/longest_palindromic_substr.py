'''Given a string S
find the longest palindromic substring in S.
Substring of string S: S[i....j]
where 0 ≤ i ≤ j < len(S).
Palindrome string: A string which reads the same backwards.
More formally, S is palindrome if reverse(S) = S.
Incase of conflict, return the substring which occurs first
( with the least starting index ).

Required Time Complexity O(n2). '''

# function to find longest palindromic substring
# dynamic approach


def find_longst_pal_substr(string):
    maxLen = 1
    l = len(string)

    low = high = start = 0
    for i in range(1, l):
        low = i - 1
        high = i
        while low >= 0 and high < l and string[low] == string[high]:
            if high - low + 1 > maxLen:
                start = low
                maxLen = high - low + 1
            low -= 1
            high += 1
        low = i - 1
        high = i + 1
        while low >= 0 and high < l and string[low] == string[high]:
            if high - low + 1 > maxLen:
                start = low
                maxLen = high - low + 1
            low -= 1
            high += 1
    return string[start:start + maxLen]


'''for _ in range(int(input())):
    s = input()
    print(find_longst_pal_substr(s)) '''

s = 'aaaabbaa'
print(find_longst_pal_substr(s))

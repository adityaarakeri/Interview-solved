# return a first recurring char
# Q: ABCDA
# A: A

def firstRecurring(str):

    if (len(str) == 0 or len(str) == 1):
        return str

    if (str.isdigit()):
        return '\0'

    dict = {}
    for ch in str:
        if ch in dict:
            return ch
        else:
            dict[ch] = 0

    return '\0'


print(firstRecurring(input("enter the string to get first recurring char: ")))


def reverse1(s):
    return s[::-1]

def reverse2(s):
    rev=''
    for i in range(len(s)):
        ind = -(i+1)
        rev += s[ind]

    return rev


print reverse1(raw_input("Enter a string to be reversed [method 1]: "))
print reverse2(raw_input(("Enter a string to be reversed [method 2]: ")))

from Implement.Stack import Stack


def reverseUsingStack(str):

    s = Stack()
    rev_s = ''
    for char in str:
        s.push(char)

    while not s.isEmpty():
        rev_s = rev_s + s.pop()

    return rev_s


print(reverseUsingStack(input("Enter a string to be reverse > ")))

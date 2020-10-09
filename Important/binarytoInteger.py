# Q : create a func to create binary to integer
# input : 1010
# Output : 0*2^0 + 1*2^1 + 0*2^2 + 1*2^3 = 0 + 2 + 0 + 8 = 10

def binary_to_integer(b):

    if not b.isdigit():
        return "Not a binary"

    if int(b) == 0:
        return 0
    elif int(b) == 1:
        return 1
    else:
        a = list(b)
        f = 0
        i = 0
        while len(a) != 0:
            p = a.pop()
            f = f + int(p) * 2**i
            i = i + 1

        return f


print(binary_to_integer(input("enter the binary digit to convert to integer: ")))

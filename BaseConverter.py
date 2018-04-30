# implemeting a Base converter which takes in a int and the base to convert

def BaseConverter(num, base):

    digits= "0123456789ABCDEF"
    stack= []
    newString = ""

    while num > 0:
        rem = num % base
        stack.append(rem)
        num = num // base

    while len(stack)>0:
        newString = newString + digits[stack.pop()]


    return newString

print BaseConverter(26,2) # binary conversion
print BaseConverter(26,8) # Octal
print BaseConverter(26,16) # Hexadecimal
print BaseConverter(26,26)   # base of 26

import random

def Cipher(string):

    if len(string)==0:
        return ""
    if len(string)==1:
<<<<<<< HEAD
        return random.choice([chr(i) for i in xrange(97,123)])
=======
        return string
>>>>>>> d40be58a114407f7ab1062973b0dd1f05318646e

    c=0
    new_string=[]
    while c < len(string):
        a = random.choice([chr(i) for i in xrange(97,123)])
        if string[c] == ' ':
            new_string.append(' ')
            c+=1
        elif a not in string:
            new_string.append(a)
            c+=1

    return ''.join(new_string)

print Cipher(raw_input("Enter a string to be Ciphered: "))


def Palindrome(string):

    if string=='':
        return False

    if len(string)==1:
        return True

    return string.lower()==string[::-1].lower()

print Palindrome(raw_input("Is this a Palindrome? :"))

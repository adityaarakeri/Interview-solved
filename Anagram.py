'''
Write a function to check if two strings are anagrams of each other
Anagram = 'abcd' is anagram of 'cdba'

input:
'abcd'
'cdba'

output:
True

'''

def is_Anagram(str1, str2):

    l1=list(str1)
    l2=list(str2)

    return sorted(l1)==sorted(l2)

a=raw_input("Enter the first string: ")
b=raw_input("Enter the second string: ")
print is_Anagram(a,b)

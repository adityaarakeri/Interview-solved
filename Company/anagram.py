# Question: Check if two strings are anagram or not
# Example: abcd and dabc are anagram
# aaba aabad are not anagram
string1 = input()
string2 = input()
# if length of strings are not same they are not anagram
# count the occurance of each alphabet and if they are same then strings are anagram
if len(string2) != len(string1):
    print("Strings are not anagram")
else:
    alphabet_count1 = [0]*26
    alphabet_count2 = [0]*26
    anagram = True
    for i in range(len(string1)):
        alphabet_count1[ord(string1[i])-97] += 1
        alphabet_count2[ord(string2[i])-97] += 1
        
    for i in range(26):
        if alphabet_count1[i] != alphabet_count2[i]:
            anagram = False
            break
        
    if anagram:
        print("Strings are anagram")
    else:
        print("Strings are not anagram")

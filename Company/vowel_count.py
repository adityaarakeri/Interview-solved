"""
You get a string and need to return its number of vowels.
For this test, we will only consider a, e, i, o and u as vowels.

For example:

Input: "Alabama"
Output: 4

Input: "Caserta"
Output: 3

"""


#For Loop
def count(input_string):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in input_string.lower():
        if letter in vowels:
            num_vowels += 1

    return num_vowels


#Lambda
countLambda = lambda s: sum(s.lower().count(i) for i in 'aeiou')
"""
Function that count lowercase letters in a given string and
return the letter count in a hash with 'letter' as key and 
count as 'value'. 

Example 
letter_count('arithmetics') 
    #=> {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}

"""

from collections import Counter


def letter_count(s):
    char_counts = Counter()
    char_counts.update(list(s))
    return char_counts

#execute the function
letter_count("arithmetics")

# Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)

# After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

# Given a sentence , tell Roy if it is a pangram or not.

s = raw_input().lower()

import string

alphabets = [x for x in string.ascii_lowercase]

result = []
for char in alphabets:
    if char in s:
        result.append(1)
    else:
        result.append(0)

if 0 in result:
    print "not pangram"
else:
    print "pangram"
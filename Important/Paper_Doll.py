# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶
# paper_doll('Hello') - -> 'HHHeeellllllooo'
# paper_doll('Mississippi') - -> 'MMMiiissssssiiippppppiii'


def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result


# Check-1
print(paper_doll('Hello'))

# Check 2
print(paper_doll('Mississippi'))

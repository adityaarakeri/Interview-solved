import timeit
import collections

def firstNonRecurring(string):

    d = collections.OrderedDict()

    for char in string.lower():
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    while d > 0:
        #Pairs are returned in LIFO order if last is true or FIFO order if false.
        char , count = d.popitem(last=False) # if you change the last=True , you will get the last non dup item

        if count == 1:
            return char

    return None

def firstNonRecurring1(string):

    d = {}
    nonRecurring = []
    for ch in string:
        if ch in d:
            d[ch]+=1
        else:
            d[ch]=1
            nonRecurring.append(ch)

    for ch in nonRecurring:
        if d[ch] == 1:
            return ch
    
    return None


def firstNonRecurring_optimal(s):
    import string
    letters = string.ascii_letters
    index = [s.index(l) for l in letters if s.count(l) == 1]
    if len(index) != 0:
        return s[min(index)]
    else:
        return None

print(firstNonRecurring('ABCDABD'))
print(firstNonRecurring1('ABCDABD'))
print(firstNonRecurring_optimal('ABCDABD'))




# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("firstNonRecurring('ABCDABD')", setup="from __main__ import firstNonRecurring"))
#     print(timeit.timeit("firstNonRecurring1('ABCDABD')", setup="from __main__ import firstNonRecurring1"))
#     unittest.main(verbosity=2)
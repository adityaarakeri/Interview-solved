import collections

def first_non_dup_item(string):

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


print first_non_dup_item(raw_input("Enter a string to return first Non Dupe item: "))

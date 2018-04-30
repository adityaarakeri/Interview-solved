# print the duplicates in a string

def Dup(s):

    s= s.lower()
    s= list(s)

    d={}

    for ind, ele in enumerate(s):
        if ele in d:
            d[ele].append(ind)
        else:
            d.update({ele:[ind]})
            # d[ele] = [ind]  - can also be written like this

    print d

    for key, val in d.items():
        if len(val) > 1:
            print "{} has indices {}".format(key, val)


Dup(raw_input("> "))

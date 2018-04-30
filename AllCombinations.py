import itertools

def CombinationOfWords(str):

    if len(str)==1:
        return str

    str_list=[]
    for i in range(len(str)):
        ls = permutations(str, i)
        str_list.append(ls)
        i+=1

    new_list=[]
    for s in str_list:
        if isinstance(s, list):
            for item in s:
                new_list.append(''.join(item))

    #new_list = set(new_list)

    return list(new_list)

def permutations(str, i):

    perm_list=[]
    for s in itertools.permutations(str, i+1):  #i+1 since it needs to reach len of string
        perm_list.append(list(s))

    return perm_list


#attempt to change algo
def Combinations2(str, step=0):

    l =len(str)
    s = list(str)

    for i in range(1, l+1):
        pass




print CombinationOfWords(raw_input('Enter a string to get all the combinations: '))

'''
Write a function to flatten a list of lists

input:
[1,[2,3,4],[5,[6,7]]]

output:
[1,2,3,4,5,6,7]

'''


#recursive function
def flattenList(lst, f_lst=None):

    if f_lst is None:
        f_lst=[]

    for l in lst:
        if isinstance(l,list):
            flattenList(l, f_lst)
        else:
            f_lst.append(l)

    return f_lst


#using itertools
import itertools
def flattenList1(lst):

    f_lst = list(itertools.chain.from_iterable(lst))

    return f_lst


print flattenList([[1,2,3],[4,5,6],['a','b'], [7], [8,9]])

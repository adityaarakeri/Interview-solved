'''  Provided a list of integers, return a list which is a multiple of 
every other integer except the one at its index

input 
[1,2,3,4]

output
[24,12,8,6]
'''
from functools import reduce


def list_of_int(old_list):

    new_list = []

    for val in old_list:
        d_list = []
        for val1 in old_list:
            if old_list.index(val) != old_list.index(val1):
                d_list.append(val1)
                i = reduce(lambda x, y: x*y, d_list)
        new_list.append(i)

    return new_list


def listofints(l):

    if l == []:
        return []
    elif len(l) == 1:
        return l

    stack = []
    for i in range(len(l)):
        res = multiply(l[:i], l[i+1:])
        stack.append(res)

    return stack


def multiply(l1, l2):
    if l1 == [] or l2 == []:
        return 1
    i = reduce(lambda x, y: x*y, l1)
    j = reduce(lambda x, y: x*y, l2)
    return i*j

# solution


def get_products_of_all_ints_except_at_index(int_list):

    # we make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    i = 0
    while i < len(int_list):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    i = len(int_list) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    return products_of_all_ints_except_at_index


# print list_of_int([1,2,3,4])
print(listofints([1, 2, 3, 4]))

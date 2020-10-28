
l = [1, 2, -1, 5, 8, 90, 2, 21, 32, 45]


def highest_num(l):

    max_num = l[0]

    for num in l:
        if num > max_num:
            max_num = num

    return max_num


def highest_num1(l):

    return sorted(l)[-1]


def highest_num2(l):
    l.sort()
    return l[-1]


print(highest_num(l))

print(highest_num1(l))

print(highest_num2(l))

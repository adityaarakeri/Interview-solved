from timeit import timeit as ti


def ltest1():
    start = ti(number=1000)
    l = []
    for i in range(1000):
        l = l+[i]
    end = ti(number=1000)

    return start-end


def ltest2():
    start = ti(number=1000)
    l = []
    for i in range(1000):
        l.append(i)
    end = ti(number=1000)

    return start-end


def ltest3():
    start = ti(number=1000)
    l = [i for i in range(1000)]
    end = ti(number=1000)

    return start-end


def ltest4():
    start = ti(number=1000)
    l = list(range(1000))
    end = ti(number=1000)

    return start-end


print("concat        : {} milliseconds".format(str(ltest1())))
print("append        : {} milliseconds".format(str(ltest2())))
print("comprehension : {} milliseconds".format(str(ltest3())))
print("list range    : {} milliseconds".format(str(ltest4())))

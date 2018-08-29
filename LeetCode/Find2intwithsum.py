# Let A be an array of random integers and a given integer x.
# Find all pairs of numbers from the array whose sum is equal to x.

# import collections

def find2ints(arr, x):

    #d = [0] * 10000
    d = {x-i : (i*0) for i in arr}

    new_l = []
    for i in arr:
        temp = x - i

        if temp >= 0 and d[temp] == 1:
            new_l.append((temp,i))

        d[i] = 1
    return new_l

arr = [1,2,3,4,5,6,7,7,10]
x = 10

print find2ints(arr, x)

'''
Sieve of Sundaram
To find the prime number less than n

'''


def SieveOfSundaram(N):
    n = (N - 2) / 2

    '''
    This array is used to separate numbers of the form i+j+2ij 
    from others where  1 <= i <= j   

    '''
    marked = [False] * (n + 1)

    prime = []

    '''
    Main logic of Sundaram.  Mark all numbers of the 
    form i + j + 2ij as true where 1 <= i <= j 

    '''

    for i in xrange(1, n):
        j = i
        while (i + j + 2 * i * j) <= n:
            marked[i + j + 2 * i * j] = True
            j += 1

    if N > 2:
        prime.append(2)

    for i in xrange(1, n):
        if marked[i] == False:
            prime.append(2 * i + 1)

    return prime


print SieveOfSundaram(20)
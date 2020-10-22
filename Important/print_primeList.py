for n in range(1, 101):
    prime = True
    for i in range(2, n):
        if(n % 2 == 0):
            prime = False
    if prime:
        print(n)

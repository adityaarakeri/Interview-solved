# 1 1 2 3 5 8

def fib(limit):

	a,b = 0,1
	fib_list=[]
	for i in xrange(limit):
		a,b = b, a+b
		fib_list.append(a)

	for v in fib_list:
		print v

fib(7)
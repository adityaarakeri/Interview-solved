'''
Write a function which takes 
i= integer
s= index
n= increment

convert the integet i to binary and swap the 1/0 starting from index s 
and incrementing it to n

'''


def IntToBin(i, s, n):

	i_binary = bin(i)[2:]

	i1= i_binary[:s]
	i2= i_binary[s:n+s]

	i_l = []
	for c in i2:
		if c=='0':
			i_l.append('1')
		else:
			i_l.append('0')
	i_F= ''.join(i_l)

	i3= i_binary[len(i1)+len(i2):]

	int_form = int((i1+i_F+i3), 2)

	print "Sent int: {}".format(i)
	print "converted int: {}".format(int_form)

IntToBin(60, 3, 5)


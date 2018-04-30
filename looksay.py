'''
Function to look at the provided alphanumeric string and say it in order

input:
'1A2BBC'

output:
'111A122B1C'

'''


def looksay(look):
	
	
	look = str(look)
	if len(look) == 0 :
    		return 'Empty string entered'
	else:
		prev = look[0]
		count = 1
		say = ''

		for char in look[1:]:
			if char == prev:
				count += 1
				continue
			say += str(count) + prev
			prev = char
			count = 1

		return say + str(count) + prev 

print looksay(raw_input("Enter a value which needs to be looked and said: ")) #number will go here

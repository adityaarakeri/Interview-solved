#0 1
#1 11
#2 21
#3 1211
#4 111221
#5 312211
#6 13112221

# i = 1
# n = 7

def looksay(look):
	look = str(look)
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

print looksay(raw_input("Enter a value which needs to be looked and sayed: ")) #number will go here

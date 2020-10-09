def averageValue(s): 
	sum_char = 0
	for i in range(len(s)): 
		sum_char += ord(s[i])
	return sum_char // len(s) 

if __name__ == "__main__": 
	
	s = input();

	print(averageValue(s)) 
	s1=input()

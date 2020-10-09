#Evaluate an expression represented by a String.
#Expression can contain parentheses, you can assume parentheses are well-matched.
#For simplicity, you can assume only binary operations allowed are +, -, *, and /.
#Arithmetic Expressions can be written in one of three forms:
#->Infix Notation: Operators are written between the operands they operate on, e.g. 3 + 4 .
#->Prefix Notation: Operators are written before the operands, e.g + 3 4
#->Postfix Notation: Operators are written after operands.

def precedence(op): 
	
	if op == '+' or op == '-': 
		return 1
	if op == '*' or op == '/': 
		return 2
	return 0
  
def applyOp(a, b, op): 
	
	if op == '+': return a + b 
	if op == '-': return a - b 
	if op == '*': return a * b 
	if op == '/': return a // b 
 
def evaluate(tokens): 
	
	values = [] 
	
	ops = [] 
	i = 0
	
	while i < len(tokens): 
		if tokens[i] == ' ': 
			i += 1
			continue
		elif tokens[i] == '(': 
			ops.append(tokens[i]) 
		elif tokens[i].isdigit(): 
			val = 0
			while (i < len(tokens) and
				tokens[i].isdigit()): 
			
				val = (val * 10) + int(tokens[i]) 
				i += 1
			
			values.append(val) 
		elif tokens[i] == ')': 
		
			while len(ops) != 0 and ops[-1] != '(': 
			
				val2 = values.pop() 
				val1 = values.pop() 
				op = ops.pop() 
				
				values.append(applyOp(val1, val2, op)) 
			ops.pop() 
		
		else: 
			while (len(ops) != 0 and
				precedence(ops[-1]) >= precedence(tokens[i])): 
						
				val2 = values.pop() 
				val1 = values.pop() 
				op = ops.pop() 
				
				values.append(applyOp(val1, val2, op))  
			ops.append(tokens[i]) 
		
		i += 1 
	while len(ops) != 0: 
		
		val2 = values.pop() 
		val1 = values.pop() 
		op = ops.pop() 
				
		values.append(applyOp(val1, val2, op)) 
	return values[-1] 

if __name__ == "__main__": 
	s=input("Enter Expression : ");
	print(evaluate(s))
	s1=input()
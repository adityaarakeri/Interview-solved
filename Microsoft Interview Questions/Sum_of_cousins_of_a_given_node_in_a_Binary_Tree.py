class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def findCousinSum( root, key): 

	if (root == None): 
		return -1

	if (root.data == key): 
		return -1
	
	currSum = 0

	size = 0

	q = [] 
	q.append(root) 

	found = False

	while (len(q)): 
		if (found == True): 
			return currSum 
		size = len(q) 
		currSum = 0

		while (size): 
			root = q[0] 
			q.pop(0) 
			if ((root.left and root.left.data == key) or
				(root.right and root.right.data == key)) : 
				found = True 
			else: 
				if (root.left): 
					currSum += root.left.data 
					q.append(root.left) 
				
				if (root.right) : 
					currSum += root.right.data 
					q.append(root.right) 

			size -= 1
	return -1
if __name__ == '__main__': 
	root = newNode(1) 
	root.left = newNode(3) 
	root.right = newNode(7) 
	root.left.left = newNode(6) 
	root.left.right = newNode(5) 
	root.left.right.left = newNode(10) 
	root.right.left = newNode(4) 
	root.right.right = newNode(13) 
	root.right.left.left = newNode(17) 
	root.right.left.right = newNode(15) 

	print(findCousinSum(root, 13)) 

	print(findCousinSum(root, 7)) 

    s1=input()
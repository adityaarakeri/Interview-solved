
# Python3 code to demonstrate working of 
# Check if all elements in list follow a condition 
# Using all() 
  
# initializing list 
test_list = [4, 5, 8, 9, 10] 
  
# printing list 
print("The original list : " + str(test_list)) 
  
# Check if all elements in list follow a condition 
# Using all() 
res = all(ele > 3 for ele in test_list) 
  
# Printing result 
print("Are all elements greater than 3 ? : " + str(res)) 

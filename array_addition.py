'''
given an integer array [1,2,3,9] add a carry to it so that it becomes [1,2,4,0]

Input:
[1,2,9,9]
Output:
[1,3,0,0]

'''

def array_add(A):
    carry = 1
    new = []
    for i in A[::-1]:
        add = i + carry
        if add != 10 :
            carry = 0
            new.append(add)
        else:
            new.append(0)
    
    if carry == 1:
        new.append(1)

    return new[::-1]

print(array_add([1,9,9,9,9,9]))
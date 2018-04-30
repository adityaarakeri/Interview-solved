#You are given  numbers. Store them in a list and find the second largest number.

try:
    N=int(raw_input())
except ValueError as va:
    print "expected an int:{}".format(va)

l=list(raw_input().split())
    
new_l=[]
for v in l:
    new_l.append(int(v))

max_val=max(new_l)

while max_val in new_l:
    new_l.pop(new_l.index(max_val))

print max(new_l)


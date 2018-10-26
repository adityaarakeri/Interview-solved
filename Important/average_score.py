try:
    N=int(raw_input())
except ValueError as va:
    print "Expected int input"

names_list=[]
while True:
    try:
        name_score=raw_input().split()
    except ValueError as va:
        print "Expected string input"
    
    names_list.append(name_score)
    
    if len(names_list)==N:
        break

names_only=[]

for name in names_list:
    names_only.append(name[0])


while True:
    try:
        name=str(raw_input())
    except ValueError as va:
            print "Expected string input"

    if name in names_only:
        break

avg_dict={}
for v in names_list:
    avg= (float(v[1])+float(v[2])+float(v[3]))/3

    avg_dict[v[0]]= '{:.2f}'.format(avg)

print avg_dict
exit()

for k,v in avg_dict.iteritems():
    if k==name:
        print v



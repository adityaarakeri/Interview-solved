
def find_substring(s1, s2):

    l1=len(s1)
    l2=len(s2)
    count=0

    if s1==s2:
        return count+1
    else:
        for i in range(l1-l2+1):
            if s2 == s1[i:l2+i]:
                count+=1

    return count

print (find_substring('abcdcdcd', 'cd'))

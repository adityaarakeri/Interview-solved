"""
Approach:
 start from the end given if the end is odd then perform 2 operations simultaneously decrement end by 1 and divide end with 2 else
 divide end with 2 if it is even continuously perform these operations until end equals start
 """

def solve(start,end):
    count=0
    while(end//2>=start):
        if(end%2==1):
            end-=1
            end//=2
            count+=2
        else:
            end//=2
            count+=1
    count+=end-start
    return(count)    
if __name__=="__main__":
    start=int(input())
    end=int(input())
    print(solve(start,end))    
"""
Test:
start=2
end=9

Output:
3
"""    
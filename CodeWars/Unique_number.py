###This one is from a problem I soved on codewars in my beginner level
#Qustion
'''There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
'''

#Solution

def find_uniq(arr):
    if arr[0] != arr[1]:
        if arr[0] != arr[2]:
            return arr[0]
        else:
            return arr[1]           
    else:
        for i in arr[2:]:
            if i != arr[0]:
                return i
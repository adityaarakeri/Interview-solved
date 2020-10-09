'''

write a func which replaces the vowels in a string and outputs the string

input
victor 

output
voctir
'''


def vowelReplace(str):
    l = list(str)
    vowel = ['a', 'e', 'i', 'o', 'u']
    deque = []
    newString = ''

    # edge case:
    if len(l) == 0:
        return "Empty"
    elif len(l) == 1:
        return str

    # everything else
    else:
        for char in l:
            if char in vowel:
                deque.append(char)
        len_d = len(deque)

        if len_d % 2 == 1:
            half = len_d/2
            middle = deque[len_d/2]
            deque = deque[:half] + deque[half+1:]
        else:
            middle = ''

        rearFlag = True
        while len(deque) > 0:
            for i in range(len(l)):
                if l[i] == middle:
                    newString = newString + middle
                elif l[i] not in vowel:
                    newString = newString + l[i]
                else:
                    if rearFlag:
                        newString = newString + deque.pop()
                        rearFlag = False
                    else:
                        newString = newString + deque.pop(0)
                        rearFlag = True

        return newString


print(vowelReplace(input("Enter the string: ")))

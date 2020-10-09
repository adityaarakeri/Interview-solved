# ABBCD

def lookandSay(look):

    say = ''
    for char in look:
        i = look.index(char)
        if i != look.index(look[-1]):
            nex = look[i+1]
            count = '1'

            if char == nex:
                count = int(count)+1
                continue
            else:
                say = str(count) + char

    print(say)


lookandSay(input("Enter a string for LookandSay: "))

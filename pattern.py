# given input:  3[d2[ca]]
# output: dcacadcacadcaca

#  3[d[caca]]  d2[ca]d2[ca]d2[ca]
# dcacadcacadcaca

# stack 1 = [ 3, 2 ]
# stack 2 = [ '[', 'd', '[', 'c', 'a' ]

# import a predefined stack or create our own stack in here
from ImplementStack import Stack

def pattern_solve(inp):
    word_stack = Stack()
    num_stack = Stack()

    for char in inp:
        if (char != ']'):
            if(char.isalpha()):
                # print('alpha: {0}'.format(char))
                word_stack.push(char)
            else:
                if(char.isdigit()):
                    # print('number: {0}'.format(char))
                    num_stack.push(char)
                else:
                    # print('not a num: {0}'.format(char))
                    word_stack.push(char)


    word_till_now = ''
    while(word_stack.isEmpty() == False):
        word = word_stack.pop()

        if(word != '['):
            word_till_now = word + word_till_now

        if(word == '['):
            num = num_stack.pop()

            word_till_now = word_till_now * int(num)

    
    return word_till_now    
# print(pattern_solve('3[d2[ca]]'))
print(pattern_solve('3[d2[ca]]'))

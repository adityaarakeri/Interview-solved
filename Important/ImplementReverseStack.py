#Implement a Reverse Stack in python

class ReverseStack():

    def __init__(self):
        self.items = list()

    def push(self,*args):
        for val in args:
            self.items.insert(0, val)

    def peek(self):
        return self.items[0]

    def pop(self):
        return self.items.pop(0)

    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)


s = ReverseStack()

s.push(1)
s.push(2)
s.push(3)
s.push(4,5)
s.push('test')

print s.items
print s.isEmpty()
print s.peek()
print s.size()
s.pop()
print s.items

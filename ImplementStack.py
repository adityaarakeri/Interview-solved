#Implement a Stack in python

class Stack():

    def __init__(self):
        self.items = list()

    def push(self,*args):
        for val in args:
            self.items.append(val)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def show(self):
        return (self.items)


# s = Stack()

# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4,5)
# s.push('test')

# print s.items
# print s.isEmpty()
# print s.peek()
# print s.size()
# s.pop()
# print s.items


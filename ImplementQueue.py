#implement a Queue which works on FIFO principle

class Queue():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, *args):
        for value in args:
            self.items.insert(0, value)

    def dequeue(self):
        return self.items.pop()


q = Queue()

q.enqueue(1)
q.enqueue("test")
q.enqueue(True)
q.enqueue(1.5)
q.enqueue(-1, 'test2', False)

# print q.items
# print q.size()
# print q.dequeue()
# print q.isEmpty()

class Queue(object):

    def __init__(self):
        self._list = list()

    def __str__(self):
        return str(self._list)

    def enqueue(self, item):
        self._list.append(item)

    def dequeue(self, item):
        if len(self._list) > 0:
            index = self._list.index(item)
            return self._list.pop(index)


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print q 
q.dequeue('c')
print q
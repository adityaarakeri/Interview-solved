
class Dequeue:
    """
    class which creates a Deque object
    """

    def __init__(self):
        self.items = list()

    def addRear(self, item):
        self.items.insert(0, item)

    def addFront(self, item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# d1 = Dequeue()
# d2 = Dequeue()
# s = input(">")
# for ch in s:
#     d1.addFront(ch)

# print d1.items

# for ch in s:
#     d2.addRear(ch)

# print d2.items

# print d1.items == d2.items

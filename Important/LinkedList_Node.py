# A single node of a linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def insert(self, data):
        new_node = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                curret = current.get_next


A = [1,2,3,4]

N = Node(24)
N.set_next(25)
N.set_next(26)
N.set_next(27)
print(N.data)
print(N.get_next())
print(N.get_next())

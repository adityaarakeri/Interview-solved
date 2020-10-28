class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext


N = Node(24)
print(N.data)
N.setNext(25)
N.setNext(26)
N1 = Node(25)
print(N1.data)

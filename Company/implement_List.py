

class List():

    def __init__(self):
        self._list = list()

    def __str__(self):
        return str(self._list)

    def addItem(self, item):
        if item not in self._list:
            self._list.append(item)

    def removeItem(self, item):
        self._list.remove(item)


l = List()
l.addItem('a')
l.addItem('a')
l.addItem('b')
print(l)
l.removeItem('b')
print(l)

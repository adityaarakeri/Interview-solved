# base class
class Base(object):

    def __init__(self, x):
        self.x = x


class Derived(Base):

    def __init__(self, x, y):
        # sending the x value up to base class
        super(Derived, self).__init__(x)
        self.y = y

    def printD(self):
        print(self.x + " " + self.y)


d = Derived("hi", "there")
d.printD()  # prints => hi there

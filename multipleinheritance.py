# base class
class Base1:

    def __init__(self):
        self.str1 = "string from base1"
        print("base1 class")

class Base2:

    def __init__(self):
        self.str2 = "string from base2"
        print("base2 class")

# Base1 and Base2 are being inherited by Deriver
class Deriverd(Base1, Base2):

    def __init__(self):
        # calling initializers for both base classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Deriver class")

    def printStr(self):
        print self.str1 + " " + self.str2

d = Deriverd()
d.printStr()

# prints => 
# base1 class
# base2 class
# Deriver class
# string from base1 string from base2
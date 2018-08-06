# printing objects/class

class MyClass:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "a: " + self.a + "b: " + self.b

m = MyClass("hi", "there")
print(m)
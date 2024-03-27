class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super(Child, self).__init__(name)
        self.age = age

    def display(self):
        print(self.name, self.age)

obj = Child("child name", 6)
obj.display()
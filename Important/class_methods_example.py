# types of class methods
class MyClass(object):

    # instance method has access to the instance of the object MyClass
    def method(self):
        return "instance method called ", self

    # class method has access to the class object MyClass and not the instance of MyClass
    @classmethod
    def classMethod(cls):
        return "class method called", cls

    # static method does not have access to either class Object MyClass or the instance of MyClass
    @staticmethod
    def staticMethod():
        return "static method called"


obj = MyClass()
print(obj.method())
print(obj.classMethod())
print(obj.staticMethod())
# prints =>
# ('instance method called ', <__main__.MyClass object at 0x10586cb10>)
# ('class method called', <class '__main__.MyClass'>)
# static method called
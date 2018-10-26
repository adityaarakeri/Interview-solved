# define a regular class
class Car:

    # hidden properties are defined between __?
    __hiddenProperty = "test"

    def __init__(self, model):
        self.model = model

    def model(self):
        print(self.model)

mazda = Car("Mazda")
print(mazda.model)
# this will give u an error
# print(mazda.__hiddenProperty)

# can be read by below
print(mazda._Car__hiddenProperty)
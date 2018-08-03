# 1
# decorator function takes a function
# returns a function
def decorator1(function):

    # has a nested function
    def addWelcome(name):
        return "Welcome to " + function(name)

    # returns the nested function
    return addWelcome

# decorator is appended above a regular function
@decorator1
def welcome(name):
    return name

# using the welcom now

print welcome("decorator example")
# prints => Welcome to decorator example

# 2
# decorator to add data to func
def decorator2(function):
    function.data = "attached data to function"
    return function

@decorator2
def addition(x, y):
    return x + y

print(addition(2,3))
print(addition.data)
# prints => 7
# prints => attached data to function




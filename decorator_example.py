# 1
# decorator function takes a function
# returns a function
def decorator1(function):

    # has a nested function
    def addWelcome(name):
        return "\nWelcome to " + function(name)

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
    function.data = "\nattached data to function in decorator 2"
    return function

@decorator2
def addition(x, y):
    return x + y

print(addition(2,3))
print(addition.data)
# prints => 5
# prints => attached data to function


# 3
# decorator to add functionality to func along with uneven arguments
def decorator3(function):
    def wrapper(*args, **kwargs): # adding *args **kwargs makes it take any no of arguments
        print "\nexecuting inside of decorator 3: {}".format(function.__name__)
        return function(*args, **kwargs)
    return wrapper

@decorator3
def display():
    print "Running this inside of a decorator"

display()

@decorator3
def display_info(name, age):
    print "Display_info ran with {} and {}".format(name, age)

display_info('John', 32)

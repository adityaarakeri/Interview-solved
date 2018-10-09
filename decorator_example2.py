# decorator as a function
# decorator to add functionality to func along with uneven arguments
def decorator_function(original_function):
    def wrapper(*args, **kwargs): # adding *args **kwargs makes it take any no of arguments
        print "\nexecuting inside of Decorator Function: {}".format(original_function.__name__)
        return original_function(*args, **kwargs)
    return wrapper

@decorator_function
def display():
    print "Running this inside of a decorator"

@decorator_function
def display_info(name, age):
    print "Display_info ran with {} and {}".format(name, age)

display()
display_info('John', 32)


# decorator as a class
# class decorator adds functionality to a func
class Decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print "\nexecuting inside of Decorator Class: {}".format(self.original_function.__name__)
        return self.original_function(*args, **kwargs)
    
@Decorator_class
def display():
    print "Running this inside of a decorator"

@Decorator_class
def display_info(name, age):
    print "Display_info ran with {} and {}".format(name, age)

display()
display_info('John', 32)
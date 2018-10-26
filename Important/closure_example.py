# example of a nested function with out closure
# outer func
def outer_function(text):
    
    def inner_fuction():
        print(text)
    
    inner_fuction()

outer_function("Hi, from nested function without closure")

# example of nested function with closure
def outer_function1(text):

    def inner_function1():
        print(text)

    return inner_function1 # notice the nested func being returned with out the paranthesis

out_func = outer_function1("Hi, From nested function with Closure")
out_func()
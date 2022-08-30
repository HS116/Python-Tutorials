#Corey Schafer Tutorial
#decorators alter the functionality of a function, without changing the inner code
#it uses the @ symbol


def outer_function1(msg):

    def inner_function1():
        print(msg)

    return inner_function1()

outer_function1("hi")


def outer_function2(msg):

    def inner_function2():
        print(msg)

    return inner_function2

#In Python, functions can be treated as objects, hence we can return functions and store them so they can be called later
my_func = outer_function2("hi")
my_func()

#A decorator allows us to do this in a more concise way
# A decorator is a function that takes another function as an argument, adds some functionality and returns another function

def decorator_function(original_function):
    def wrapper_function():
        #The main reason for decorators is we can easily add extra functionality to a function without changing the function
        #E.g. extra functionality is the below print statement
        print(f"The wrapper function executed before the {original_function.__name__} function")
        return original_function()

    return wrapper_function

def display():
    print("display function ran")

#make sure to pass in the function "display", not the called function i.e. return value "display()"
decorated_display = decorator_function(display)
decorated_display()


#Exact same as above but using the Python decorator syntax:

def decorator_function2(original_function):
    #Important!
    #The number of arguments in the wrapper_function() must match the number of arguments in the passed in function e.g. display()
    #Solution: using *args, **kwargs allowing us an arbitrary number of positional and key-word args
    def wrapper_function2(*args, **kwargs):
        print(f"The wrapper funciton executed before the {original_function.__name__} function")
        return original_function(*args, **kwargs)
    return wrapper_function2

@decorator_function2
def display2():
    print("Display function executed")

@decorator_function2
def display_info(name, age):
    print(f"Display Info function executed. Name: {name}. Age: {age}")

display_with_decorator = display2
display_with_decorator()
display_info_with_decorator = display_info
display_info_with_decorator("Dell", 5)

#TechWithTim tutorial
'''
Main use cases of decorators:
Testing the performance of a function e.g. time, memory
class and static methods
property decorators
Logging, but not sure about this tbh
'''



#Decorator - Testing performnce of a function
import time
def timer_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        start = time.time()
        return_value =  original_function(*args, **kwargs)
        end = time.time()
        print(f"Total time taken for {original_function.__name__} function: {end-start}")
        return return_value
    return wrapper_function

@timer_decorator
def iter():
    a = []
    for i in range(10000000):
        a.append(i)
print("\n\n\n")

iter()














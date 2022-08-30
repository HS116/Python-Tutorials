#Unit testing is much better automated way of testing compared to print statements

def add(x,y):
    return x + y

def subtract(x,y):

    return x - y

def multiply(x,y):
    
    return x * y

def divide(x,y):

    if y == 0:
        raise ValueError("Exception: Cannot divide by 0")
    else: 
        return x / y


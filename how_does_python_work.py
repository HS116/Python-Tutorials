'''Python is an intepreted language. 
Python code is first checked for any syntax errors, 
and then converted into byte code, which is lower level code, but it is still not machine executable
Then this byte code is intepreted into machine code and directly executed line by line. 

This is why Python is not popular for mobile applications because there must be a Python intepreter. 

'''


#A lot of the errors are checked at runtime, and not detected by the compiler e.g. the below code
class A:
    def __init__(self):
        #In Java the compiler would tell us we have an error e.g. "method bark() is not defined". 
        #But this does not happen in Python
        self.bark()

'''some other weird stuff u can do in Python:
- define a function inside a loop
- create a class inside the definition of a function
- 
'''






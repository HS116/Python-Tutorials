#Dunder methods (also known as magic methods or data model methods) are methods that start and end with double underscores

import inspect

'''
E.g. a list is an object. 
We can do certain things to a list
'''
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
# E.g. add to a list
print(list1+list2)
#E.g. multiply a list
print(3*list1)
#E.g. printing a list. 
# What enable us to print the list in this format, rather than just printing the memory location of the list obj
print(list1)

#What enable us to do these operations are dunder methods. 
#for lists these dunder methods are "under the hood", so we can't see them

#But we can similarly create dunder methods for our own objects, 
# so that we can interact with them more dynamically like with the traditional Python objects e.g. lists

#Example
class Person:

    #Make sure it is "__init__", NOT "__innit__"
    def __init__(self, name):
        self.name = name

    #This dunder method is like the toString() method in Java
    #It allows us to print in a particular format, rather than defaulting printing the memory location of the object
    def __repr__(self):
        #f string technique, helps us include variables in an easier way
        return f"Person: {self.name}"

    #This dunder method describes what happens when we multiply the object i.e. use "*"
    def __mul__(self, num):
        
        if type(num) is not int:
            #raise is kinda like "throw" in Java
            raise Exception("Not an integer")
        else:
            self.name = self.name * num

    #more examples of dunder methods
    def __len__(self):
        return len(self.name)

    def __call__(self, arg):
        print("called this function " + str(arg))

    
person1 = Person("Neil")
print(person1)
person1 * 5
print(person1)
print(len(person1))
person1("person 2")


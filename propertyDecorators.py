#property decorators allow us to have getter, setter and deleter functionality for our attributes

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@gmail.com"

    def full_name(self):
        return f"{self.first} {self.last}"


emp1 = Employee("John", "Smith")

emp1.first = "Jim"

print(emp1.first)
print(emp1.last)
#Problem is the email does not change, even tho first name changed
print(emp1.email)
#No problem with full_name method, cuz it uses the updated first and last name each time it is run
print(emp1.full_name())

#To fix the issue of the email not updating, we can create getter and setter methods
#BUT we can also add a property decorator to these getter and setter methods, so that we can access it like an attribute
#If we did not add property decorators,
#  then everyone that was accessing the email attribute would now have to switch to using the email method

class Employee_Better:
    def __init__(self, first, last):
        self.first = first
        self.last = last


    #To fix the issue of the email not updating, we can create getter methods
    #BUT we can also add a property decorator to these getter and setter methods, so that we can access it like an attribute
    #If we did not add property decorators,
    #  then everyone that was accessing the email attribute would now have to switch to using the email method
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    # @property decorator for getters, @"property_name".setter for setters, @"property_name".deleter for deleters i.e. resetting attribute
    @full_name.setter
    def full_name(self, full_name):
        self.first, self.last = full_name.split(" ")

    @full_name.deleter
    def full_name(self):
        print("Full name deleted")
        self.first = None
        self.last = None

emp2 = Employee_Better("John", "Smith")

emp2.first = "Jim"
print(emp2.first)
print(emp2.last)
#Now even though we have email() and full_name() methods, 
# we can still access them like attributes cuz we have a property decorators
print(emp2.email)
print(emp2.full_name)
#cuz we have a property_name.setter decorator we can do this
emp2.full_name = "Neil Alb"
print(emp2.first)
print(emp2.last)
#cuz we have property_name.deleter decorator we can do this
del(emp2.full_name)
print(emp2.first)
print(emp2.last)



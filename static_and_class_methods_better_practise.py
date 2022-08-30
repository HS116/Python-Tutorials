'''
3 types of methods in Python OOP:
Regular methods
- these methods take the instance i.e. self as the first arg (and maybe include other additioal args)
Class methods
- these methods take the class i.e. cls as the first arg (and maybe include other additional args)
- should have the @classmethod decorator above the method
- Main use of class methods is for alternative constructors
Static methods
- these methods do not take the instance or the class as an argument. 
- they are just included in the class because they logically kinda belong there
- should have the @staticmethod decorator above the method
'''
#from Corey Schafer tutorial
class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"
        self.pay = pay

        Employee.num_of_emps += 1

    #regular method
    def fullname(self):
        return self.first + " " + self.last
    
    #another regular method
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    #main use of class methods is alternative constructors, since Python can only use one __init__()
    #E.g. in this case we pass in a string with the data separated by dashes
    @classmethod
    def create_with_text(cls, txt):
        first, last, pay = txt.split("-")
        #in general, only use class methods when u specifically need the class e.g. for a constructor
        return cls(first, last, pay)

    @staticmethod
    #if we do not pass in a "self" or "cls" arg, then use a static method
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
    

emp1 = Employee("Alice", "Smith", 35000)
emp2 = Employee("Bob", "Jones", 25000)
#using a class method
emp3 = Employee.create_with_text("Charlie-Chaplin-60000")
print(emp3.email)
#using a static method
import datetime
my_date = datetime.date(2022, 4, 9)
print(Employee.is_workday(my_date))





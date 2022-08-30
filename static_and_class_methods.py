class Person():

    population = 50

    #make sure it is "__init__", NOT "__innit__"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18
    
    def display(self):
        print(self.name + " is " + str(self.age) + " years old")

newPerson = Person("Neil", 19)
print(newPerson.name)
print(Person.getPopulation())




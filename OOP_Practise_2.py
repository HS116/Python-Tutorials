class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
    
    def intro(self):
        print("My name is " + self.name + " and I am " + str(self.age) + " years old")
    
animal = Animal("Bob", 19, "Goat")
animal.intro()

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Dog")

dog = Dog("Jeff", 6)
dog.intro()

class Pen:
    def __init__(self, color, size):
        self.color = color
        self.size = size
    
    def write(self):
        print("Hi, I am a " + self.color + " pen")
    
pen = Pen("blue", 5)
pen.write()

class Vehicle:
    def __init__(self, wheels, cost, color):
        self.wheels = wheels
        self.cost = cost
        self.color = color

class Car(Vehicle):
    def __init__(self, cost, color, type = "Regular"):
        self.type = type
        super().__init__(4, cost, color)

bmw = Car(50000, "Black")
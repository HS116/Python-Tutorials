import turtle

class Polygon:
    #must include self
    #every parameter after self is what we will have to include when instantiating an object
    #but "size" is a default parameter i.e. it will be 100 unless explictly passed in a value
    def __init__(self, sides, name, size = 100):
        self.sides = sides
        self.name = name
        self.size = size

    def draw(self):
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.left(360 / self.sides)
        turtle.done()

square = Polygon(4, "square")
pentagon = Polygon(5, "pentagon")

#pentagon.draw()

hexagon = Polygon(6, "hexagon", 50)
#hexagon.draw()


#Inheritance
class Square(Polygon):
    def __init__(self, size = 100):
        # __init__ is kinda like the constructor in java
        super().__init__(4, "square", size)

    #Overriding methods, no need for override annotation i think like in Java
    def draw(self):
        turtle.color("blue")
        #remem it is "super()", NOT "super"
        super().draw()


square1 = Square(30)
square1.draw()

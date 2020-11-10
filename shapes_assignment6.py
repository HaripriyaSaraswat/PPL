import turtle

s=turtle.getscreen()
t=turtle.Turtle()

class Shape():
    def __init__(self, sides = 0, length = 0):
        self.sides=sides
        self.length=length
        
class Polygon(Shape):
    def info(self):
        print("Polygon is defined as a plane figure with at least three straight sides and angles, and typically five or more.")

class Square(Polygon):
    def display(self):
        for i in range(4):
            t.forward(100)
            t.right(90)  

class Hexagon(Polygon):
    def display(self):
        for i in range(6):
            t.forward(50)
            t.right(72)

            
class EquTriangle(Polygon):
    def display(self):
        for i in range(3):
            t.forward(50)
            t.right(60)            

class Circle():
    def display(self):
        r = 50
        t.circle(r)

   
sq=Square()
sq.display() 

#hx=Hexagon()
#hx.display() 

#tri=EquTriangle()
#tri.display() 

#cir.Circle()
#cir,display()   
turtle.done()
print("Topic : Method Overwritting ")
#   Parent class
class Shape:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    # calculating area 
    def area(self):
        return self.x * self.y

#   Child Class
class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius
        # accessing Parent Class Constructor
        super().__init__(radius,radius)
        # Calculating area
    def area(self):
        return 3.14 * super().area()

s1 = Shape(3,4)
print(s1.area())

C1 = Circle(3)
print(C1.area())

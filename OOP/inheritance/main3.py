# super() = Function used in a child class to call methods from a parent class (superclass)
#           Allows you to extend functionality of the inherited methods

# class Super:
#     pass

# class Sub(Super):
#     pass

class Shape:
    
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):

    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    # Method overwritting - the python will use this one
    # def describe(self):
    #     print(f"It is a circle with an area of {self.radius ** 2 * 3.14 }")

    def describe(self):
        print(f"It is a circle with an area of {self.radius ** 2 * 3.14 }")
        super().describe() # here we are extending the functionality of the method from Superclass

class Square(Shape):

    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width ** 2}")
        super().describe() 

class Triangle(Shape):

    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {(self.width * self.height) / 2}")
        super().describe() 



circle = Circle("red", True, 30)
square = Square("blue", True, 21)
triangle = Triangle("green", False, 15, 26)

print(circle.color)
print(square.color)
print(triangle.color)

circle.describe()
triangle.describe()
square.describe()
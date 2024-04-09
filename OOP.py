class Rectangle:
    def __init__(self, width, height):
        self.width = width  
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


def print_area(shape):
    print(shape.area())


rect = Rectangle(3, 9)
square = Square(5)

print_area(rect)   
print_area(square) 

# Create a class Rectangle with private attributes length and width.
# Overload '>' operator to compare the area of 2 rectangles.

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __gt__(self, other):
        return self.area() > other.area()

r1 = Rectangle(10, 4)
r2 = Rectangle(8, 6)

if r1 > r2:
    print("Rectangle 1 has larger area")
else:
    print("Rectangle 2 has larger area")

# OUTPUT:
# Rectangle 2 has larger area
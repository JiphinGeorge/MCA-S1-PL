# Create Rectangle class with attributes length and breadth and methods to find area and perimeter.
# Compare two Rectangle objects by their area.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# Creating objects
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)

print("Area of Rectangle 1:", r1.area())
print("Perimeter of Rectangle 1:", r1.perimeter())

print("Area of Rectangle 2:", r2.area())
print("Perimeter of Rectangle 2:", r2.perimeter())

if r1.area() > r2.area():
    print("Rectangle 1 has larger area")
elif r1.area() < r2.area():
    print("Rectangle 2 has larger area")
else:
    print("Both have equal area")

# OUTPUT:
# Area of Rectangle 1: 50
# Perimeter of Rectangle 1: 30
# Area of Rectangle 2: 48
# Perimeter of Rectangle 2: 28
# Rectangle 1 has larger area
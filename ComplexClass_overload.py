# QUESTION:
# Create a class Complex with private attributes real and imaginary parts.
# Overload '>=' operator to find the greatest number (compare using magnitude).

import math

class Complex:
    def __init__(self, real, imag):
        self.__real = real
        self.__imag = imag

    def magnitude(self):
        return math.sqrt(self.__real**2 + self.__imag**2)

    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()

    def __repr__(self):
        return f"{self.__real} + {self.__imag}i"


# Example
c1 = Complex(3, 4)   # magnitude = 5
c2 = Complex(1, 1)   # magnitude ≈ 1.41

print(c1 >= c2)  # True

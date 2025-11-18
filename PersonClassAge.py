# QUESTION:
# Create a class Person with private attributes name and age.
# Compare two Persons by their age.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __lt__(self, other):   # less than
        return self.__age < other.__age

    def __gt__(self, other):   # greater than
        return self.__age > other.__age

    def __repr__(self):
        return f"{self.__name} ({self.__age})"


# Example
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(p1 > p2)  # True
print(p1 < p2)  # False

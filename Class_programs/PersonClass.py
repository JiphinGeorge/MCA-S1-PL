# Create a class Person(name, age) with constructor and a method display().
# Create a class Employee(EmpID) from Person and override display() to include ID
# Create a derived class Faculty(department) from Employee and override display() to include the department.
# Create a class Researcher with method can_do_research() that returns a string indicating the person can conduct research.
# Create a class Professor inheriting from Faculty and Researcher.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, empID):
        super().__init__(name, age)
        self.empID = empID

    def display(self):
        super().display()
        print("Employee ID:", self.empID)


class Faculty(Employee):
    def __init__(self, name, age, empID, department):
        super().__init__(name, age, empID)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


class Researcher:
    def can_do_research(self):
        return "Can conduct research."


class Professor(Faculty, Researcher):
    def __init__(self, name, age, empID, department):
        Faculty.__init__(self, name, age, empID, department)


# Create object
p1 = Professor("Dr. Meera", 45, "EMP123", "Computer Science")

# Display details
p1.display()
print(p1.can_do_research())

# ------------------------------------------------------
# OUTPUT:
# Name: Dr. Meera
# Age: 45
# Employee ID: EMP123
# Department: Computer Science
# Can conduct research.
# ------------------------------------------------------
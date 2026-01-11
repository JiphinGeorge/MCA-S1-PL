# Create Person(name, phno), Dept(name, location).
# Employee(designation, salary) inherits both.
# Display details after 10% increment.

class Person:
    def __init__(self, name, phno):
        self.name = name
        self.phno = phno

class Dept:
    def __init__(self, dname, location):
        self.dname = dname
        self.location = location

class Employee(Person, Dept):
    def __init__(self, name, phno, dname, location, designation, salary):
        Person.__init__(self, name, phno)
        Dept.__init__(self, dname, location)
        self.designation = designation
        self.salary = salary

    def show(self):
        inc = self.salary + (self.salary * 0.10)
        print("Name:", self.name)
        print("Phone:", self.phno)
        print("Dept:", self.dname)
        print("Location:", self.location)
        print("Designation:", self.designation)
        print("New Salary:", inc)

emp = Employee("Bella", 9999999999, "CS", "Kochi", "Developer", 20000)
emp.show()

# OUTPUT:
# Name: Bella
# Phone: 9999999999
# Dept: CS
# Location: Kochi
# Designation: Developer
# New Salary: 22000.0
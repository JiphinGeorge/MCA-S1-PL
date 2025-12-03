# Employee from Person + Dept + 10% increment

class Person:
    def __init__(self, name, phno):
        self.name = name
        self.phno = phno

class Dept:
    def __init__(self, name, location):
        self.dept = name
        self.location = location

class Employee(Person, Dept):
    def __init__(self, name, phno, dept, location, desig, salary):
        Person.__init__(self, name, phno)
        Dept.__init__(self, dept, location)
        self.desig = desig
        self.salary = salary

    def increment(self):
        self.salary *= 1.10

    def display(self):
        print("\n--- EMPLOYEE DETAILS ---")
        print("Name:", self.name)
        print("Phone:", self.phno)
        print("Department:", self.dept)
        print("Location:", self.location)
        print("Designation:", self.desig)
        print("Updated Salary:", self.salary)


name = input("Name: ")
phno = input("Phone: ")
dept = input("Department: ")
loc = input("Location: ")
desig = input("Designation: ")
salary = float(input("Salary: "))

e = Employee(name, phno, dept, loc, desig, salary)
e.increment()
e.display()

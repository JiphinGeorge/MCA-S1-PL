# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"The name of the Person is {self.name}")
#         print(f"The age of the Person is {self.age}")
# class Employee(Person):
#     def
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")

# Faculty class derived from Person
class Faculty(Person):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

# Employee class derived from Person
class Employee(Person):
    def __init__(self, name, id, emp_id):
        super().__init__(name, id)
        self.emp_id = emp_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.emp_id}")

# Researcher class
class Researcher:
    def can_do_research(self):
        return "This person can conduct research."

# Professor class derived from Faculty and Researcher
class Professor(Faculty, Researcher):
    def __init__(self, name, id, department, emp_id):
        Faculty.__init__(self, name, id, department)
        Employee.__init__(self, name, id, emp_id)

    def display(self):
        super().display()
        print(self.can_do_research())

# Example usage
professor = Professor("Dr. Smith", "12345", "Computer Science", "6789")
professor.display()
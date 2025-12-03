# Student details: Person + Marks

class Person:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

class Marks:
    def __init__(self, maths, comp):
        self.maths = maths
        self.comp = comp

class Student(Person, Marks):
    def __init__(self, name, roll, maths, comp):
        Person.__init__(self, name, roll)
        Marks.__init__(self, maths, comp)

    def display(self):
        percent = (self.maths + self.comp) / 2
        print("\n--- STUDENT INFO ---")
        print(f"Name: {self.name}, Roll: {self.roll}")
        print(f"Maths: {self.maths}, Computer: {self.comp}")
        print(f"Percentage: {percent} -> {'PASS' if percent >= 50 else 'FAIL'}")


name = input("Name: ")
roll = input("Roll: ")
maths = int(input("Maths marks: "))
comp = int(input("Computer marks: "))

s = Student(name, roll, maths, comp)
s.display()


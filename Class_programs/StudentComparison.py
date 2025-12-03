# Compare two students based on percent

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

    def percent(self):
        return (self.maths + self.comp) / 2


def create_student():
    name = input("Name: ")
    roll = input("Roll: ")
    maths = int(input("Maths: "))
    comp = int(input("Computer: "))
    return Student(name, roll, maths, comp)


print("Enter Student 1:")
s1 = create_student()
print("\nEnter Student 2:")
s2 = create_student()

if s1.percent() > s2.percent():
    print(f"{s1.name} has a higher percentage.")
elif s2.percent() > s1.percent():
    print(f"{s2.name} has a higher percentage.")
else:
    print("Both have equal percentages.")

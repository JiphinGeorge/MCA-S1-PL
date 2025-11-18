# Create a class Flower(name).
# Add the attribute petalColor at runtime.
# If the flower has the attribute petalColor then display "<petalColor> <name>" else display "Unknown Flower".

class Flower:
    def __init__(self, name):
        self.name = name

    def set_color(self, color):
        self.petalColor = color

    def display(self):
        if hasattr(self, "petalColor"):
            print(f"{self.petalColor} {self.name}")
        else:
            print("Unknown Flower")

f = Flower("Rose")
f.set_color("Red")
f.display()

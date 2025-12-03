# Compare cuboids based on volume using <= operator

class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

class Cuboid(Rectangle):
    def __init__(self, l, b, h):
        super().__init__(l, b)
        self.h = h

    def volume(self):
        return self.l * self.b * self.h

    def __le__(self, other):
        return self.volume() <= other.volume()


def create_cuboid(n):
    print(f"\nEnter Cuboid {n} details:")
    l = int(input("Length: "))
    b = int(input("Breadth: "))
    h = int(input("Height: "))
    return Cuboid(l, b, h)


c1 = create_cuboid(1)
c2 = create_cuboid(2)

print("\nComparing volumes...")
if c1 <= c2:
    print("Cuboid 1 volume <= Cuboid 2 volume")
else:
    print("Cuboid 1 volume > Cuboid 2 volume")

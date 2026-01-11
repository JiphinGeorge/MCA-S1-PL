#(a) Check whether two collections are of the same length
a = list(map(int, input("Enter first list: ").split()))
b = list(map(int, input("Enter second list: ").split()))

if len(a) == len(b):
    print("Same length")
else:
    print("Different length")


#(b) Check whether sums are the same
if sum(a) == sum(b):
    print("Same sum")
else:
    print("Different sum")

#(c) Check whether any value occurs in both
common = set(a) and set(b)
if common:
    print("Common elements:", common)
else:
    print("No common elements")



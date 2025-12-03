# Recursive join with commas

def join_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + "," + join_recursive(lst[1:])

lst = input("Enter items: ").split()
print("Joined:", join_recursive(lst))

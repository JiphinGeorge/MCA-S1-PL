# Write a function which reverses each item in a list and return the new list.

def reverse_items(lst):
    return [item[::-1] for item in lst]

# Example
items = ["apple", "ball", "cat"]
result = reverse_items(items)

print(result)

# OUTPUT:
# ['elppa', 'llab', 'tac']


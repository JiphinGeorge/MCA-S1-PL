#4. Arrange characters in a string so that lowercase letters come first.
def reorder_string(s):
    lower = ''.join([c for c in s if c.islower()])
    upper = ''.join([c for c in s if c.isupper()])
    return lower + upper

print(reorder_string("PyTHon"))

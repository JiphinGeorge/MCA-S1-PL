#Check whether a given positive integer is a power of 2. Raise exception for negative input.
def is_power_of_two(n):
    if n < 0:
        raise ValueError("Negative input not allowed")
    return n != 0 and (n & (n - 1)) == 0

print(is_power_of_two(8))  
print(is_power_of_two(0)) 

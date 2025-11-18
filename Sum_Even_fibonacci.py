# Program to find the sum of even-valued terms in a Fibonacci series

def sum_even_fibonacci(n):
    a, b = 0, 1
    total = 0
    
    for _ in range(n):
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    
    return total

# Example: sum of even terms of first 11 Fibonacci numbers
print(sum_even_fibonacci(11))   # Output: 44

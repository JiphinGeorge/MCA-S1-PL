# Extract all odd numbers from an array

import numpy as np

arr = np.array(list(map(int, input("Enter numbers: ").split())))
print("Odd numbers:", arr[arr % 2 != 0])

# SAMPLE OUTPUT:
# Enter numbers: 1 2 3 4 5 6 7
# Odd numbers: [1 3 5 7]
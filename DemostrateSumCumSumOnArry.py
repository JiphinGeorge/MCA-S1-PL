# PROGRAM – 53
# Demonstrate sum(), cumsum(), max(), min() axis wise on a 2D array

import numpy as np

r = int(input("Rows: "))
c = int(input("Cols: "))

a = np.array(list(map(int, input().split()))).reshape(r, c)

print("sum axis 0:", a.sum(axis=0))
print("sum axis 1:", a.sum(axis=1))

print("cumsum axis 0:\n", a.cumsum(axis=0))

print("max axis 1:", a.max(axis=1))
print("min axis 1:", a.min(axis=1))

# Rows: 2
# Cols: 3
# 1 2 3 4 5 6

# sum axis 0: [5 7 9]
# sum axis 1: [ 6 15]

# cumsum axis 0:
#  [[ 1  2  3]
#  [ 5  7  9]]

# max axis 1: [3 6]
# min axis 1: [1 4]
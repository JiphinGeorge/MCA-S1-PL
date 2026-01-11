# PROGRAM – 52
# Demonstrate slicing operations on 2D and 3D arrays

import numpy as np

# 2D array
r = int(input("Rows: "))
c = int(input("Cols: "))
a = np.array(list(map(int, input().split()))).reshape(r, c)

print("2D slice a[0:2, 1:3]:")
print(a[0:2, 1:3])

# 3D array
b = np.arange(1, 28).reshape(3, 3, 3)

print("3D slice b[0, 1, :2]:")
print(b[0, 1, :2])

# Rows: 3
# Cols: 3
# 1 2 3 4 5 6 7 8 9
# 2D slice a[0:2, 1:3]:
# [[2 3]
#  [5 6]]

# 3D slice b[0, 1, :2]:
# [4 5]

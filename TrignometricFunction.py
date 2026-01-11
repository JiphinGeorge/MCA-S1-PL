# Perform element-wise sin, cos, tan on an array

import numpy as np

arr = np.array(list(map(float, input("Enter values: ").split())))

print("sin =", np.sin(arr))
print("cos =", np.cos(arr))
print("tan =", np.tan(arr))

# SAMPLE OUTPUT:
# Enter values: 0 1.57 3.14
# sin = [0.         0.99999968 0.        ]
# cos = [ 1.00000000e+00 -7.96326711e-04 -1.00000000e+00]
# tan = [ 0.00000000e+00 -1.25542733e+03 -1.22464680e-16]
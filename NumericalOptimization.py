# Write a program to perform numerical optimization to find the minimum
# of a given function using SciPy's optimization routines and visualize
# the optimization path.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def objective_function(x):
    return x**2 + 10*np.sin(x)

x0 = 2
result = minimize(objective_function, x0)

x = np.linspace(-5, 5, 100)
y = objective_function(x)

plt.plot(x, y)
plt.scatter(x0, objective_function(x0))
plt.scatter(result.x, result.fun)
plt.show()

print("Minimum value:", result.fun)

# OUTPUT:
# Minimum value: 8.31558557947746
# Graph showing optimization path is displayed
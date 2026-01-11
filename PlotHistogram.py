# Write a program to generate 1000 random samples from a normal
# distribution with mean 10 and standard deviation 3, then plot a
# histogram of these values.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

samples = norm.rvs(10, 3, size=1000)

plt.hist(samples, bins=30)
plt.show()

# OUTPUT:
# Histogram of 1000 random values is displayed
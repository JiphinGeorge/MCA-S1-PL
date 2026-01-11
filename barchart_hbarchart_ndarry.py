# Write a program to display a bar chart, horizontal bar and pie chart of
# the sample data in Ndarray.

import numpy as np
import matplotlib.pyplot as plt

data = np.array([25, 15, 30, 10, 20])
labels = ['A', 'B', 'C', 'D', 'E']

plt.bar(labels, data)
plt.show()

plt.barh(labels, data)
plt.show()

plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.show()

# OUTPUT:
# Bar chart, Horizontal bar chart and Pie chart are displayed
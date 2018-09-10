import numpy as np
import matplotlib.pyplot as plt

data = np.arange(100, 201)
plt.plot(data)

"""
A figure can be understood as a graphics window. matplotlib.pyplot 
will have a default figure, and we can also create more by plt.figure(), as shown below:
"""

data2 = np.arange(200, 301)
plt.figure()
plt.plot(data2)

plt.show()  # draws two windows, each of which is a line graph with a different interval
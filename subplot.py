import numpy as np
import matplotlib.pyplot as plt

"""
In some cases, we want to display multiple graphics in the same window. At this point, you can use multiple subplots,
like below:
"""

data = np.arange(100, 201)
plt.subplot(2, 1, 1)
plt.plot(data)

data2 = np.arange(200, 301)
plt.subplot(2, 1, 2)
plt.plot(data2)

plt.show()

"""
The first two parameters of the subplot function specify the number of subplots. Thus the current graph will be divided 
in the form of matrix, and the two parameters, which are integers, specify the number of rows and columns of the matrix 
respectively. The third parameter refers to the index in the matrix. Therefore, the following code refers to the first 
subplot in the 2-row and 1-column subplots.

plt.subplot(2, 1, 1)

The following code refers to the second subplot in the 2-row and 1-column subplots.

plt.subplot(2, 1, 2)

The parameters of the subplot function not only support the above form, but also can combine three integers (within 10)
 into one integer. For example: 2, 1, 1 can be written as 211, and 2, 1, 2 can be written as 212.
"""

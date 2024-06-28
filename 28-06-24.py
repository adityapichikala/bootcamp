'''
Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

Matplotlib was created by John D. Hunter.

Matplotlib is open source and we can use it freely.

'''


'''
for installing matplotlib

pip instll matplotlib

'''


'''

A linear equation in two variables (say, x and y) can be represented as y = mx + c, where m is the slope of the line, and c is the y-intercept. Let's plot a simple linear equation using Matplotlib and NumPy.

'''
import numpy as np

import matplotlib.pyplot as plt


x = np.linspace(start=-10, stop=10, num=400)

print(x)

m = 2  # Slope
c = 3  # Intercept
y = m * x + c

plt.plot(x, y, label='y = 2x + 3')
plt.title('Plot of the Linear Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,10) # Lower Limit, Upper Limit
plt.ylim(0,20) # Lower Limit, Upper Limit
plt.grid(True)
plt.legend()
plt.savefig('linear-equation.png')
plt.show()
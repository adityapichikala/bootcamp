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

'''
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

'''
'''
# Define the coefficients
a = 1
b = -4
c = 4

# Generate x values
x = np.linspace(-1, 7, 400)

# Calculate y values using the quadratic equation
y = a * x**2 + b * x + c

# Create the plot
plt.plot(x, y, label='y = x^2 - 4x + 4')

# Adding title and labels
plt.title('Plot of the Quadratic Equation')
plt.xlabel('x')
plt.ylabel('y')

plt.xlim(-5,10)
plt.ylim(0,30)

plt.legend()
# Add grid
plt.grid(True)

# Show the plot
plt.show()

'''


'''
# Create a figure object
fig = plt.figure()

# Add axes to the figure (left, bottom, width, height)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Display the figure
plt.show()
'''

'''
# Creating an array of x values
x = np.linspace(0, 10, 100)
# Calculating y values based on x
y = np.sin(x)

# Create a new figure with a specific size
fig = plt.figure(figsize=(8, 6))

# Add an axes to the figure
# The list [left, bottom, width, height] defines the dimensions of the axes within the figure
ax = fig.add_axes([0.1, 0.1, 0.85, 0.85])

# Plot data on the axes
ax.plot(x, y, label='sin(x)', color='green')

# Set the title of the plot
ax.set_title('Simple Plot of sin(x)')
ax.legend()
# Set the x and y axis labels
ax.set_xlabel('x')
ax.set_ylabel('Amplitude')

# Display the figure
plt.show()
'''

'''
**Overview**:

When creating visualizations in Matplotlib, the figure serves as a canvas where multiple plots (axes) can be arranged in various positions. Each set of axes can display different aspects or components of data. For linear functions, these plots might represent different linear equations or variations thereof.

**Key Components**:

* Figure: The entire window or the canvas for the plots.

* Axes: The individual plots; each set of axes can contain its own elements like lines, labels, ticks, and titles.

**Configuring Multiple Axes**:

To position axes, use *fig.add_axes()* with the format [left, bottom, width, height] where each value is a fraction of the figure dimensions:

* left, bottom: These determine the position of the bottom-left corner of the axes.
* width, height: These determine the size of the axes.

**Example Code for Linear Functions in Different Axes Positions**:

This example demonstrates how to arrange six different axes within a single figure, each displaying a simple linear function with a different slope and intercept, organized in various positions.

'''
'''
# Generate x values
x = np.linspace(0, 10, 100)

# Create a blank canvas
fig = plt.figure(figsize=(10, 8))


# Center plot - main plot
axes_center = fig.add_axes([0.3, 0.3, 0.4, 0.4])  # left, bottom, width, height
axes_center.plot(x, x + 1)  # y = x + 1
axes_center.set_title('Center Plot: y = x + 1')

# Top plot - summary
axes_top = fig.add_axes([0.3, 0.75, 0.4, 0.2])
axes_top.plot(x, 2*x + 1)  # y = 2x + 1
axes_top.set_title('Top Plot: y = 2x + 1')

# Right plot - auxiliary data
axes_right = fig.add_axes([0.75, 0.3, 0.2, 0.4])
axes_right.plot(x, 0.5*x + 1)  # y = 0.5x + 1
axes_right.set_title('Right Plot: y = 0.5x + 1')

# Left plot - contextual information
axes_left = fig.add_axes([0.05, 0.3, 0.2, 0.4])
axes_left.plot(x, 3*x + 1)  # y = 3x + 1
axes_left.set_title('Left Plot: y = 3x + 1')

# Bottom plot - comparative data
axes_bottom = fig.add_axes([0.3, 0.05, 0.4, 0.2])
axes_bottom.plot(x, -x + 1)  # y = -x + 1
axes_bottom.set_title('Bottom Plot: y = -x + 1')

# Top Right Corner plot - highlight
axes_top_right = fig.add_axes([0.75, 0.75, 0.2, 0.2])
axes_top_right.plot(x, 4*x + 1)  # y = 4x + 1
axes_top_right.set_title('Top Right Plot: y = 4x + 1')

plt.show()
'''



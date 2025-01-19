"""
This is code for applying gradient descent and graphing it.

The equation I have started with is: y = x**3 - 4*x
The derivative of this equation is dy/dx = 3(x**2) - 4
I started with initial x value of 6, and learning rate as 0.01
"""

import numpy as np
import matplotlib.pyplot as plt

# Gradient Descent
x=6
learning_rate=0.01
x_s= np.array([])
for i in range(100):
    dy_dx = 3*(x**2) - 4
    x -= learning_rate*dy_dx
    x_s = np.append(x_s, x)

# Graphing the curve and the x's that gradient descent went through
curve_x = np.array([-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
curve_y = curve_x**3 - 4*curve_x
y_s = x_s**3 - 4*x_s
plt.plot(curve_x, curve_y)
plt.scatter(x_s, y_s, s=10)

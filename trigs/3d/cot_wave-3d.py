import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = 1 / np.tan(np.sqrt(X**2 + Y**2))

# Create a 3D plot for the cotangent function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='cividis')
ax.set_title('3D Cotangent Function')

# Show the plot
plt.show()

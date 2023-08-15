import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z_sin = np.sin(np.sqrt(X**2 + Y**2))
Z_cos = np.cos(np.sqrt(X**2 + Y**2))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surfaces for sine and cosine
surf_sin = ax.plot_surface(X, Y, Z_sin, cmap='Reds')
surf_cos = ax.plot_surface(X, Y, Z_cos, cmap='Blues')

# Add labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = 1 / np.sin(np.sqrt(X**2 + Y**2))

# Create a 3D plot for the cosecant function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='plasma')
ax.set_title('3D Cosecant Function')

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the dimensions of the grid
x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 50)
z = np.linspace(0, 5, 20)

# Create a meshgrid
X, Y, Z = np.meshgrid(x, y, z)

# Simulate fluid flow values using a mathematical formula
""" 
    simplified representation used for generating the fluid flow values in the context
    of creating a visual example. It doesn't necessarily represent a physical phenomenon
    accurately but rather combines trigonometric and exponential functions to demonstrate 
    a varying pattern of fluid flow values in a 3D porous media visualization.

    np.sin(X) and np.cos(Y): 
            these components introduce oscillations in the x and y directions, contributing to
            the variation of fluid flow values across the porous media.

    np.exp(-Z/5): 
            this component introduces an exponential decay along the z direction. As Z increases,
            the exponential term becomes smaller, resulting in decreasing fluid flow values as you
            move deeper into the porous media. The division by 5 (-Z/5) controls the rate of decay.
"""
fluid_flow = np.sin(X) * np.cos(Y) * np.exp(-Z / 5)

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Plot the fluid flow
"""
surface: 
    This variable will store the plot surface object that represents the 3D visualization of the fluid flow.
    
ax: 
    This is the 3D subplot created using fig.add_subplot(111, projection='3d'). It's the axis object on which we're going to plot the surface.

plot_surface: 
    This is a function provided by mpl_toolkits.mplot3d that is used to plot a 3D surface plot.

X[:,:,0], Y[:,:,0], Z[:,:,0]: 
    These slices select the 2D arrays from the 3D meshgrid arrays X, Y, and Z at a specific z-coordinate (in this case, 0). This effectively creates 2D grids representing the x, y, and z coordinates for the surface plot.

facecolors=plt.cm.plasma(fluid_flow[:,:,0]): 
    This sets the color of the surfaces based on the fluid_flow values at the chosen z-coordinate (0 in this case). The plt.cm.plasma colormap is used to map fluid flow values to colors, creating a visually appealing effect.

rstride=1 and cstride=1: 
    These parameters control the step size when sampling the grid to generate the surface. A value of 1 means that every point in the grid will be used.

alpha=0.8: 
    This parameter sets the transparency of the plotted surface, making it slightly transparent (alpha value of 0.8) so that underlying structures are partially visible.
"""
surface = ax.plot_surface(
    X[:, :, 0],
    Y[:, :, 0],
    Z[:, :, 0],
    facecolors=plt.cm.plasma(fluid_flow[:, :, 0]),
    rstride=1,
    cstride=1,
    alpha=0.8,
)

# Add color bar
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

# Set labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Fluid Flow in Porous Media")

# Show the plot
plt.show()

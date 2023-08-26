# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define spherical coordinates
theta = np.linspace(0, np.pi, 100)  # Generate an array of theta values
phi = np.linspace(0, 2 * np.pi, 100)  # Generate an array of phi values
theta, phi = np.meshgrid(theta, phi)  # Create a 2D grid of theta and phi values

# Hydrogen atom probability density function (1s orbital)
a0 = 1.0  # Bohr radius
r = 2 * a0  # Distance from nucleus (arbitrary for visualization)
psi_1s = (1 / np.sqrt(np.pi * a0**3)) * np.exp(-r / a0)  # Calculate the 1s orbital wavefunction

# Convert spherical to Cartesian coordinates
x = r * np.sin(theta) * np.cos(phi)  # Convert spherical coordinates to x
y = r * np.sin(theta) * np.sin(phi)  # Convert spherical coordinates to y
z = r * np.cos(theta)  # Convert spherical coordinates to z

# Create a colormap based on phi (azimuthal angle)
colors = phi

# Create the figure and 3D axis
fig = plt.figure()  # Create a new figure
ax = fig.add_subplot(111, projection='3d')  # Add a 3D subplot to the figure

# Scatter plot with colormap
sc = ax.scatter(x, y, z, c=colors, cmap='hsv', marker='o', s=10)  # Create a scatter plot with varying colors
fig.colorbar(sc, label="Azimuthal Angle")  # Add a colorbar to the figure to indicate color mapping

# Set labels and title
ax.set_title("Hydrogen Atom - Electron Cloud (1s Orbital)")  # Set the title of the plot
ax.set_xlabel("X")  # Set label for the x-axis
ax.set_ylabel("Y")  # Set label for the y-axis
ax.set_zlabel("Z")  # Set label for the z-axis

# Display the plot
plt.show()  # Display the 3D plot of the hydrogen atom's electron cloud

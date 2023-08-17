import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

""" Define constants for the graph 
    x_min and x_max: 
    These constants define the minimum and maximum values for the x-coordinate. 
    The x-coordinate represents the horizontal position in the 2D plane where the 
    wavefunction will be plotted. By setting these values, you're specifying the 
    range of x-values that the wavefunction will cover horizontally.
    
    y_min and y_max: 
    Similar to x_min and x_max, these constants define the minimum and maximum 
    values for the y-coordinate. The y-coordinate represents the vertical position 
    in the 2D plane where the wavefunction will be plotted. By setting these values, 
    you're specifying the range of y-values that the wavefunction will cover vertically.
    
    num_points: This constant determines the number of points along each dimension (x and y) 
    that will be used to create the grid for plotting the wavefunction. The larger the value 
    of num_points, the more detailed and fine-grained the plot will be, as it will have more 
    data points to represent the wavefunction. However, a larger value of num_points might also
    increase computation time and memory usage. 
"""

x_min = -5
x_max = 5
y_min = -5
y_max = 5
num_points = 100

"""  Create a grid of x and y values 
     x = np.linspace(x_min, x_max, num_points): 
     This line generates an array of num_points equally spaced values between x_min and x_max. 
     These values will represent the x-coordinates along the horizontal axis of the 2D plane.
     
     y = np.linspace(y_min, y_max, num_points): 
     Similar to the previous line, this line generates an array of num_points equally spaced 
     values between y_min and y_max. These values will represent the y-coordinates along the 
     vertical axis of the 2D plane.
     
     X, Y = np.meshgrid(x, y): 
     This line uses the meshgrid function from NumPy to create a 2D grid of coordinates. It 
     takes the arrays x and y created in the previous steps and generates two 2D arrays, X and Y, 
     where each combination of X[i, j] and Y[i, j] represents a specific point in the 2D plane. The
     arrays X and Y collectively define a grid of points where the 2D wavefunction will be evaluated.
"""

x = np.linspace(x_min, x_max, num_points)
y = np.linspace(y_min, y_max, num_points)
X, Y = np.meshgrid(x, y)


""" Define a function for the 2D wavefunction 
    Calculates a 2D wavefunction in a quantum system. The function takes several parameters that define
    the quantum state and the properties of the system, and it returns the value of the 2D wavefunction 
    at a given point (x, y).
"""


def psi_2d(x, y, nx, ny, Lx, Ly):
    """
    2 / Ly:
        This part calculates the ratio of 2 divided by the length of the box in the y-direction, represented by Ly.
        This ratio is used to normalize the wavefunction, ensuring that the total probability over all positions is
        equal to 1. It's a normalization factor.

    np.sqrt(2 / Ly):
        This takes the square root of the above result. Taking the square root maintains the normalization
        and ensures that the wavefunction's overall intensity is properly scaled.

    ny * np.pi * y / Ly:
        This part involves the quantum number ny, the constant π (pi), the y-coordinate y, and the box length Ly.
        It represents the argument of the sine function and determines the oscillatory behavior of the wavefunction
        along the y-axis.

    np.sin(ny * np.pi * y / Ly):
        This calculates the sine of the argument calculated in the previous step. The sine function generates
        oscillations that represent the spatial behavior of the wavefunction along the y-axis. The quantum number
        ny determines the number of nodes or oscillations in the wavefunction.
    """

    psi_x = np.sqrt(2 / Lx) * np.sin(nx * np.pi * x / Lx)
    psi_y = np.sqrt(2 / Ly) * np.sin(ny * np.pi * y / Ly)

    """
    2 / Ly:                         
            This part calculates the ratio of 2 divided by the length of the box in the y-direction, represented by Ly. 
            This ratio is used to normalize the wavefunction, ensuring that the total probability over all positions is 
            equal to 1. It's a normalization factor.
    
    np.sqrt(2 / Ly):                
            This takes the square root of the above result. Taking the square root maintains the normalization 
            and ensures that the wavefunction's overall intensity is properly scaled.
    
    ny * np.pi * y / Ly:
            This part involves the quantum number ny, the constant π (pi), the y-coordinate y, and the box length Ly. 
            It represents the argument of the sine function and determines the oscillatory behavior of the wavefunction 
            along the y-axis.
    
    np.sin(ny * np.pi * y / Ly):    
            This calculates the sine of the argument calculated in the previous step. The sine function generates 
            oscillations that represent the spatial behavior of the wavefunction along the y-axis. The quantum number
            ny determines the number of nodes or oscillations in the wavefunction.
    """

    # Return the combined 2D wavefunction
    return psi_x * psi_y


# Quantum numbers and box dimensions
""" 
nx: 
    This variable represents the quantum number associated with the x-direction. 
    Quantum numbers are integers that describe different aspects of a quantum system. 
    In the context of the provided code, nx is used to determine the number of nodes (oscillations) 
    along the x-axis of the wavefunction. The value of nx influences how many times the wavefunction
    oscillates within the specified box length Lx.

ny: 
    Similar to nx, this variable represents the quantum number associated with the y-direction.
    It determines the number of nodes (oscillations) along the y-axis of the wavefunction. The 
    value of ny affects how many times the wavefunction oscillates within the specified box length Ly.

Lx: 
    This variable represents the length of the box in the x-direction. 
    In the context of the provided code, it defines the spatial extent of the region where the wavefunction
    is being calculated and plotted along the x-axis.

Ly: 
    Similar to Lx, this variable represents the length of the box in the y-direction. It defines the spatial 
    extent of the region where the wavefunction is being calculated and plotted along the y-axis.
"""
nx = 2
ny = 2
Lx = 10
Ly = 10

# Calculate the 2D wavefunction values
Z = psi_2d(X, Y, nx, ny, Lx, Ly)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Plot the 3D wavefunction as a surface plot
surf = ax.plot_surface(X, Y, Z, cmap="viridis")

# Add labels and title
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Wavefunction")
ax.set_title("3D Quantum Mechanical Wavefunction")

# Add colorbar to indicate wavefunction values
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Show the plot
plt.show()

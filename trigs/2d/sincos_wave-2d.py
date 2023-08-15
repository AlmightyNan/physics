import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 10, 1000)
y = np.sin(x)
y2 = np.cos(x)  # Another sine wave for comparison

# Create a 2D plot
plt.figure()

# Plot the sine waves
plt.plot(x, y, color='red', label='sin(x)')
plt.plot(x, y2, color='blue', label='sin(2x)')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sine Waves')
plt.legend()

# Show the plot
plt.show()

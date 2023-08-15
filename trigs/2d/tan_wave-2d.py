import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2*np.pi, 1000)
y = np.tan(x)

# Create a 2D plot for the tangent function
plt.figure()
plt.plot(x, y, color='green')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Tangent Function')
plt.ylim(-5, 5)  # Set y-axis limits due to asymptotes
plt.show()

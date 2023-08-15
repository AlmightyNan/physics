import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2*np.pi, 1000)
y = 1 / np.tan(x)

# Create a 2D plot for the cotangent function
plt.figure()
plt.plot(x, y, color='purple')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cotangent Function')
plt.ylim(-5, 5)  # Set y-axis limits due to asymptotes
plt.show()

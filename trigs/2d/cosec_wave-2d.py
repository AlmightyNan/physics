import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2*np.pi, 1000)
y = 1 / np.sin(x)

# Create a 2D plot for the cosecant function
plt.figure()
plt.plot(x, y, color='orange')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cosecant Function')
plt.ylim(-5, 5)  # Set y-axis limits due to asymptotes
plt.show()

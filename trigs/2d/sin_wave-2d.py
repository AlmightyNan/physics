import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

# Create a 2D plot for the sine function
plt.figure()
plt.plot(x, y, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sine Function')
plt.show()

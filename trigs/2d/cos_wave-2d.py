import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2*np.pi, 1000)
y = np.cos(x)

# Create a 2D plot for the cosine function
plt.figure()
plt.plot(x, y, color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cosine Function')
plt.show()

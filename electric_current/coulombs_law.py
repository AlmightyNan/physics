import matplotlib.pyplot as plt
import numpy as np

# Coulomb's Law: Force vs. Distance
k = 8.99e9  # Coulomb's constant in N m^2 / C^2
q1 = 1e-9   # Charge 1 in coulombs
q2 = 1e-9   # Charge 2 in coulombs
r = np.linspace(1, 10, 100)  # Separation distance in meters

# Calculate the force between charges using Coulomb's Law
force = k * q1 * q2 / r**2

plt.figure()
plt.plot(r, force)
plt.xlabel('Separation Distance (m)')
plt.ylabel('Force (N)')
plt.title("Coulomb's Law: Force vs. Distance")
plt.grid(True)
plt.show()

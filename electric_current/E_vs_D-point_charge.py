import matplotlib.pyplot as plt
import numpy as np

# Electric Field vs. Distance from a Point Charge
k = 8.99e9  # Coulomb's constant in N m^2 / C^2
q = 1e-9    # Charge in coulombs
r = np.linspace(0.1, 10, 100)  # Distance from the charge in meters

# Calculate electric field strength using E = k * q / r^2
electric_field = k * q / r**2

plt.figure()
plt.plot(r, electric_field)
plt.xlabel('Distance from Charge (m)')
plt.ylabel('Electric Field (N/C)')
plt.title('Electric Field vs. Distance from a Point Charge')
plt.grid(True)
plt.show()

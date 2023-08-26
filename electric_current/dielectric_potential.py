import matplotlib.pyplot as plt
import numpy as np

# Dielectric Material Polarization in an Electric Field
E = np.linspace(0, 10000, 100)  # Electric field strength in N/C
P = 0.8 * E                     # Polarization of the material

plt.figure()
plt.plot(E, P)
plt.xlabel('Electric Field (N/C)')
plt.ylabel('Polarization (C/m^2)')
plt.title('Dielectric Material Polarization in an Electric Field')
plt.grid(True)
plt.show()

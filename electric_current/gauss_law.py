import matplotlib.pyplot as plt
import numpy as np

# Gauss's Law: Electric Flux vs. Enclosed Charge
Q = np.linspace(0, 10, 100)  # Enclosed charge values
flux = Q  # Electric flux calculated (for simplicity)

plt.figure()
plt.plot(Q, flux)
plt.xlabel('Enclosed Charge (C)')
plt.ylabel('Electric Flux')
plt.title("Gauss's Law: Electric Flux vs. Enclosed Charge")
plt.grid(True)
plt.show()

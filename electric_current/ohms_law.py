import matplotlib.pyplot as plt
import numpy as np

# Ohm's Law: Voltage vs. Current
R = 10  # Resistance in ohms
I = np.linspace(0, 5, 100)  # Current values
V = R * I  # Voltage calculated from Ohm's Law

plt.figure()
plt.plot(I, V)
plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.title("Ohm's Law: Voltage vs. Current")
plt.grid(True)
plt.show()

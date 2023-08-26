import matplotlib.pyplot as plt
import numpy as np

# RC Circuit Charging: Voltage across Capacitor vs. Time
R_charge = 1000   # Resistance in ohms
C_charge = 0.001  # Capacitance in farads
t = np.linspace(0, 5, 200)  # Time values

# Calculate voltage across the capacitor during charging
V_charge = (1 - np.exp(-t / (R_charge * C_charge))) * 5

plt.figure()
plt.plot(t, V_charge)
plt.xlabel('Time (s)')
plt.ylabel('Voltage across Capacitor (V)')
plt.title('RC Circuit Charging: Voltage across Capacitor vs. Time')
plt.grid(True)
plt.show()

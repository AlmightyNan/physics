import matplotlib.pyplot as plt
import numpy as np

# Series and Parallel Circuits: Voltage-Current Characteristics
R1 = 10   # Resistance 1 in ohms
R2 = 20   # Resistance 2 in ohms
V = 5     # Applied voltage in volts
I_series = V / (R1 + R2)   # Total current in series circuit
I_parallel = V / R1        # Total current in parallel circuit

I_range = np.linspace(0, 0.5, 100)  # Current values for the plot
V_series = I_range * (R1 + R2)      # Voltage in series circuit
V_parallel = V                      # Voltage in parallel circuit

plt.figure()
plt.plot(I_range, V_series, label='Series Circuit')
plt.plot(I_range, V_parallel * np.ones_like(I_range), label='Parallel Circuit')
plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.title('Series and Parallel Circuits: Voltage-Current Characteristics')
plt.legend()
plt.grid(True)
plt.show()

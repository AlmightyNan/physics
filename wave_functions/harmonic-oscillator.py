import numpy as np  # Import the numpy library for numerical operations
import matplotlib.pyplot as plt  # Import the pyplot module for plotting

# Generate an array of x values from -3 to 3 with 500 points
x = np.linspace(-3, 3, 500)

# Calculate the ground state wave function of a harmonic oscillator
# The wave function is given by psi_harmonic = (1 / sqrt(pi))^0.25 * e^(-x^2 / 2)
psi_harmonic = (1 / np.pi) ** 0.25 * np.exp(-x**2 / 2)

# Create a plot of the harmonic oscillator wave function
plt.plot(x, psi_harmonic)  # Plot x values against the calculated wave function values
plt.title("Harmonic Oscillator - Ground State")  # Set the plot's title
plt.xlabel("Position")  # Set the label for the x-axis
plt.ylabel("Wavefunction")  # Set the label for the y-axis
plt.show()  # Display the plot

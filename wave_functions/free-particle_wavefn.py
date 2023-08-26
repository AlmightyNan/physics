import numpy as np  # Import the numpy library for numerical operations
import matplotlib.pyplot as plt  # Import the pyplot module for plotting

# Generate an array of x values from -5 to 5 with 500 points
x = np.linspace(-5, 5, 500)

# Set wave number and standard deviation parameters
k0 = 1.0  # Wave number
sigma = 0.5  # Standard deviation

# Calculate the free particle wave function (Gaussian wave packet)
# The wave function is given by psi_free = exp(-0.5 * ((x - 2) / sigma)^2) * exp(1j * k0 * x)
psi_free = np.exp(-0.5 * ((x - 2) / sigma)**2) * np.exp(1j * k0 * x)

# Plot the real and imaginary parts of the wave function
plt.plot(x, np.real(psi_free), label="Real part")  # Plot real part of the wave function
plt.plot(x, np.imag(psi_free), label="Imaginary part")  # Plot imaginary part of the wave function

# Customize the plot
plt.title("Free Particle Wave Packet")  # Set the plot's title
plt.xlabel("Position")  # Set the label for the x-axis
plt.ylabel("Wavefunction")  # Set the label for the y-axis
plt.legend()  # Display legend to differentiate real and imaginary parts
plt.show()  # Display the plot

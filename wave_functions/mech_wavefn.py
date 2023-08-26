import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
L: 
    - Length of the Domain
    - This parameter represents the length of the spatial domain in which the quantum mechanical
      wavefunction is being simulated. It defines the range of x-values that the wavefunction covers.

num_points: 
    - Number of Spatial Points
    - The num_points parameter specifies the number of spatial points used to discretize the x-axis. 
      More points allow for a more detailed representation of the wavefunction but might increase computation time.

num_frames: 
    - Number of Animation Frames
    - This parameter determines the number of animation frames used to visualize the time evolution of the quantum 
      wavefunction. It specifies how many steps the animation will take.

dt: 
    - Time Step
    - dt represents the time step used in the simulation to compute the time evolution of the wavefunction. A smaller time
      step provides more accuracy but may increase computation time.

hbar: 
    - Reduced Planck's Constant
    - The parameter hbar is the reduced Planck's constant, which is a fundamental constant in quantum mechanics. It scales the
      quantum mechanical effects in the simulation.
"""

L = 10
num_points = 500
num_frames = 100
dt = 0.01
hbar = 1.0

"""
in the following line, x generates an array of equally spaced points along the x-axis, which represents the spatial domain. 
The np.linspace function creates num_points points between 0 and L (inclusive) and stores them in the array x.

dx calculates the spacing (dx) between consecutive grid points in the x array. The difference between the second element (x[1])
and the first element (x[0]) of the array x gives the spacing between adjacent grid points.
"""
x = np.linspace(0, L, num_points)
dx = x[1] - x[0]

"""
x0: 
    - calculates the initial position (x0) of the center of the Gaussian wave packet. 
    - It's set to one-third of the length of the domain L.

sigma:
    - calculates the standard deviation (sigma) of the Gaussian wave packet. It's set to 20%
      of the length of the domain L. The value of sigma determines the width of the Gaussian distribution, which affects the spatial extent of the wave packet.

psi_0:
    - This line calculates the initial wavefunction psi_0 based on a Gaussian wave packet with a phase factor. 
      The expression is a combination of two parts:
            - np.exp(-((x - x0) ** 2) / (2 * sigma**2)) calculates the Gaussian envelope of the wave packet. It represents the spatial distribution of the wave packet along the x-axis.
            - np.exp(1j * 0.5 * x) introduces a complex phase factor that imparts a spatially varying phase to the wavefunction. This factor can create oscillatory behavior.
"""
x0 = L / 3
sigma = 0.2 * L
psi_0 = np.exp(-((x - x0) ** 2) / (2 * sigma**2)) * np.exp(1j * 0.5 * x)


"""
k = np.fft.fftfreq(num_points, dx) * 2 * np.pi:
   - This line calculates the array of wave numbers `k` using the Fourier transform. The function `np.fft.fftfreq` generates an array of frequency values corresponding to the Fourier transform of discrete data. By multiplying it with `2 * np.pi`, you're converting frequencies to wave numbers, which are crucial in quantum mechanics.

psi_k = np.fft.fft(psi):
   - This line calculates the Fourier transform of the input wavefunction `psi` using `np.fft.fft`. The Fourier transform decomposes the wavefunction into its frequency components.

psi_k *= np.exp(-0.5j * hbar * k**2 * dt):
   - This line applies the kinetic operator to the frequency components of the wavefunction. The kinetic operator is associated with the energy of a quantum system and is represented by the term involving `k` in the exponential. By multiplying `psi_k` by this exponential term, you're simulating the time evolution due to the kinetic energy component.

psi_new = np.fft.ifft(psi_k):
   - This line calculates the inverse Fourier transform of the modified frequency components `psi_k` to obtain the updated wavefunction in the position space.
"""


def time_evolution(psi, dt):
    k = np.fft.fftfreq(num_points, dx) * 2 * np.pi  # Wave numbers
    psi_k = np.fft.fft(psi)
    psi_k *= np.exp(-0.5j * hbar * k**2 * dt)  # Applying the kinetic operator
    psi_new = np.fft.ifft(psi_k)
    return psi_new


# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(-1, 1)
ax.set_xlabel("Position")
ax.set_ylabel("Real(Psi)")
ax.set_title("Time Evolution of Quantum Wavefunction")

# Plot the real part of the wave function
(line,) = ax.plot(x, np.real(psi_0))


# Animation update function
def animate(frame):
    global psi_0
    psi_0 = time_evolution(psi_0, dt)
    line.set_ydata(np.real(psi_0))
    ax.set_title(f"Frame {frame}/{num_frames}")
    return (line,)


# Create the animation
animation = FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

plt.show()

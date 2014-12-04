#
# A simple fft demonstration
#
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np

# Number of samplepoints
Samples = 600
# Time between each sample
T = 1.0 / 800.0

# x from 0 to 600, with a spacing of 0,75.
x = np.linspace(0.0, Samples*T, Samples)

# The function y consists of three sine waves. One of 50, one of 80 and one of 120 [Hz].
# omega = 2*pi*f
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x) + 0.25*np.sin(120 * 2.0*np.pi*x)

# Plot the source function
plt.plot(x, y)
plt.grid()
plt.show()

# Compute the FFT.
yfft = fft(y)
xfft = np.linspace(0.0, 1.0/(2.0*T), Samples/2)

# Plot the result of the FFT
plt.plot(xfft, 2.0/Samples * np.abs(yfft[0:Samples/2]))
plt.grid()
plt.show()
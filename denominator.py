import numpy as np
import matplotlib.pyplot as plt

# Define the function
n_values = np.arange(1, 10000, 1)  # n from 1 to a very large number
sin_n_squared = np.sin(n_values)**2

# Calculate n^2 * sin^2(n) and n^3 * sin^2(n)
n2_sin2 = n_values**2 * sin_n_squared
n3_sin2 = n_values**3 * sin_n_squared

# Calculate the cumulative sum (sum of n^2 * sin^2(n) and n^3 * sin^2(n) over n)
sum_n2_sin2 = np.cumsum(n2_sin2)
sum_n3_sin2 = np.cumsum(n3_sin2)

# Plotting
plt.figure(figsize=(14, 10))

# Plot n^2 * sin^2(n)
plt.subplot(2, 2, 1)
plt.plot(n_values, n2_sin2, label=r'$n^2 \cdot \sin^2(n)$', color='orange')
plt.title(r'$n^2 \cdot \sin^2(n)$')
plt.xlabel('n')
plt.ylabel(r'$n^2 \cdot \sin^2(n)$')
plt.grid(True)
plt.legend()

# Plot n^3 * sin^2(n)
plt.subplot(2, 2, 2)
plt.plot(n_values, n3_sin2, label=r'$n^3 \cdot \sin^2(n)$', color='orange')
plt.title(r'$n^3 \cdot \sin^2(n)$')
plt.xlabel('n')
plt.ylabel(r'$n^3 \cdot \sin^2(n)$')
plt.grid(True)
plt.legend()

# Plot cumulative sum of n^2 * sin^2(n)
plt.subplot(2, 2, 3)
plt.plot(n_values, sum_n2_sin2, label=r'$\sum n^2 \cdot \sin^2(n)$', color='orange')
plt.title(r'$\sum n^2 \cdot \sin^2(n)$')
plt.xlabel('n')
plt.ylabel(r'Cumulative Sum')
plt.grid(True)
plt.legend()

# Plot cumulative sum of n^3 * sin^2(n)
plt.subplot(2, 2, 4)
plt.plot(n_values, sum_n3_sin2, label=r'$\sum n^3 \cdot \sin^2(n)$', color='orange')
plt.title(r'$\sum n^3 \cdot \sin^2(n)$')
plt.xlabel('n')
plt.ylabel(r'Cumulative Sum')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('plot.png')


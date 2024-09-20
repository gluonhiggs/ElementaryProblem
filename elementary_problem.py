import numpy as np
import matplotlib.pyplot as plt

# Define the function
n_values = np.arange(1, 100000, 1)  # n from 1 to a very large number
sin_n_squared = np.sin(n_values)**2

# Calculate 1/(n^3 * sin^2(n)) and 1/(n^2 * sin^2(n))
term_A = 1 / (n_values**3 * sin_n_squared)
term_B = 1 / (n_values**2 * sin_n_squared)
term_C = 1 / (n_values * sin_n_squared)
term_D = 1 / (n_values**4 * sin_n_squared)

# Calculate the cumulative sum for each series
sum_term_A = np.cumsum(term_A)
sum_term_B = np.cumsum(term_B)
sum_term_C = np.cumsum(term_C)
sum_term_D = np.cumsum(term_D)

# Print the values of each sum at n = 10000
print(f"Sum of 1/(n^3 * sin^2(n)) at n = 100000: {sum_term_A[-1]}")
print(f"Sum of 1/(n^2 * sin^2(n)) at n = 100000: {sum_term_B[-1]}")
print(f"Sum of 1/(n^2 * sin^2(n)) at n = 90000: {sum_term_B[-1000]}")
print(f"Sum of 1/(n * sin^2(n)) at n = 100000: {sum_term_C[-1]}")
print(f"Sum of 1/(n^4 * sin^2(n)) at n = 100000: {sum_term_D[-1]}")
# Plotting
plt.figure(figsize=(14, 10))

# Plot 1/(n^3 * sin^2(n))
plt.subplot(2, 4, 1)
plt.plot(n_values, term_A, label=r'$\frac{1}{n^3 \cdot \sin^2(n)}$', color='blue')
plt.title(r'$\frac{1}{n^3 \cdot \sin^2(n)}$')
plt.xlabel('n')
plt.ylabel(r'Term Value')
plt.grid(True)
plt.legend()

# Plot 1/(n^2 * sin^2(n))
plt.subplot(2, 4, 2)
plt.plot(n_values, term_B, label=r'$\frac{1}{n^2 \cdot \sin^2(n)}$', color='green')
plt.title(r'$\frac{1}{n^2 \cdot \sin^2(n)}$')
plt.xlabel('n')
plt.ylabel(r'Term Value')
plt.grid(True)
plt.legend()

# Plot 1/(n * sin^2(n))
plt.subplot(2, 4, 3)
plt.plot(n_values, term_C, label=r'$\frac{1}{n \cdot \sin^2(n)}$', color='red')
plt.title(r'$\frac{1}{n \cdot \sin^2(n)}$')
plt.xlabel('n')
plt.ylabel(r'Term Value')
plt.grid(True)
plt.legend()

# Plot 1/(n^4 * sin^2(n))
plt.subplot(2, 4, 4)
plt.plot(n_values, term_D, label=r'$\frac{1}{n^4 \cdot \sin^2(n)}$', color='purple')
plt.title(r'$\frac{1}{n^4 \cdot \sin^2(n)}$')
plt.xlabel('n')
plt.ylabel(r'Term Value')
plt.grid(True)
plt.legend()

# Plot cumulative sum of 1/(n^3 * sin^2(n))
plt.subplot(2, 4, 5)
plt.plot(n_values, sum_term_A, label=r'$\sum \frac{1}{n^3 \cdot \sin^2(n)}$', color='blue')
plt.title(r'Cumulative Sum of $\frac{1}{n^3 \cdot \sin^2(n)}$')
plt.xlabel('n')
plt.ylabel(r'Cumulative Sum')
plt.grid(True)
plt.legend()

# Plot cumulative sum of 1/(n^2 * sin^2(n))
plt.subplot(2, 4, 6)
plt.plot(n_values, sum_term_B, label=r'$\sum \frac{1}{n^2 \cdot \sin^2(n)}$', color='green')
plt.title(r'Cumulative Sum of $\frac{1}{n^2 \cdot \sin^2(n)}$')
plt.xlabel('n')
plt.ylabel(r'Cumulative Sum')
plt.grid(True)
plt.legend()

# Plot cumulative sum of 1/(n * sin^2(n))
plt.subplot(2, 4, 7)
plt.plot(n_values, sum_term_C, label=r'$\sum \frac{1}{n \cdot \sin^2(n)}$', color='red')
plt.title(r'Cumulative Sum of $\frac{1}{n \cdot \sin^2(n)}$')
plt.xlabel('n')
plt.ylabel(r'Cumulative Sum')
plt.grid(True)
plt.legend()

# Plot cumulative sum of 1/(n^4 * sin^2(n))
plt.subplot(2, 4, 8)
plt.plot(n_values, sum_term_D, label=r'$\sum \frac{1}{n^4 \cdot \sin^2(n)}$', color='purple')
plt.title(r'Cumulative Sum of $\frac{1}{n^4 \cdot \sin^2(n)}$')
plt.xlabel('n')
plt.ylabel(r'Cumulative Sum')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('main_problems.png')

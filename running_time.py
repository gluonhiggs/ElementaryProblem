import numpy as np
import matplotlib.pyplot as plt

# Define constants for the function
alpha = 1.0   # Efficiency gain factor from parallelism
beta = 0.1    # Overhead cost factor due to parallelism
gamma = 0.01  # Network communication cost factor due to parallelism
delta = 100.0  # Load imbalance cost factor due to imbalance cores per executor
epsilon = 0.1 # Constant term

# Define cluster configuration (example)
W = 3  # Number of workers
E = [1, 1, 1]  # Executors per worker (example)
C = [[8], [8], [4]]  # Cores per executor in each worker

# Total parallelism (sum of all cores across workers and executors)
total_parallelism = sum([sum(C[i]) for i in range(W)])

# Define distributed computing factor D
D = 3  # Example factor to simulate network overhead or shuffling

# Define a range for the number of partitions P
P_values = np.arange(1, total_parallelism * 5, 1)  # More partitions than parallelism

# Define the function T(P)
def T(P):
    imbalance_factor = max([sum(C[i]) for i in range(W)]) / total_parallelism
    return alpha * np.log(P) + beta * P + gamma * P**2 + delta * D * imbalance_factor / P + epsilon

# Compute T(P) for the range of P values
T_values = T(P_values)
# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(P_values, T_values, label="T(P) - Running Time Function with Distributed Computing", color='b')
plt.xlabel("Number of Partitions (P)")
plt.ylabel("Running Time (T(P))")
plt.title("Running Time as a Function of Partitions (Incorporating Distributed Computing)")
plt.grid(True)
plt.legend()
plt.savefig('running_time.png')

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))

# Perform least squares regression
A = np.vstack([x, np.ones(len(x))]).T
alpha, _, _, _ = np.linalg.lstsq(A, y, rcond=None)

# Plot the data points and least squares solution
plt.plot(x, y, 'ro', label='data')
plt.plot(x, alpha[0] * x + alpha[1], 'b-', label='least squares solution')
plt.legend()
plt.show()

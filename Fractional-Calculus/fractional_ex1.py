import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import gamma

def fgl_deriv(a, y, h):
    n = len(y)
    J = np.arange(n)
    G1 = gamma(J + 1)
    G2 = gamma(a + 1 - J)
    s = (-1) ** J

    # Check if G1 or G2 are zero or invalid and replace them with epsilon
    epsilon = 1e-10
    G1[G1 == 0] = epsilon
    G2[G2 == 0] = epsilon

    M = np.tril(np.ones((n, n)))
    R = np.outer(y, np.ones(n))

    T = (gamma(a + 1) / (h ** a)) * s / (G1 * G2)
    Y = np.sum(R * M * T, axis=1).reshape(y.shape)

    return Y

# Sample sine between 0 and 2*pi with steps of 0.01 rad
h = 0.01
t = np.arange(0, 2 * np.pi + h, h)
y = np.sin(t)

# Compute fractional derivatives with different orders
order = np.arange(0, 1.1, 0.1)
yd = np.zeros((len(order), len(t)))

for i in range(len(order)):
    yd[i, :] = fgl_deriv(order[i], y, h)

# Plot the results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(t, order)
ax.plot_surface(X, Y, yd, cmap='viridis')
ax.set_xlabel('t')
ax.set_ylabel('\u03B1')
ax.set_zlabel('y')
ax.set_title('Fractional derivatives of sine')
plt.show()









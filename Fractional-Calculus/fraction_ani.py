import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import gamma
from matplotlib.animation import FuncAnimation

def fgl_deriv(a, y, h):
    n = len(y)
    J = np.arange(n)
    G1 = gamma(J + 1)
    G2 = gamma(a + 1 - J)
    s = (-1) ** J

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

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the range of orders for the animation
order_range = np.arange(0.1, 1.0, 0.1)

# Create a grid of t and order values
T, Order = np.meshgrid(t, order_range)

# Initialize an empty list to store the surfaces
surfaces = []

# Function to update the plot for each frame of the animation
def update(frame):
    ax.clear()
    order = order_range[frame]
    yd = fgl_deriv(order, y, h)
    YD = np.tile(yd, (len(order_range), 1))  # Replicate yd for all orders
    ax.plot_surface(T, Order, YD, cmap='viridis')
    ax.set_xlabel('t')
    ax.set_ylabel('\u03B1')
    ax.set_zlabel('y')
    ax.set_title(f'Fractional derivatives of sine (Order = {order:.1f})')

# Create the animation
ani = FuncAnimation(fig, update, frames=len(order_range), interval=500)

# Save the animation as an MP4 file
ani.save('fractional_derivatives_animation.mp4', writer='ffmpeg', fps=10)

# Show the animation in the Jupyter Notebook (optional)
# from IPython.display import HTML
# HTML(ani.to_jshtml())

plt.show()




import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def fint(x, alpha, n, h):
    N = len(x)
    output = np.zeros(N)
    h_a = h ** alpha
    
    for i in range(N):
        sigma = 0
        for m in range(n + 1):
            if i - m < 0:
                break
            denominator = np.math.factorial(m) * gamma(alpha)
            if denominator == 0:
                # Handle division by zero or very small denominator
                print(f"Warning: denominator is zero for i={i}, m={m}")
                sigma += 0  # You can choose an appropriate value here
            else:
                sigma += gamma(alpha + m) / denominator * x[i - m]
        
        output[i] = sigma * h_a
    
    return output
ts = 0.01
n = 170
t = np.arange(0, 2 + ts, ts)
x = t

fig, ax = plt.subplots()
h1, = ax.plot(t, x + 0.05, 'r', label='\u03B1 = 0')
h2, = ax.plot(t, x, 'b', label='0 < \u03B1 < 1')
h3, = ax.plot(t, x, 'm', label='\u03B1 = 1')
ax.legend()
ax.set_xlabel('t')
ax.set_ylabel('x(t)')
ax.set_title('Fractional Integral')
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
h4 = ax.text(0.2, 1.8, '')

def update(alpha):
    ax.set_title(f'Fractional Integral (\u03B1 = {alpha:.2f})')
    if alpha == 0:
        x1 = x + 0.05
    else:
        x1 = x
    x2 = fint(x1, alpha, n, ts)
    h1.set_ydata(x1)
    h2.set_ydata(x2)
    h4.set_text(f'\u03B1 = {alpha:.2f}')
    return h1, h2, h4

ani = FuncAnimation(fig, update, frames=np.arange(0, 1.05, 0.05), blit=True)

# Save the animation as a GIF
ani.save('fint.gif', writer='pillow', fps=10)

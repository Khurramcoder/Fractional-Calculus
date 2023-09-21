import numpy as np
from scipy.special import gamma

def fderiv(x, alpha, n, h):
    # Calculate the fractional derivative of x
    # x      Sampled function
    # alpha  Fractional order
    # n      Size of the memory
    # h      Sampling rate
    
    N = len(x)
    output = np.zeros(N)
    h_a = h ** alpha
    
    for i in range(N):
        sigma = 0
        for m in range(n + 1):
            if i - m < 0:
                break
            sigma += ((-1) ** m) * gamma(alpha + 1) / (np.math.factorial(m) * gamma(alpha - m + 1)) * x[i - m]
        
        output[i] = sigma / h_a
    
    return output


import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt
def fint(x, alpha, n, h):
    # Calculate the fractional integral of x
    # x      Sampled function
    # alpha  Fractional order
    # n      Size of the memory
    # h      Sampling rate
    
    N = len(x)
    output = np.zeros(N)
    h_a = h ** alpha
    
    for i in range(N):
        sigma = 0
        for m in range(n + 1):
            if i - m < 0:
                break
            sigma += gamma(alpha + m) / (np.math.factorial(m) * gamma(alpha)) * x[i - m]
        
        output[i] = sigma * h_a
    
    return output
ts = 0.01
n = 170

t = np.arange(0, 2 + ts, ts)
x = t

plt.figure()
plt.plot(t, x)

x_d = fderiv(x, 1, n, ts)
x_i = fint(x, 1, n, ts)

plt.plot(t, x_d)
plt.plot(t, x_i)

plt.legend(['x', 'xd', 'xint'])
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


ts = 0.01
n = 170
t = np.arange(0, 2 + ts, ts)
x = t

fig, ax = plt.subplots()
h1, = ax.plot(t, x, 'r', label='\u03B1 = 0')
h2, = ax.plot(t, x, 'b', label='0 < \u03B1 < 1')
h3, = ax.plot(t, x, 'm', label='\u03B1 = 1')
ax.legend()
ax.set_xlabel('t')
ax.set_ylabel('x(t)')
ax.set_title('Fractional Derivative')
h4 = ax.text(0.2, 1.8, '')

def update(alpha):
    ax.set_title(f'Fractional Derivative (\u03B1 = {alpha:.2f})')
    ax.legend(loc='lower right')
    x2 = fderiv(x, alpha, n, ts)
    h2.set_ydata(x2)
    h4.set_text(f'\u03B1 = {alpha:.2f}')
    return h2, h4

ani = FuncAnimation(fig, update, frames=np.arange(0, 1.05, 0.05), blit=True)

# Save the animation as a GIF
ani.save('fderiv.gif', writer='pillow', fps=10)



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



ts = 0.01
n = 170
t = np.arange(0, 2 + ts, ts)
x = t

fig, ax = plt.subplots()
h1, = ax.plot(t, x, 'r', label='\u03B1 = 0')
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
    ax.legend(loc='lower right')
    x2 = fint(x, alpha, n, ts)
    h2.set_ydata(x2)
    h4.set_text(f'\u03B1 = {alpha:.2f}')
    return h2, h4

ani = FuncAnimation(fig, update, frames=np.arange(0, 1.05, 0.05), blit=True)

# Save the animation as a GIF
ani.save('fint.gif', writer='pillow', fps=10)

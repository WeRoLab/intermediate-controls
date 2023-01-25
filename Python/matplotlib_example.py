import numpy as np
import matplotlib
matplotlib.use('TkAgg')         #Optional code if you get "backend" errors

import matplotlib.pyplot as plt

def funHW1(x):
    """Function template"""
    return np.sin(x)

x = np.linspace(0, 2*np.pi, 1000)
y = np.array([funHW1(xi) for xi in x])

fig, ax = plt.subplots()
ax.plot(x, y, '--o', label = 'Sine')
ax.set_ylabel('Output y')
ax.set_xlabel('Input y')
ax.set_title('Sample Plot')
ax.legend()
ax.grid(True)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Update plotting parameters for aesthetics (optional)
plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    # 'font.size' : 11,
    'text.usetex': True,
    'pgf.rcfonts': False,
})

def funHW1(x):      #Defining an arbitrary function (modify according to HW)
    """Function template"""
    y = np.sin(x)   #Template function is a sinusoid but it can be any function
    return y

x = np.linspace(0, 2*np.pi, 300)       #Generating grid of points in x axis
y = np.array([funHW1(xi) for xi in x])  #Generating outputs using "List Comprehensions" https://docs.python.org/3.11/tutorial/datastructures.html#list-comprehensions

# Plotting the output
fig, ax = plt.subplots()
ax.plot(x, y, '--o', label = '$y = \sin(x)$')
ax.set_ylabel('Output ($y$)')
ax.set_xlabel('Input ($x$)')
ax.set_title('Sample Plot')
ax.legend()
ax.grid(True)
plt.savefig('pdflatex_IC\Figures\TestFigure.pgf')
plt.show()
# Example code to numerically solve a differential equation using Runge-Kutta
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def fun(x, a):
    """Example differential equation \dot{x} = a*x"""
    dxdt = a*x
    return dxdt

n   = 1000                      #Number of samples
a   = 2                         #Parameter for the differential equation
tim = np.linspace(0, 1, n)      #Array of time
f   = lambda t, x: fun(x, a)    #Function that takes as input time and x and outputs dx/dt

sol = solve_ivp(f, [0, 1], [7], t_eval= tim)    #Solve! (using scipy.integrate)

fig, ax = plt.subplots()        #Plot!
ax.plot(sol.t, sol.y[0], '--o')
ax.set_ylabel('Solution [x]')
ax.set_xlabel('Time [s]')
ax.set_title('Solution to the differential equation')
plt.show()
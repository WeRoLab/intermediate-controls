# Example code to numerically solve a differential equation using Runge-Kutta
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def fun(x, p, v):
    """Nonlinear differential equation to model Hare and Lynx population
        x: state
        p: system parameters
        r: reference signal 
    """
    dxdt    = np.array([0, 0])
    u       = p['K'] @ x + p['kf'] * v      #Use @ to indicate matrix multiplication on ndarrays
    dxdt[0] = (p['r'] + u) * x[0] * (1 - x[0] / p['k1']) - (p['a'] * x[0] * x[1]) / (p['c'] + x[0])
    dxdt[1] = (p['b'] * p['a'] * x[0] * x[1]) / (p['c'] + x[0]) - p['d'] * x[1]
    return dxdt

p = {           #Dictionary with the differential equation parameters
    'a' : 3.2,
    'b' : 0.6,
    'c' : 50,
    'd' : 0.56,
    'k1': 125,
    'r' : 1.6,
    'K' : np.array([0, 0]),
    'kf': 0,
}

n   = 1000                      #Number of samples
tim = np.linspace(0, 1000, n)     #Array of time
v   = 0
f   = lambda t, x: fun(x, p, v)    #Function that takes as inputs time and x and outputs dx/dt
sol = solve_ivp(f, [0, tim[-1]], [21, 34], t_eval= tim)    #Solve! (using scipy.integrate)

fig, ax = plt.subplots()        #Plot!
ax.plot(sol.t, sol.y[1], '--o', label = 'Hare')
ax.plot(sol.t, sol.y[0], '--o', label = 'Lynx')
ax.set_ylabel('Solution [x]')
ax.set_xlabel('Time [s]')
ax.set_title('Solution to the differential equation')
ax.legend()
ax.grid()
plt.show()
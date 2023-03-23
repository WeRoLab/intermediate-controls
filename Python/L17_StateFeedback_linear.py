# Example code to numerically solve a differential equation using Runge-Kutta
import numpy as np
import matplotlib.pyplot as plt
import control as ct

zet = 1/np.sqrt(2)
om0 = 5.6/5
la1 = -zet*om0 + om0*np.emath.sqrt(zet**2 - 1)
la2 = -zet*om0 - om0*np.emath.sqrt(zet**2 - 1)

# Linear dynamics
A = np.array([[0.13, -0.93],[0.57, 0]])
B = np.array([[17.2], [0]])
C = np.array([0, 1])
D = 0
# Ackerman's formula
K  = ct.place(A, B, [la1, la2])
kf = -1/(C @ np.linalg.inv(A - B @ K) @ B)
# Check eigenvalues of closed loop
w, v = np.linalg.eig(A - B@K)
print(w)
print(la1)
print(la2)

# Plot the step response of the closed-loop system
sys = ct.ss(A - B@K, B*kf, C, D)
T, yout = ct.step_response(sys)

fig, ax = plt.subplots()        #Plot!
ax.plot(T, yout, '--o', label = 'Closed loop')
ax.set_ylabel('z_1')
ax.set_xlabel('Time [s]')
ax.set_title('Step response in closed loop')
ax.legend()
ax.grid()
plt.show()
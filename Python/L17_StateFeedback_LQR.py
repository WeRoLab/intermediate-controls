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

# LQR
Qx = np.diag([1, 1])
Qu = [1]
Klqr, S, E = ct.lqr(A, B, Qx, Qu)
kflqr = -1/(C @ np.linalg.inv(A - B @ Klqr) @ B)
sysLqr = ct.ss(A - B@Klqr, B*kflqr, C, D)
Tlqr, youtLqr = ct.step_response(sysLqr)

fig, ax = plt.subplots(2,1)        #Plot!
ax[0].plot(T, yout, '--o', label = 'Eig. assignment')
ax[0].plot(Tlqr, youtLqr, '--o', label = 'LQR')
ax[0].set_ylabel('z_1')
ax[0].set_xlabel('Time [s]')
ax[0].set_title('Step response in closed loop')
ax[0].legend()
ax[1].grid()
ax[1].plot(T, yout, '--o', label = 'Eig. assignment')
ax[1].plot(Tlqr, youtLqr, '--o', label = 'LQR')
ax[1].set_ylabel('z_1')
ax[1].set_xlabel('Time [s]')
ax[1].set_title('Step response in closed loop')
ax[1].legend()
ax[1].grid()
plt.show()
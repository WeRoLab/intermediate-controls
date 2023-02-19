import numpy as np
import matplotlib.pyplot as plt

n = 10                                              #Number of samples
g = np.random.normal(loc = 50, scale= 1.5, size=n)  #Measurements

# Values of the resistance from the average and least squares (to be calculated)
avg = 0
lsq = 0

# Plotting measurements for illustration purposes
fig, axs = plt.subplots()
axs.plot(g, '--o')
axs.set_title(f'Measurements - Avg = {avg:.3f} - lsq = {lsq:0.3f}')
axs.set_xlabel('Number of sample')
axs.set_ylabel('Resistance [mOhm]')
plt.show()
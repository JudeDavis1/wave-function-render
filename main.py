import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()
ax = fig.add_subplot(111, projection='3d')
x_set = []
y_set = []
z_set = []

PLANKS_CONSTANT = 6.626 * 10**-34
PLANKS_CONSTANT_BAR = PLANKS_CONSTANT / (2 * np.pi)

def animate(frame_i):
    """Animation function"""

    x = 0.1 * frame_i
    y = wave_func(x, t=time.time(), n_=x/2)

    x_set.append(x)
    y_set.append(y)

    ax.clear()
    ax.scatter(x_set, y_set, x_set)

def wave_func(x, t, a=4, n_=5, eN=0.4):
    """Wave function solved by Schrodinger's equation"""
    norm_term = np.sqrt(2 / a)
    ret = norm_term * np.sin(n_ * np.pi * x / a) * np.exp(-1j * eN * t / PLANKS_CONSTANT_BAR)

    return ret

anim = animation.FuncAnimation(
    fig,
    animate,
    interval=1,
    frames=int(100),

)
plt.show()

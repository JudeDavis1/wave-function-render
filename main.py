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
H_BAR = PLANKS_CONSTANT / (2 * np.pi)
DELTA = 0.02

def animate(frame_i):
    """Animation function"""

    x = DELTA * frame_i
    y = DELTA * frame_i
    z = wave_func((x, y), t=time.time(), n_=3)

    x_set.append(x)
    y_set.append(y)
    z_set.append(z)

    ax.clear()
    ax.plot3D(x_set, y_set, z_set)

def wave_func(coords, t, a=4, n_=5, m=1.00784):
    """Wave function by solving Schrodinger's equation"""

    x, y = coords
    eN = get_energy(n_, m, a)
    norm_term = np.sqrt(2 / a)
    time_dependence = np.exp(-1j * eN * t / H_BAR)
    arg = lambda coord: n_ * np.pi * coord / a
    ret = norm_term * np.sin(arg(x)) * np.sin(arg(y)) * time_dependence

    return ret

def get_energy(n, m, a):
    potential = 0
    upper = np.product([H_BAR ** 2, np.pi ** 2, n ** 2])
    lower = 2 * m * a ** 2
    return (upper / lower) + potential

anim = animation.FuncAnimation(
    fig,
    animate,
    interval=0,
    frames=int(1e6),
)
plt.show()

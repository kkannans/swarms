import numpy as np
def Compute_Sinusoidal_Trajectory(T, amplitude, frequency, offset):
    trajectory = np.zeros(T)
    for idx, val in enumerate(np.linspace(0, 2*np.pi, T)):
        trajectory[idx] = amplitude*(np.sin(frequency*val + offset))

    return trajectory
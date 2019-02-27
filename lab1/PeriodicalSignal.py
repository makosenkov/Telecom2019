import cmath

import matplotlib.pyplot as plt
import numpy as np


def signal_wave():
    frequency = 0.5 * np.pi
    fs = 0.001
    ts = 1 / fs
    n = 256
    t = np.arange(0, n * ts, ts)
    x = np.cos(2 * np.pi * frequency * t)
    sig_fft = abs(np.fft.fft(x))
    sig_phase = map(cmath.phase, np.fft.fft(x))
    plt.figure()
    #plt.plot(t, x)
    plt.grid(True)
    #plt.show()
    plt.plot(sig_fft)
    plt.show()

    plt.figure()
    plt.plot(t, x)
    plt.grid(True)
    plt.show()
    plt.plot(sig_phase)
    plt.show()


if __name__ == '__main__':
    signal_wave()
    #pulstran
    #rectpuls
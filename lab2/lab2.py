import numpy as np
from scipy import signal
import time


def position(correlations, sinc_package):
    for i in range(0, len(correlations) - 3):
        if sum(correlations[i:i + 3]) == sum(sinc_package):
            return i + 1


def package():
    sinc_package = np.array([1, 0, 1], dtype=int)
    sig = np.array([0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0], dtype=int)

    start_time = time.time()
    correlations_direct = signal.correlate(sig, sinc_package, mode='valid', method='direct')  # прямой метод
    print("Direct method: %s seconds" % (time.time() - start_time))

    start_time = time.time()
    correlations_fft = signal.correlate(sig, sinc_package, mode='valid', method='fft')  # быстрая корреляция
    print("FFT method: %s seconds" % (time.time() - start_time))

    print("Direct correlations:", correlations_direct)
    print("FFT correlations   :", correlations_fft)
    pos = position(correlations_direct, sinc_package)
    print("Direct position:", pos)
    print("FFT position   :", position(correlations_fft, sinc_package))
    package = sig[pos + 3:][:8]
    print("Package: ", package)


if __name__ == '__main__':
    package()

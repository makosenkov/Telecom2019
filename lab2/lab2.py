import numpy as np
from scipy import signal
import time
import matplotlib.pyplot as plt


def position(correlations, sinc_package):
    for i in range(0, len(correlations) - 3):
        if sum(correlations[i:i + 3]) == sum(sinc_package):
            return i + 1

def get_plot(x, y, x_label, y_label, title, show, save):
    plt.figure()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(x, y)
    plt.grid(True)
    if show:
        plt.show()
    if save:
        plt.savefig(title + '.png')

def package():
    sinc_package = np.array([1, 0, 1], dtype=int)
    sig = np.array([0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0], dtype=int)

    start_time = time.time()
    correlations_direct = signal.correlate(sig, sinc_package, mode='valid', method='direct')  # прямой метод
    print("Direct method:\n--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    correlations_fft = signal.correlate(sig, sinc_package, mode='valid', method='fft')  # быстрая корреляция
    print("FFT method:\n--- %s seconds ---" % (time.time() - start_time))

    print("Correlations using direct method:", correlations_direct)
    print("Correlations using FFT method   :", correlations_fft)
    pos = position(correlations_direct, sinc_package)
    print("Position with direct correlation:", pos)
    print("Position with FFT correlation   :", position(correlations_fft, sinc_package))
    package = sig[pos + 3:][:8]
    print("Package: ", package)


def get_triangle():
    fs = 1000
    number = 4096
    t = np.arange(0, number / fs, 1 / fs)
    freq = 20

    sig = signal.sawtooth(2 * np.pi * freq * t)
    sig_fft = np.fft.fft(sig) / number * 2
    fft_freq = np.fft.fftfreq(number, 1 / fs)
    lim = fs // 2
    # график треугольного сигнала
    get_plot(x=t[:lim], y=sig[:lim], x_label='Time',
             y_label='Amplitude', title='Triangle signal',
             show=True, save=False)
    # спектр треугольного сигнала
    get_plot(x=fft_freq[:lim], y=sig_fft[:lim], x_label='Frequency',
             y_label='Amplitude', title='Triangle spectrum',
             show=True, save=False)


if __name__ == '__main__':
    package()
    get_triangle()

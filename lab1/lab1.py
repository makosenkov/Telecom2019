import matplotlib.pyplot as plt
import numpy as np


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


if __name__ == '__main__':
    fs = 1000
    number = 4096
    t = np.arange(0, number / fs, 1 / fs)
    freq = 20
    amplitude = 2
    # синусоидальный сигнал
    signal = amplitude * np.cos(2 * np.pi * freq * t) + \
             amplitude * np.sin(4 * np.pi * freq * t) + \
             amplitude * np.sin(np.pi * freq * t)
    # импульсный сигнал
    signal_imp = amplitude * np.sign(signal)
    # преобразования Фурье
    sig_fft = np.fft.fft(signal) / number * 2
    sig_imp_fft = np.fft.fft(signal_imp) / number * 2
    # частота
    fft_freq = np.fft.fftfreq(number, 1 / fs)
    lim = fs // 2
    # график синусоидального сигнала
    get_plot(x=t[:lim], y=signal[:lim], x_label='Time',
             y_label='Amplitude', title='Wave signal',
             show=True, save=False)
    # спектр синусоидального сигнала
    get_plot(x=fft_freq[:lim], y=sig_fft[:lim], x_label='Frequency',
             y_label='Amplitude', title='Wave spectrum',
             show=True, save=False)
    # график импульсного сигнала
    get_plot(x=t[:lim], y=signal_imp[:lim], x_label='Time',
             y_label='Amplitude', title='Impulse signal',
             show=True, save=False)
    # спектр импульсного сигнала
    get_plot(x=fft_freq[:lim], y=sig_imp_fft[:lim], x_label='Frequency',
             y_label='Amplitude', title='Impulse spectrum',
             show=True, save=False)

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


# синусоидальный сигнал
def sin_signal(time, frequency, amplit):
    sig = amplit * np.sin(2 * np.pi * frequency * time)
    return sig


# импульсный сигнал
def imp_signal(time, frequency, amplit):
    sig = amplit * np.sign(sin_signal(time, frequency, amplit))
    return sig


# треугольный сигнал
def triangle_signal(time, frequency):
    sig = np.convolve(np.sign(np.sin(2 * np.pi * frequency * time)),
                      np.sign(np.sin(2 * np.pi * frequency * time)), 'same')
    return sig


def get_fft_signal(num, sampling, sig):
    # преобразование Фурье
    fft = np.fft.fft(sig) / num * 2
    # частота
    freq_fft = np.fft.fftfreq(num, 1 / sampling)
    limit = sampling // 2
    return fft, freq_fft, limit


if __name__ == '__main__':
    fs = 1000
    number = 4096
    t = np.arange(0, number / fs, 1 / fs)
    freq = 20
    amplitude = 2
    mean = 0
    std = 1
    sig_array = [sin_signal(t, freq, amplitude),
                 imp_signal(t, freq, amplitude),
                 triangle_signal(t, freq)]
    for signal in sig_array:
        sig_fft, fft_freq, lim = get_fft_signal(number, fs, signal)
        # график сигнала
        get_plot(x=t[:lim], y=signal[:lim], x_label='Time',
                 y_label='Amplitude', title='Signal plot',
                 show=True, save=False)
        # график спектра сигнала
        get_plot(x=fft_freq[:lim], y=sig_fft[:lim], x_label='Frequency',
                 y_label='Amplitude', title='Spectrum plot',
                 show=True, save=False)
        sig_with_noise = np.random.normal(mean, std, size=number)
        get_plot(x=t[:lim], y=sig_with_noise[:lim], x_label='Time',
                 y_label='Amplitude', title='Noise plot',
                 show=True, save=False)

import matplotlib.pyplot as plt
import numpy as np

def get_plot(x, y, x_label, y_label, title, show, save, close):
    #plt.figure()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(x, y)
    plt.grid(True)
    if show:
        plt.show()
    if save:
        plt.savefig(title + '.png')
    if close:
        plt.close()


def get_fft_signal(num, sampling, sig):
    # преобразование Фурье
    fft_sig = np.fft.fft(sig) / num * 2
    # частота
    freq_fft = np.fft.fftfreq(num, 1 / sampling)
    lim = 1000
    return fft_sig, freq_fft, lim


def plot_am(t, message_signal, modulated):
    lim = 150
    get_plot(t[:lim], modulated[:lim],
             x_label='Time', y_label='Amplitude', title='AM',
             show=False, save=False, close=False)
    get_plot(t[:lim], message_signal[:lim],
             x_label='Time', y_label='Amplitude', title='AM',
             show=True, save=False, close=True)


def signal_synthesis():
    fs = 2000
    number = 8192
    t = np.arange(0, number / fs, 1 / fs)
    message_freq = 20
    amplitude = 1
    # синусоидальный сигнал
    message_signal = amplitude * np.sin(2 * np.pi * message_freq * t)
    carrier_freq = 500
    carrier_signal = 2 * np.cos(2 * np.pi * carrier_freq * t)
    modulated = message_signal * carrier_signal
    plot_am(t, message_signal, modulated)

    carrier_signal = 2 * np.sin(2 * np.pi * carrier_freq * t)
    modulated = message_signal * carrier_signal
    plot_am(t, message_signal, modulated)

    sig_fft, fft_freq, lim = get_fft_signal(number, fs, modulated)
    # график спектра сигнала
    get_plot(x=fft_freq[:lim], y=sig_fft[:lim], x_label='Frequency',
             y_label='Amplitude', title='Spectrum plot',
             show=True, save=False, close=True)


if __name__ == '__main__':
    signal_synthesis()

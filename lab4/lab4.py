import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def get_plot(x, y, x_label, y_label, title, show, save, close, pic_name):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(x, y)
    plt.grid(True)
    if save:
        plt.savefig(pic_name + '.png')
    if close:
        plt.close()


def get_fft_signal(num, sampling, sig):
    # преобразование Фурье
    fft_sig = np.fft.fft(sig) / num * 2
    # частота
    freq_fft = np.fft.fftfreq(num, 1 / sampling)
    lim = 1500
    return fft_sig, freq_fft, lim


def signal_synthesis():
    fs = 1500
    number = 4096
    t = np.arange(0, number / fs, 1 / fs)
    message_freq = 20
    amplitude = 1
    # исходный сигнал
    message_signal = amplitude * np.sin(2 * np.pi * message_freq * t)
    carrier_freq = 500
    carrier_signal = np.sin(2 * np.pi * carrier_freq * t)

    # ==========АМПЛИТУДНАЯ===========
    modulated = (1 + 0.5 * amplitude * message_signal) * carrier_signal
    lim = 200
    get_plot(t[:lim], modulated[:lim],
             x_label='Time', y_label='Amplitude', title='AM, M < 1',
             show=True, save=True, close=True, pic_name='am1_sig')

    modulated = (1 + 1.5 * amplitude * message_signal) * carrier_signal
    get_plot(t[:lim], modulated[:lim],
             x_label='Time', y_label='Amplitude', title='AM, M > 1',
             show=True, save=True, close=True, pic_name='am2_sig')

    modulated = (1 + amplitude * message_signal) * carrier_signal
    get_plot(t[:lim], modulated[:lim],
             x_label='Time', y_label='Amplitude', title='AM, M = 1',
             show=True, save=True, close=True, pic_name='am3_sig')
    sig_fft, fft_freq, lim = get_fft_signal(number, fs, modulated)
    # график спектра сигнала с модуляцией
    get_plot(x=fft_freq[:lim], y=sig_fft[:lim], x_label='Frequency',
             y_label='Amplitude', title='AM spectrum',
             show=True, save=True, close=True, pic_name='am_spectrum')

    # ==========С ПОДАВЛЕНИЕМ НЕСУЩЕЙ===========
    suppressed_modulated = message_signal * carrier_signal
    lim = 190
    get_plot(t[:lim], suppressed_modulated[:lim],
             x_label='Time', y_label='Amplitude', title='Supressed modulation',
             show=True, save=True, close=True, pic_name='sup_sig')
    sig_fft, fft_freq, lim = get_fft_signal(number, fs, suppressed_modulated)
    # график спектра сигнала с модуляцией
    get_plot(x=fft_freq[:lim], y=sig_fft[:lim], x_label='Frequency',
             y_label='Amplitude', title='Supressed spectrum',
             show=True, save=True, close=True, pic_name='sup_spectrum')

    # ==========ОДНОПОЛОСНАЯ===========
    single_mod = signal.hilbert(message_signal) * np.cos(2 * np.pi * carrier_freq * t) - \
                 signal.hilbert(message_signal) * carrier_signal
    lim = 190
    get_plot(t[:lim], single_mod[:lim],
             x_label='Time', y_label='Amplitude', title='Singleband modulation',
             show=False, save=False, close=False, pic_name='single_sig')
    get_plot(t[:lim], message_signal[:lim],
             x_label='Time', y_label='Amplitude', title='Singleband modulation',
             show=True, save=True, close=True, pic_name='single_sig')
    sig_fft, fft_freq, lim = get_fft_signal(number, fs, single_mod)
    # график спектра сигнала с модуляцией
    get_plot(x=fft_freq[:lim], y=sig_fft[:lim], x_label='Frequency',
             y_label='Amplitude', title='Single band spectrum',
             show=True, save=True, close=True, pic_name='single_spectrum')


if __name__ == '__main__':
    signal_synthesis()

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


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



# синусоидальный сигнал
def sin_signal(time, frequency, amplit):
    sig = amplit * np.sin(2 * np.pi * frequency * time)
    return sig


# импульсный сигнал
def imp_signal(time, frequency, amplit):
    sig = amplit * np.sign(sin_signal(time, frequency, amplit))
    return sig


# треугольный сигнал
def triangle_signal(time, frequency, amplit):
    sig = signal.sawtooth(amplit * np.pi * frequency * time)
    return sig


def get_fft_signal(num, sampling, sig):
    # преобразование Фурье
    fft_sig = np.fft.fft(sig) / num * 2
    # частота
    freq_fft = np.fft.fftfreq(num, 1 / sampling)
    limit = sampling // 2
    return fft_sig, freq_fft, limit


if __name__ == '__main__':
    fs = 1000
    number = 2048
    t = np.arange(0, number / fs, 1 / fs)
    freq = 20
    amplitude = 1
    sig_array = [sin_signal(t, freq, amplitude),
                 imp_signal(t, freq, amplitude),
                 triangle_signal(t, freq, amplitude)]
    for input_signal in sig_array:
        sig_fft, fft_freq, lim = get_fft_signal(number, fs, input_signal)
        # добавляем шум
        noise = 2 * np.random.random_sample(input_signal.size, ) - 1
        sig_with_noise = input_signal + noise
        get_plot(x=t[:lim], y=sig_with_noise[:lim], x_label='Time',
                 y_label='Amplitude', title='Noise plot',
                 show=False, save=False, close=False)
        # график сигнала
        get_plot(x=t[:lim], y=input_signal[:lim], x_label='Time',
                 y_label='Amplitude', title='Signal plot',
                 show=True, save=False, close=True)
        # график спектра сигнала
        get_plot(x=fft_freq[:lim], y=sig_fft[:lim], x_label='Frequency',
                 y_label='Amplitude', title='Spectrum plot',
                 show=False, save=False, close=True)
        # создаем фильтр и применяем на зашумленный сигнал
        b, a = signal.butter(4, Wn=[(freq - 1) / 500, (freq + 1) / 500], btype='bandpass')
        filtered = signal.filtfilt(b, a, sig_with_noise)
        get_plot(x=t[:lim], y=filtered[:lim], x_label='Time',
                 y_label='Amplitude', title='Filtered signal',
                 show=True, save=False, close=True)
        # спектр отфильтрованного сигнала
        filt_sig_fft, filt_fft_freq, filt_lim = get_fft_signal(number, fs, filtered)
        get_plot(x=filt_fft_freq[:filt_lim], y=filt_sig_fft[:filt_lim], x_label='Frequency',
                 y_label='Amplitude', title='FILTERED SPECTRUM',
                 show=False, save=False, close=True)

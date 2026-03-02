import soundfile as sf
import numpy as np

# sf.read() returns two things:
# 1. the audio data as a NumPy array 
# 2. the sample rate
def load_audio(filename):
    data, samplerate = sf.read(filename)
    return data, samplerate 


# Uses Fast Fourier Transform on the data matrix from load_audio() to a frequency (Time -> Frequency)
# then uses fftfreq() to find the frequency rates. Early entries in the matrix are low freqncies higher entries are high frequencies
# If it is dual audio process as two data sets if it is mono audio process one data set
def to_frequency_domain(data, samplerate):
    if data.ndim == 2:
        # Apply FFT to each channel separately
        data_fft_left = np.fft.fft(data[:, 0])
        data_fft_right = np.fft.fft(data[:, 1])
        freq_axis = np.fft.fftfreq(len(data), 1/samplerate)
        return (data_fft_left, data_fft_right), freq_axis
    else:
        data_fft = np.fft.fft(data)
        freq_axis = np.fft.fftfreq(len(data), 1/samplerate)
        return data_fft, freq_axis

# Take whatever filter shape you desire and then apply that to the data_fft from to_frequency_domain() (remember your filter is a literal y= mx + b kinda function that is why we made an axis)
def apply_filter(data_fft, freq_axis, filter_function):
    if isinstance(data_fft, tuple):
        left = data_fft[0] * filter_function(freq_axis)
        right = data_fft[1] * filter_function(freq_axis)
        return (left, right)
    return data_fft * filter_function(freq_axis)

# Use inverse FFT to take your now modified data and convert it from the frequency domain back to the time domain
def to_time_domain(filtered_data):
    if isinstance(filtered_data, tuple):
        left = np.real(np.fft.ifft(filtered_data[0]))
        right = np.real(np.fft.ifft(filtered_data[1]))
        return np.column_stack((left, right))
    return np.real(np.fft.ifft(filtered_data))

# Function that saves the now transformed data as a file to be listened to
def save_as_audio(filename, data_ifft, samplerate):
    sf.write(filename, data_ifft, samplerate)

    









# data, samplerate = load_audio("test_sound.wav")
# data_fft, freq_axis = to_frequency_domain(data, samplerate)

#PRINTS FOR TESTING PURPOSES
#load_audio()
# print(samplerate) # 48000 in my test
# print(data.shape) # return the data as a (X, 2) matrix where the columns are the collection of samples for each "ear" 7.61 seconds clip at 48k yields 7.61 * 48000 = 365714 rows
# print(data[:10])

#frequency_domain()
# print(len(data))
# print(1/samplerate)
# print(freq_axis)
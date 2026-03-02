from data_filters import *
from filter_choice import *

#---------------CHANGE THESE-----------------------
cutoff_frequency = 1100 # Cutoff frequency in Hz

the_filter = low_pass(cutoff_frequency) #change low_pass to high_pass if you want to test the highpass

data, samplerate = load_audio("test_sound.wav") # Name of the audio file you want to filter

file_output_name = "lowpassfilter_e.wav" # Name of the file upon output
#--------------------------------------------------

data_fft, freq_axis = to_frequency_domain(data, samplerate)

filtered_data = apply_filter(data_fft, freq_axis, the_filter)

data_ifft = to_time_domain(filtered_data)

save_as_audio(file_output_name, data_ifft, samplerate)
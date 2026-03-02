# Audio Filter Engine

A Python-based audio signal processing pipeline that applies 
customizable frequency domain filters to audio files of choice.

## What It Does
Loads a .WAV file (or any file supported by soundfile), transforms it into the frequency 
domain using FFT. Then applies a user-defined filter function and reconstructs 
the filtered audio using inverse FFT. At the moment, a very basic lowpass and highpass
are the only filters available.

## Installation
pip install numpy scipy matplotlib soundfile

## Usage
python main.py

For now, just change the values in the CHANGE THESE section of main.py. Later on 
I will add a prompt for the user to input their cutoff frequency, file of choice, and
what filter they want to use.


## How It Works
Audio signals are transformed from the time domain into the 
frequency domain using the Fast Fourier Transform (FFT). 
A filter function is applied by multiplying the frequency 
spectrum by a transfer function - values near 1 pass through 
unchanged, values near 0 are reduced. The filtered signal 
is reconstructed via inverse FFT.

## Filters Available
- Lowpass - reduce frequencies above a cutoff
- Highpass - reduce frequencies below a cutoff
- More coming soon

## Planned Features
SOON
- Change the Lowpass and Highpass to resemble that of a classic MG filter that is seen in software
- Prompt the user rather than having them change the code manually

LATER
- Comb filter
- Ring modulation
- Real-time visualization with sliders
- Reverb and delay
- Any filter that I can think of



# https://pythondsp.rob-elder.com/loading-wav-files-and-showing-frequency-response/


import winsound, time
from math import log2, pow

A4 = 440
C0 = A4*pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

print('\nHappy Birthday : Tune...\n')

h = ['264', '264', '297', '264', '352', '330', '264', '264', '297', '264', '396', '352', '264', '264', '264', '440', '352', '352', '330', '297', '466', '466', '440', '352', '396', '352']

l = ['250', '250', '1000', '1000', '1000', '2000', '250', '250', '1000', '1000', '1000', '2000', '250', '250', '1000', '1000', '500', '250', '1000', '2000', '250', '250', '1000', '1000', '1000', '2000']

d = ['500', '250', '250', '250', '250', '500', '500', '250', '250', '250', '250', '500', '500', '250', '250', '250', '250', '250', '250', '500', '500', '250', '250', '250', '250', '250']

def pitch(fre):
	h = round(12*log2(fre/C0))
	octave = h // 12
	n = h % 12
	return name[n] + str(octave)

for i in range( len(h) ):
	print( pitch( float(h[i]) ))
	winsound.Beep( int(h[i]), int(l[i] ))
	time.sleep( int(d[i])/1000 )



# f = {'C#0': 17.32, 'D0': 18.35, 'D#0': 19.45, 'E0': 20.6, 'F0': 21.83, 'F#0': 23.12, 'G0': 24.5, 'G#0': 25.96, 'A0': 27.5, 'A#0': 29.14, 'B0': 30.87, 'C1': 32.7, 'C#1': 34.65, 'D1': 36.71, 'D#1': 38.89, 'E1': 41.2, 'F1': 43.65, 'F#1': 46.25, 'G1': 49.0, 'G#1': 51.91, 'A1': 55.0, 'A#1': 58.27, 'B1': 61.74, 'C2': 65.41, 'C#2': 69.3, 'D2': 73.42, 'D#2': 77.78, 'E2': 82.41, 'F2': 87.31, 'F#2': 92.5, 'G2': 98.0, 'G#2': 103.83, 'A2': 110.0, 'A#2': 116.54, 'B2': 123.47, 'C3': 130.81, 'C#3': 138.59, 'D3': 146.83, 'D#3': 155.56, 'E3': 164.81, 'F3': 174.61, 'F#3': 185.0, 'G3': 196.0, 'G#3': 207.65, 'A3': 220.0, 'A#3': 233.08, 'B3': 246.94, 'C4': 261.63, 'C#4': 277.18, 'D4': 293.66, 'D#4': 311.13, 'E4': 329.63, 'F4': 349.23, 'F#4': 369.99, 'G4': 392.0, 'G#4': 415.3, 'A4': 440.0, 'A#4': 466.16, 'B4': 493.88, 'C5': 523.25, 'C#5': 554.37, 'D5': 587.33, 'D#5': 622.25, 'E5': 659.26, 'F5': 698.46, 'F#5': 739.99, 'G5': 783.99, 'G#5': 830.61, 'A5': 880.0, 'A#5': 932.33, 'B5': 987.77, 'C6': 1046.5, 'C#6': 1108.73, 'D6': 1174.66, 'D#6': 1244.51, 'E6': 1318.51, 'F6': 1396.91, 'F#6': 1479.98, 'G6': 1567.98, 'G#6': 1661.22, 'A6': 1760.0, 'A#6': 1864.66, 'B6': 1975.53, 'C7': 2093.0, 'C#7': 2217.46, 'D7': 2349.32, 'D#7': 2489.02, 'E7': 2637.02, 'F7': 2793.83, 'F#7': 2959.96, 'G7': 3135.96, 'G#7': 3322.44, 'A7': 3520.0, 'A#7': 3729.31, 'B7': 3951.07, 'C8': 4186.01, 'C#8': 4434.92, 'D8': 4698.64, 'D#8': 4978.03, 'E8': 5274.04, 'F8': 5587.65, 'F#8': 5919.91, 'G8': 6271.93, 'G#8': 6644.88, 'A8': 7040.0, 'A#8': 7458.62, 'B8': 7902.13}

# m = ['D#5', 'D5', 'C5', 'C5', 'C5', 'C5,', 'F5', 'D5', 'A#4', 'A#4', 'A4', 'A#4', 'F4', 'G4', 'G#4', 'G#4', 'G#4', 'G#4', 'C5', 'D#5', 'C5', 'G#4', 'A#4', 'G#4', 'G4', 'G4', 'D#5', 'D5', 'C5', 'C5', 'C5', 'C5,', 'F5', 'D5', 'A#4', 'A#4', 'A4', 'A#4', 'F4', 'G4', 'G#4', 'G#4', 'G#4', 'G#4', 'C5', 'D#5', 'C5', 'G#4', 'A#4', 'G#4', 'G4', 'G4', 'C5', 'D5', 'D#5', 'F5', 'F5', 'F5', 'F5,', 'C5', 'D5', 'D5', 'D#5', 'D#5', 'D#5', 'D#5', 'D#5', 'C5', 'A#4', 'G#4', 'G#4', 'G#4', 'G#4', 'A#4', 'A#4', 'D5', 'D5', 'D#5', 'F5', 'D#5', 'D5', 'C5', 'C5', 'D#5', 'D5', 'C5', 'C5', 'C5', 'C5,', 'F5', 'D5', 'A#4', 'A#4', 'A4', 'A#4', 'F4', 'G4', 'G#4', 'G#4', 'G#4', 'G#4', 'C5', 'D#5', 'C5', 'G#4', 'A#4', 'G#4', 'G4', 'G4', 'D#5', 'D5', 'C5', 'C5', 'C5', 'C5,', 'F5', 'D5', 'A#4', 'A#4', 'A4', 'A#4', 'F4', 'G4', 'G#4', 'G#4', 'G#4', 'G#4', 'C5', 'D#5', 'C5', 'G#4', 'A#4', 'G#4', 'G4', 'G4', 'C5', 'D5', 'C5', 'D5', 'C5', 'A#4', 'C5', 'D5', 'C5', 'A#4', 'G#4', 'G4', 'C5', 'D5', 'D#5', 'G5', 'D#5', 'D5', 'A#4', 'C5', 'D5', 'C5', 'A#4', 'G#4', 'G4', 'C5', 'D5', 'C5', 'D5', 'C5', 'A#4', 'C5', 'D5', 'C5', 'A#4', 'G#4', 'G4', 'C5', 'D5', 'D#5', 'G5', 'D#5', 'D5', 'G4', 'A#4', 'C5', 'D5', 'D#5', 'F5', 'F5', 'F5', 'F5,', 'C5', 'D5', 'D5', 'D#5', 'D#5', 'D#5', 'D#5', 'D#5', 'C5', 'A#4', 'G#4', 'G#4', 'G#4', 'G#4', 'A#4', 'A#4', 'D5', 'D5', 'D#5', 'F5', 'D#5', 'D5', 'C5', 'C5', 'D#5', 'D5', 'C5', 'C5', 'C5', 'C5,', 'F5', 'D5', 'A#4', 'A#4', 'A4', 'A#4', 'F4', 'G4', 'G#4', 'G#4', 'G#4', 'G#4', 'C5', 'D#5', 'C5', 'G#4', 'A#4', 'G#4', 'G4', 'G4', 'D#5', 'D5', 'C5', 'C5', 'C5', 'C5,', 'F5', 'D5', 'A#4', 'A#4', 'A4', 'A#4', 'F4', 'G4', 'G#4', 'G#4', 'G#4', 'G#4', 'C5', 'D#5', 'C5', 'G#4', 'A#4', 'G#4', 'G4', 'G4']

# print('\nMere Raske Qamar : Tune...\n')

# for i in m:
# 	s = f.get(i)
# 	print(s)
# 	try:
# 		winsound.Beep(int(s), 1000)
# 	except Exception as e:
# 		print(e)
		

# from scipy.io import wavfile
# from scipy.fftpack import fft, fftfreq

# samplerate, data = wavfile.read("point.wav")
# samples = data.shape[0]
# print(samplerate, samples)

# datafft = fft(data)
# #Get the absolute value of real and complex component:
# fftabs = abs(datafft)
# freqs = fftfreq(samples,1/samplerate)
# print(fftabs, freqs)



# hbd = ''':beep frequency=264 length=250ms;
# :delay 500ms;
# :beep frequency=264 length=250ms;
# :delay 250ms;
# :beep frequency=297 length=1000ms;
# :delay 250ms;
# :beep frequency=264 length=1000ms;
# :delay 250ms;
# :beep frequency=352 length=1000ms;
# :delay 250ms;
# :beep frequency=330 length=2000ms;
# :delay 500ms;
# :beep frequency=264 length=250ms;
# :delay 500ms;
# :beep frequency=264 length=250ms;
# :delay 250ms;
# :beep frequency=297 length=1000ms;
# :delay 250ms;
# :beep frequency=264 length=1000ms;
# :delay 250ms;
# :beep frequency=396 length=1000ms;
# :delay 250ms;
# :beep frequency=352 length=2000ms;
# :delay 500ms;
# :beep frequency=264 length=250ms;
# :delay 500ms;
# :beep frequency=264 length=250ms;
# :delay 250ms;
# :beep frequency=264 length=1000ms;
# :delay 250ms;
# :beep frequency=440 length=1000ms;
# :delay 250ms;
# :beep frequency=352 length=500ms;
# :delay 250ms;
# :beep frequency=352 length=250ms;
# :delay 250ms;
# :beep frequency=330 length=1000ms;
# :delay 250ms;
# :beep frequency=297 length=2000ms;
# :delay 500ms;
# :beep frequency=466 length=250ms;
# :delay 500ms;
# :beep frequency=466 length=250ms;
# :delay 250ms;
# :beep frequency=440 length=1000ms;
# :delay 250ms;
# :beep frequency=352 length=1000ms;
# :delay 250ms;
# :beep frequency=396 length=1000ms;
# :delay 250ms;
# :beep frequency=352 length=2000ms;
# :delay 250ms;'''

# print()
# f = hbd.split('frequency')
# fb = []
# for i in f:
# 	f = i.split(' ')
# 	fb.append(f[0][1:])
# freq = fb[1:]
# print(freq)
# print()

# l = hbd.split('length')
# lb = []
# for i in l:
# 	j = i.split('ms;\n:delay')
# 	lb.append(j[0][1:])
# leng = lb[1:]
# print(leng)
# print()

# d = hbd.split(':delay ')
# db = []
# for i in d:
# 	j = i.split('\n')[0]
# 	db.append(j[:3])
# delay = db[1:]
# print(delay)

# from math import log2, pow
# import winsound, time

# A4 = 440
# C0 = A4*pow(2, -4.75)
# name = ["C", "C#", "D", "D#", "E",
#  "F", "F#", "G", "G#", "A", "A#", "B"]

# def pitch(fre):
# 	h = round(12*log2(fre/C0))
# 	octave = h // 12
# 	n = h % 12
# 	return name[n] + str(octave)

# #frequency = float(input('Enter frequency : '))

# print()
# for i in range(len(freq)):
# 	print(pitch(float(freq[i])))
# 	winsound.Beep(int(freq[i]), int(leng[i]))


# ===============================================================

# from scipy import fft, arange
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io import wavfile
# import os


# def frequency_sepectrum(x, sf):
#     """
#     Derive frequency spectrum of a signal from time domain
#     :param x: signal in the time domain
#     :param sf: sampling frequency
#     :returns frequencies and their content distribution
#     """
#     x = x - np.average(x)  # zero-centering

#     n = len(x)
#     print(n)
#     k = np.arange(n)
#     tarr = n / float(sf)
#     frqarr = k / float(tarr)  # two sides frequency range

#     frqarr = frqarr[range(n // 2)]  # one side frequency range

#     x = fft(x) / n  # fft computing and normalization
#     x = x[range(n // 2)]

#     return frqarr, abs(x)


# sr, signal = wavfile.read(r'C:\Users\Vicky\Downloads\01 - Ek Ladki Ko Dekha Toh Aisa Laga - DownloadMing.Se.wav')

# y = signal[:, 0]  # use the first channel (or take their average, alternatively)
# t = np.arange(len(y)) / float(sr)

# plt.figure()
# plt.subplot(2, 1, 1)
# plt.plot(t, y)
# plt.xlabel('t')
# plt.ylabel('y')

# frq, X = frequency_sepectrum(y, sr)

# plt.subplot(2, 1, 2)
# plt.plot(frq, X, 'b')
# plt.xlabel('Freq (Hz)')
# plt.ylabel('|X(freq)|')
# plt.tight_layout()

# plt.show()

# import winsound, time
# from math import log2, pow

# A4 = 440
# C0 = A4*pow(2, -4.75)
# name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# h = frq[-1710144:-171000:100]

# def pitch(fre):
#     try:
#         h = round(12*log2(fre/C0))
#         octave = h // 12
#         n = h % 12
#         return name[n] + str(octave)
#     except Exception as e:
#         print(e)
    
    
# for i in range( len(h) ):
#     print( pitch( float(h[i]) ), end = '\n{}). '.format(i))
#     try:
#         winsound.Beep( int(h[i]), 1000)
#     except Exception as e:
#         print(e)
    
#     time.sleep( int(d[i])/1000 )
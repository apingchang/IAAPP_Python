import numpy as np
import matplotlib.pyplot as plt
from scipy import pi
import os

#%matplotlib inline

sample_num = 44100*2 # Sampling points
total_time = 2 # Sampling number
sampling_rate = sample_num / total_time # 取樣頻率

fs = [(20, 12), (100, 5), (250, 2)] # sin 波的頻率與振幅組合。 (Hz, Amp)
noise_mag = 2

time = np.linspace(0, total_time, sample_num, endpoint=False)

vib_data = [amp * np.sin(2*pi*hz*time) for hz, amp in fs]

max_time = int(sample_num / 2)

plt.figure(figsize=(12, 8))
# Show seperated signal
for idx, vib in enumerate(vib_data):
    plt.subplot(2, 2, idx+1)
    plt.plot(time[0:max_time], vib[0:max_time])
    plt.xlabel('time')
    plt.ylabel('vib_' + str(idx))
    plt.ylim((-24, 24))

vib = sum(vib_data) + np.random.normal(0, noise_mag, sample_num) # Add noise

plt.subplot(2, 2, 4)
plt.plot(time[0:max_time], vib[0:max_time])
plt.xlabel('time')
plt.ylabel('vib(with noise)')
plt.ylim((-24, 24))
plt.show()

from scipy.fftpack import fft
import struct

fd = np.linspace(0.0, sampling_rate, int(sample_num), endpoint=False)
vib_Slice = [0] * (sample_num)
signalSlice = [0] * sample_num


#b = os.path.getsize('./testfreq.tmp')
#testFile = open('testfreq.tmp', "r")

#for i in range(b):
#    f = testFile.read()

#    if i<10:
#        print(f)
#    vib_Slice[i] = float(f)
    #
#testFile.close()

#print(type(vib_Slice[0]))

#for i in range(b):
#    signalSlice[i] = float(vib_Slice[i])

freqSpectrum = fft(vib)

mag = 2/sample_num * np.abs(freqSpectrum) # Magnitude

#mag = np.abs(freqSpectrum) # Magnitude

#for i in range (int(sample_num/2)) :
#    if mag[i]>1.9:
#        print(fd[i],mag[i])


plt.plot(fd[0:int(sample_num/2)], mag[0:int(sample_num/2)])
plt.plot(mag)

plt.xlabel('Hz')
plt.ylabel('Mag')

plt.show()
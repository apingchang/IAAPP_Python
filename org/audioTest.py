#!/usr/bin/env python3
"""Plot the live microphone signal(s) with matplotlib.
Matplotlib and NumPy have to be installed.
"""
import argparse
import queue
import sys
import wx

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
from scipy.fftpack import fft

# Set default value
downsample = 10
interval = 50       # animation interval in ms
channels = [1]      # Channel numbers start with 1
window = 200
device = None
samplerate = None
samplePeriod = 2


"""

def int_or_str(text):
#    Helper function for argument parsing.
    try:
        return int(text)
    except ValueError:
        return text


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    'channels', type=int, default=[1], nargs='*', metavar='CHANNEL',
    help='input channels to plot (default: the first)')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-w', '--window', type=float, default=200, metavar='DURATION',
    help='visible time slot (default: %(default)s ms)')
parser.add_argument(
    '-i', '--interval', type=float, default=30,
    help='minimum time between plot updates (default: %(default)s ms)')
parser.add_argument(
    '-b', '--blocksize', type=int, help='block size (in samples)')
parser.add_argument(
    '-r', '--samplerate', type=float, help='sampling rate of audio device')
parser.add_argument(
    '-n', '--downsample', type=int, default=10, metavar='N',
    help='display every Nth sample (default: %(default)s)')
args = parser.parse_args(remaining)


if any(c < 1 for c in channels):
    parser.error('argument CHANNEL: must be >= 1')


# device_info = sd.query_devices('input')
# print('device info:\n',device_info)

#device_info = sd.query_devices(device, 'input')
#print('device\n',device,'\ninfo\n',device_info)

"""

#mapping = [c - 1 for c in channels]  # Channel numbers start with 1

mapping = [c - 1 for c in channels]  # Channel numbers start with 1
print('Test: mapping = ',mapping)
q = queue.Queue()       # create an unlimited FIFO




def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""

    if status:
        print(status, file=sys.stderr)
    # Fancy indexing with mapping creates a (necessary!) copy:
    #q.put(indata[::downsample, mapping])
    #print('get',indata[::1, mapping],'length',len(indata))
    #q.put(indata[::1, mapping])
    q.put(indata)
    #print('.')




def update_plot(frame):
    """This is called by matplotlib for each plot update.
    Typically, audio callbacks happen more frequently than plot updates,
    therefore the queue tends to contain multiple blocks of audio data.
    """
    global plotdata
    global q2

    while True:
        try:
            data = q.get_nowait()

        except queue.Empty:
            break
        shift = len(data)

        #print('length data', shift)
        plotdata = np.roll(plotdata, -shift, axis=0)
        plotdata[-shift:, :] = data
        #plotdata[-shift:] = data

        #print('======================================')

    for column, line in enumerate(lines):
        line.set_ydata(plotdata[:, column])
        #line.set_ydata(plotdata[:])
    return lines


try:
    if samplerate is None:
        device_info = sd.query_devices(device, 'input')
        #print('device\n',device,'\ninfo\n',device_info)
        samplerate = device_info['default_samplerate']
        #print('sample rate =',samplerate)


    #length = int(window * samplerate / (1000 * downsample))
    sample_num = length = int(samplePeriod * samplerate)      # 5 sec. buffer for sampling data

    plotdata = np.zeros((length, len(channels)))


    print('plotodata length = ',len(plotdata))

    fig, ax = plt.subplots()
    lines = ax.plot(plotdata)
    if len(channels) > 1:
        ax.legend(['channel {}'.format(c) for c in channels],
                  loc='lower left', ncol=len(channels))
    ax.axis((0, len(plotdata), -1, 1))
    ax.set_yticks([0])
    ax.yaxis.grid(True)
    ax.tick_params(bottom=False, top=False, labelbottom=False,
                   right=False, left=False, labelleft=False)
    fig.tight_layout(pad=0)
    print('device:',device,'channel:',max(channels))
    stream = sd.InputStream(
        device=device, channels=max(channels),
        samplerate=samplerate, callback=audio_callback)


    ani = FuncAnimation(fig, update_plot, interval=interval, blit=True)

    with stream:
        plt.show()



    #wx.Sleep(1)             # sleep 5 second
  
    #sd.default.samplerate = samplerate
    #sd.play(plotdata)       # replay the last few second of the sound from micro phone


    #plt.plot(plotdata)      # plot the last few seconds sound signal
    #plt.show()

    #print('samplerate:',samplerate,'sample number:',sample_num)
    fd = np.linspace(0.0, samplerate, sample_num, endpoint=False)

    vib = [0]* int (sample_num)

    for i in range(sample_num):
        #print('check:',plotdata[i])
        #print(',',plotdata[i][0])
        vib[i] = plotdata[i][0]   # convert numpy array to sound data buffer


    vib_fft = fft(vib)
    mag = np.abs(vib_fft)  # Magnitude
    #mag = 2 / sample_num * np.abs(vib_fft)  # Magnitude
    freq = np.fft.fftfreq(sample_num, 1/samplerate)

    #plt.plot(mag)
    plt.plot(fd[0:int(sample_num / 2)], mag[0:int(sample_num / 2)])
    #plt.stem(freq[0:int(sample_num / 2)], mag[0:int(sample_num / 2)])
    plt.xlabel('Hz')
    plt.ylabel('Mag')
    plt.show()

    #print(freq)
    centerFreq = 0
    centerFreqMag = mag[0]
    for i in range(int(sample_num/2)):
        if (mag[i]>centerFreqMag):
            centerFreq = fd[i]
            centerFreqMag = mag[i]

    print('Primary Frequency = ', centerFreq)



    print('\nEnd')
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))

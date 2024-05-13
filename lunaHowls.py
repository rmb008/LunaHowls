####
####
####

#Import packages
import os
import subprocess
os.environ["XDG_SESSION_TYPE"] = "xcb"
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots
import seaborn as sns
import csv

import wave
import pydub
import scipy as sp
import sklearn

#########################################
## Read in data
##  Strip (whole duration) audio from .mp4 video files using ffmpeg
##  Save as .wav audio files
#########################################
#Greeting (Context 1) 3/5/21
command = "ffmpeg -i /home/rachel/Documents/CanisLupus/PXL_20210305_221651515.LS.mp4 -ab 160k -ac 2 -ar 44100 -vn /home/rachel/Documents/CanisLupus/PXL_20210305_221651515.wav"
subprocess.call(command, shell=True)

#Greeting (Context 1) 3/8/21
command = "ffmpeg -i /home/rachel/Documents/CanisLupus/PXL_20210308_221847475.LS.mp4 -ab 160k -ac 2 -ar 44100 -vn /home/rachel/Documents/CanisLupus/PXL_20210308_221847475.wav"
subprocess.call(command, shell=True)

#Greeting (Context 1) 3/9/21
command = "ffmpeg -i /home/rachel/Documents/CanisLupus/PXL_20210309_223422683.mp4 -ab 160k -ac 2 -ar 44100 -vn /home/rachel/Documents/CanisLupus/PXL_20210309_223422683.wav"
subprocess.call(command, shell=True)

#Cued (Context 2) 5/4/24
command = "ffmpeg -i /home/rachel/Documents/CanisLupus/PXL_20240504_013755915.mp4 -ab 160k -ac 2 -ar 44100 -vn /home/rachel/Documents/CanisLupus/PXL_20240504_013755915.wav"
subprocess.call(command, shell=True)

#Cued (Context 2) 5/8/24
command = "ffmpeg -i /home/rachel/Documents/CanisLupus/PXL_20240508_201240371.mp4 -ab 160k -ac 2 -ar 44100 -vn /home/rachel/Documents/CanisLupus/PXL_20240508_201240371.wav"
subprocess.call(command, shell=True)

#########################################
## Sample extraction
#########################################

from pydub import AudioSegment
from pydub.playback import play

#########################################
# Function callExtract
# Slice and dice audio from WAV file, save sample as .WAV file
# Inputs: 
#   wavIn = input WAV file name
#   t1 = start time for cut
#   t2 = end time for cut
#   wavOut = new WAV file name for saving audio clip
#
# Outputs: N/A
#########################################
def callExtract(wavIn, t1, t2, wavOut):
    t1 = t1 * 1000 #start in ms
    t2 = t2 * 1000 #end in ms
    #import audio
    woo = AudioSegment.from_wav(wavIn)
    #slice audio to vocalization event
    woo = woo[t1:t2]
    #save sample
    woo.export(wavOut, format = 'wav')
    
    return()
#########################################

# File: PXL_20210305_221651515.wav
wavIn = 'PXL_20210305_221651515.wav'
# Context: Luna + Sly. Luna greeting Sly; Luna has not seen Sly in several hours
# Date: 3/5/21
# Event times:
#   0:02-0:06
#   0:09-0:13
#   0:15-0:16
#   0:21-0:23
#   0:42-0:47
callExtract(wavIn, 2, 6, 'ev1_3521.wav')
callExtract(wavIn, 9, 13, 'ev2_3521.wav')
callExtract(wavIn, 15, 16, 'ev3_3521.wav')
callExtract(wavIn, 21, 23, 'ev4_3521.wav')
callExtract(wavIn, 42.5, 48, 'ev5_3521.wav')

#Playback to validate
play(AudioSegment.from_file('ev5_3521.wav', format="wav")) #woowoooowooowoo

# File: PXL_20210308_221847475.wav
wavIn = 'PXL_20210308_221847475.wav'
# Context: Luna + Sly
# Date: 3/8/21
# Event times:
#   0:01-0:03 
#   0:10-0:15
callExtract(wavIn, 1, 3, 'ev1_3821.wav')
callExtract(wavIn, 10, 15, 'ev2_3821.wav')

#Playback to validate
play(AudioSegment.from_file('ev1_3821.wav', format="wav"))

# File: PXL_20210309_223422683.wav
wavIn = 'PXL_20210309_223422683.wav'
# Context: Luna + Sly
# Date: 3/9/21
# Event times:
#   0:05-0:08
#   0:20-0:25
#   0:36-0:41
#   0:54-0:58
#   1:04-1:08
#   1:23-1:26
#   1:40-1:43
callExtract(wavIn, 5, 8, 'ev1_3921.wav')
callExtract(wavIn, 20, 25, 'ev2_3921.wav')
callExtract(wavIn, 36, 41, 'ev3_3921.wav')
callExtract(wavIn, 54, 15, 'ev4_3921.wav')
callExtract(wavIn, 64, 67, 'ev5_3921.wav')
callExtract(wavIn, 83, 86, 'ev6_3921.wav')
callExtract(wavIn, 101, 103.7, 'ev7_3921.wav')

#Playback to validate
play(AudioSegment.from_file('ev7_3921.wav', format="wav"))


# File: PXL_20240504_013755915.wav
wavIn = 'PXL_20240504_013755915.wav'
# Context: Luna - cued
# 'yes' praise often included

# Date: 5/4/24
# Event times:
#   0:51-0:52
#   01:31-01:32
#   01:37-01:38
#   02:18-02:19
#   02:32-02:33
#   02:40-02:41
callExtract(wavIn, 51.16, 51.8, 'ev1_5424.wav')
callExtract(wavIn, 91, 93, 'ev2_5424.wav')
callExtract(wavIn, 98, 99, 'ev3_5424.wav')
callExtract(wavIn, 138.5, 141, 'ev4_5424.wav')
callExtract(wavIn, 154, 155.5, 'ev5_5424.wav')
callExtract(wavIn, 160, 161, 'ev6_5424.wav')

#Playback to validate
play(AudioSegment.from_file('ev1_5424.wav', format="wav"))

# File: PXL_20240508_201240371.wav
wavIn = 'PXL_20240508_201240371.wav'
# Context: Luna - cued, includes commands (my voice)
# 'yes' praise often included
# Date: 5/8/24
# Event times:
#   0:5 - 0:15
#   0:18-0:19 frustrated
#   0:24-0:28
#   1:04-1:07 frustrated? voice
#   1:04-1:07 frustrated?
#   1:11-1:14
#   1:21-1:24
#   1:27-1:30
#   1:31-1:34
#   1:37-1:39
#   1:47-1:54
callExtract(wavIn, 5, 15, 'voice_ev1_5824.wav')
callExtract(wavIn, 17, 20, 'voice_ev2_5824.wav')
callExtract(wavIn, 24, 28, 'voice_ev3_5824.wav')
callExtract(wavIn, 63, 67, 'voice_ev4_5824.wav')
callExtract(wavIn, 71, 74, 'voice_ev5_5824.wav')
callExtract(wavIn, 81, 85, 'voice_ev6_5824.wav')
callExtract(wavIn, 87, 91.5, 'voice_ev7_5824.wav')    #awwooo
callExtract(wavIn, 91, 95, 'voice_ev8_5824.wav')
callExtract(wavIn, 97, 100, 'voice_ev9_5824.wav')
callExtract(wavIn, 108, 116, 'voice_ev10_5824.wav')

#Playback to validate
play(AudioSegment.from_file('voice_ev2_5824.wav', format="wav"))

# Context: Luna - cued, DOES NOT include commands (my voice)
callExtract(wavIn, 14, 15, 'ev1_5824.wav') #bark
callExtract(wavIn, 18.2, 19.3, 'ev2_5824.wav') #soft woof
callExtract(wavIn, 26.6, 27.4, 'ev3_5824.wav')
callExtract(wavIn, 66.3, 66.98, 'ev4_5824.wav')
callExtract(wavIn, 72.3, 73.4, 'ev5_5824.wav')
callExtract(wavIn, 83, 84.29, 'ev6_5824.wav')
callExtract(wavIn, 88.4, 90, 'ev7_5824.wav') #soft awoowoo, nails clicking
callExtract(wavIn, 93, 93.85, 'ev8_5824.wav') #sharper
callExtract(wavIn, 98.6, 99.9, 'ev9_5824.wav')
callExtract(wavIn, 112.5, 114, 'ev10_5824.wav')

#Playback to validate
play(AudioSegment.from_file('ev10_5824.wav', format="wav"))



#########################################
## Visualize some of the vocalizations
#########################################

#Set up plotting parameters
sns.color_palette()
plt.colormaps()
sns.set_theme(context = "paper", 
              style = 'darkgrid', 
              palette = 'viridis_r', 
              font = "serif", 
              font_scale = 1.5, 
              color_codes = True, 
              rc = None)
plt.rcParams['figure.dpi'] = 100


#########################################
# parselmouth tutorial
#https://parselmouth.readthedocs.io/_/downloads/en/stable/pdf/
#########################################
import parselmouth
snd = parselmouth.Sound('ev5_3521.wav')

play(AudioSegment.from_file('ev5_3521.wav', format = "wav"))

plt.figure(figsize = (9, 5))
plt.plot(snd.xs(), snd.values.T)
plt.xlim([snd.xmin, snd.xmax])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
plt.savefig("fig1_ev5_3521.png")

snd_part = snd.extract_part(from_time = 0.5, preserve_times = False)
plt.figure(figsize = (9, 5))
plt.plot(snd_part.xs(), snd_part.values.T, linewidth=0.5)
plt.xlim([snd_part.xmin, snd_part.xmax])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
plt.savefig("fig2_ev5_3521.png")

#Move extracted part to main part
snd = snd_part.copy()

def draw_spectrogram(spectrogram, dynamic_range=70):
    X, Y = spectrogram.x_grid(), spectrogram.y_grid()
    sg_db = 10 * np.log10(spectrogram.values)
    plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - dynamic_range, cmap='viridis')
    plt.ylim([spectrogram.ymin, spectrogram.ymax])
    plt.xlabel("Time [s]")
    plt.ylabel("Frequency [Hz]")

def draw_intensity(intensity):
    plt.plot(intensity.xs(), intensity.values.T, linewidth=3, color='w')
    plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
    plt.grid(False)
    plt.ylim(0)
    plt.ylabel("Intensity [dB]")
    

intensity = snd.to_intensity()
spectrogram = snd.to_spectrogram()
plt.figure(figsize = (9, 5))
draw_spectrogram(spectrogram)
plt.twinx()
draw_intensity(intensity)
plt.xlim([snd.xmin, snd.xmax])
plt.title('ev5_3521')
plt.show()
plt.savefig("fig3_ev5_3521.png")


def draw_pitch(pitch):
    # Extract selected pitch contour, and
    # replace unvoiced samples by NaN to not plot
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=5, color='w')
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=2)
    plt.grid(False)
    plt.ylim(0, pitch.ceiling)
    plt.ylabel("Fundamental frequency [Hz]")

pitch = snd.to_pitch()

# pre-emphasize sound fragment before calculating spectrogram
pre_emphasized_snd = snd.copy()
pre_emphasized_snd.pre_emphasize()
spectrogram = pre_emphasized_snd.to_spectrogram(window_length=0.03, maximum_frequency=9000)
plt.figure(figsize = (9, 5))
draw_spectrogram(spectrogram)
plt.twinx()
draw_pitch(pitch)
plt.xlim([snd.xmin, snd.xmax])
plt.title('ev5_3521')
plt.show()
plt.savefig("fig4_ev5_3521.png")

#Not preemphasized
spectrogram = snd.to_spectrogram(window_length=0.03, maximum_frequency=9000)
plt.figure(figsize = (9, 5))
draw_spectrogram(spectrogram)
plt.twinx()
draw_pitch(pitch)
plt.xlim([snd.xmin, snd.xmax])
plt.title('ev5_3521')
plt.show()
plt.savefig("fig5_ev5_3521.png")




























import numpy as np
import struct
import matplotlib.pyplot as plt
import pyaudio

N_SAMPLES = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
FS = 44100

P_obj = pyaudio.PyAudio()

Audio_stream = P_obj.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=FS,
    input=True,
    output=True,
    frames_per_buffer=N_SAMPLES
)

data = Audio_stream.read(N_SAMPLES)
data

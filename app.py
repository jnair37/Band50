import os

import math
import numpy
import pyaudio
import wave
from pydub import AudioSegment

# import jpype
# import jpype.imports
# from jpype.types import *

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

global numWavFiles

# Sets this so we can put a number in the file once we have multiple notes
numWavFiles = 0

def playNote(note, PyAudio, mode):

    freqs = [261.63, 293.66, 329.63, 349.23, 392.00, 440, 493.88]

    global numWavFiles

    if note == 9:
        numWavFiles = 0

    elif note == 8:
        # Reads from wav file and plays sound
        wavList = []
        if numWavFiles != 0:
            for i in range(numWavFiles):
                fileName = "test{j}.wav".format(j=i)
                wavList.append(AudioSegment.from_wav(fileName))
            finalFile = wavList[0]
            for i in range(1, len(wavList)):
                finalFile = finalFile + wavList[i]
                finalFile.export("test.wav", format="wav")

            f = wave.open("test.wav", 'rb')
            pl = PyAudio.open(format = pyaudio.paFloat32, channels=2, rate=44100, output=True)
            pl.write(f.readframes(100000*numWavFiles))
            pl.stop_stream()
            pl.close()
            f.close()

    else:
        # hz = 440 * math.pow(2, (note-4)/12)
        hz = freqs[note - 1]
        print(hz)
        n = waveform(hz, mode)
        print(len(n))

        # Plays sound immediately
        pl = PyAudio.open(format = pyaudio.paFloat32, channels=2, rate=44100, output=True)
        pl.write(n)
        pl.stop_stream()
        pl.close()

        # Writes to wav file
        writeToWav(n)

def playDrum(setting, PyAudio):
    if setting == 1:
        f = wave.open("audio/snap.wav", 'rb')
    elif setting == 2:
        f = wave.open("audio/kick.wav", 'rb')
    elif setting == 3:
        f = wave.open("audio/hat.wav", 'rb')
    else: 
        f = wave.open("audio/perc.wav", 'rb')
    pl = PyAudio.open(format = pyaudio.paFloat32, channels=2, rate=44100, output=True)
    pl.write(f.readframes(200000))
    writeToWav(f.readframes(200000))
    pl.stop_stream()
    pl.close()
    f.close()
    

def writeToWav(data):
    global numWavFiles
    fileName = "test{i}.wav".format(i=numWavFiles)
    numWavFiles += 1
    f = wave.open(fileName, 'wb')
    f.setnchannels(2)
    f.setnframes(len(data))
    f.setsampwidth(1)
    f.setframerate(44100)
    f.writeframes(data)
    f.close()


def waveform(hz, m):
    sampleRate = 44100.0 #define sample rate
    if m == 1:
        #generation of sine wave
        r = numpy.sin(numpy.pi*numpy.arange(0,50000,1)*(hz/sampleRate)) #formula for sine wave
        note = r.astype(numpy.float32)
    elif m == 2:
        #generation of sawtooth wave
        r = numpy.arctan(1/numpy.tan(numpy.pi*numpy.arange(0,50000,1)*hz/sampleRate)).astype(numpy.float32) #formula for sawtooth wave
        note = r.astype(numpy.float32)
    else:
        #generation of square wave
        r = numpy.round(numpy.sin(numpy.pi*numpy.arange(0,50000,1)*hz/sampleRate)) #formula for square wave, math loosely inspired by https://en.wikipedia.org/wiki/Square_wave, modified heavily to fit Numpy library
        note = r.astype(numpy.float32)
    return note #sends written audio to be played


# FLASK SETUP CODE FROM FINANCE:

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# New Flask code:


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/xylo", methods=["GET", "POST"])
def inst1():
    if (request.method=="POST"):
        PyAudio = pyaudio.PyAudio()
        playNote(int(request.form["button"]), PyAudio, 1)
        PyAudio.terminate()
    return render_template("xylo.html")

@app.route("/inst2", methods=["GET", "POST"])
def inst2():
    if (request.method=="POST"):
        PyAudio = pyaudio.PyAudio()
        playNote(int(request.form["button"]), PyAudio, 2)
        PyAudio.terminate()
    return render_template("inst2.html")

@app.route("/inst3", methods=["GET", "POST"])
def inst3():
    if (request.method=="POST"):
        PyAudio = pyaudio.PyAudio()
        playNote(int(request.form["button"]), PyAudio, 3)
        PyAudio.terminate()
    return render_template("inst3.html")

@app.route("/inst4", methods=["GET", "POST"])
def inst4():
    if (request.method=="POST"):
        PyAudio = pyaudio.PyAudio()
        playDrum(int(request.form["button"]), PyAudio)
        PyAudio.terminate()
    return render_template("inst4.html")






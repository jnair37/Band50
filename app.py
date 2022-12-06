import os

import math
import numpy
import pyaudio
import wave
from pydub import AudioSegment
import shutil

# import jpype
# import jpype.imports
# from jpype.types import *

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

global numWavFiles

# Sets this so we can put a number in the file once we have multiple notes
numWavFiles = 0

def writeToWav(n):
    global numWavFiles
    fileName = "test{i}.wav".format(i=numWavFiles)
    numWavFiles += 1
    f = wave.open(fileName, 'wb')
    f.setnchannels(2)
    f.setnframes(len(n))
    f.setsampwidth(1)
    f.setframerate(44100)
    f.writeframes(n)
    f.close()

def playSound(n, PyAudio):
    pl = PyAudio.open(format = pyaudio.paFloat32, channels=2, rate=44100, output=True)
    pl.write(n)
    pl.stop_stream()
    pl.close()

# Plays a note on one of the 3 non-drum-kit instruments (waveforms)
def playNote(note, PyAudio, mode):

    # Stores frequencies for white keys in order
    freqs = [261.63, 293.66, 329.63, 349.23, 392.00, 440, 493.88]

    global numWavFiles

    # CLEAR feature
    if note == 9:
        numWavFiles = 0

    # PLAYBACK feature
    elif note == 8:
        # Reads from wav file and plays sound
        wavList = []
        # Make sure there are some files to play
        if numWavFiles != 0:
            # Append all the files to test.wav
            for i in range(numWavFiles):
                fileName = "test{j}.wav".format(j=i)
                wavList.append(AudioSegment.from_wav(fileName))
            finalFile = wavList[0]
            for i in range(1, len(wavList)):
                finalFile = finalFile + wavList[i]
                finalFile.export("test.wav", format="wav")
            

            # Play test.wav
            f = wave.open("test.wav", 'rb')
            pl = PyAudio.open(format = pyaudio.paFloat32, channels=2, rate=44100, output=True)
            pl.write(f.readframes(100000*numWavFiles))
            pl.stop_stream()
            pl.close()
            f.close()

    # Note clicked
    else:
        # Calculate frequency, synthesize waveform
        hz = freqs[note - 1]
        print(hz)
        n = waveform(hz, mode)
        print(len(n))

        # Play sound immediately
        playSound(n, PyAudio)

        # Writes to wav file
        writeToWav(n)

# Synthesize a drum sound based on input
def drumSound(mode):
    if mode == 8 or mode == 9:
        print("this has been called.")
    sampleRate = 44100.0
    fileLen = 20000

    # Snap
    if mode == 1:
        r = numpy.zeros(fileLen)
        for i in range(231):
            r[i] = numpy.sin(numpy.pi*i*(6000-i*3)/sampleRate)
        note = r.astype(numpy.float32)

    # Kick
    elif mode == 2:
        r = numpy.zeros(fileLen)
        for i in range(96):
            r[i] = numpy.sin(numpy.pi*i*(6000-i*3)/sampleRate)
        for i in range(300):
            r[i] = numpy.sin(numpy.pi*i*(60)/sampleRate)
        note = r.astype(numpy.float32)
    
    # Hat
    elif mode == 3:
        r = numpy.zeros(fileLen)
        for i in range(801):
            r[i] = numpy.sin(numpy.pi*i*(18000)/sampleRate)
        note = r.astype(numpy.float32)
    
    # Laser
    else:
        r = numpy.zeros(fileLen)
        for i in range(3001):
            r[i] = numpy.sin(numpy.pi*i*(2000+i*2)/sampleRate)
        note = r.astype(numpy.float32)
    return note

# Plays drums from drum kit; drum beats are a set of pre-created files generated using Sound.java(?)
def playDrum(setting, PyAudio):

    global numWavFiles

    if setting == 8 or setting == 9:
        print("play drum has been called.")
    n = drumSound(setting)
    
    # Play sound aloud immediately
    playSound(n, PyAudio)

    # Write to wav file
    writeToWav(n)

def waveform(hz, m):
    sampleRate = 44100.0 #define sample rate
    if m == 1:
        #generation of sine wave
        r = numpy.sin(numpy.pi*numpy.arange(0,50000,1)*(hz/sampleRate)) #formula for sine wave
    elif m == 2:
        #generation of square wave
        r = numpy.round(numpy.sin(numpy.pi*numpy.arange(0,50000,1)*hz/sampleRate)) #formula for square wave, math loosely inspired by https://en.wikipedia.org/wiki/Square_wave, modified heavily to fit Numpy library
    else:
         #generation of sawtooth wave
        r = numpy.arctan(1/numpy.tan(numpy.pi*numpy.arange(0,50000,1)*hz/sampleRate)) #formula for sawtooth wave
    note = r.astype(numpy.float32)

    return note #sends written audio to be played


# FLASK SETUP CODE FROM FINANCE:

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# New Flask code:

# Basic renders for index and about pages
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


# POST is used when a button has been pressed, so this both renders
# the page and responds appropriately to button inputs
@app.route("/inst1", methods=["GET", "POST"])
def inst1():
    if (request.method=="POST"):
        PyAudio = pyaudio.PyAudio()
        playNote(int(request.form["button"]), PyAudio, 1)
        PyAudio.terminate()
    return render_template("inst1.html")


# Same for other instruments
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
        # If we're pressing playback or clear, then we call playNote() anyway
        if request.form["button"] == "8" or request.form["button"] == "9":
            playNote(int(request.form["button"]), PyAudio, 4)
        else:
            playDrum(int(request.form["button"]), PyAudio)
        PyAudio.terminate()
    return render_template("inst4.html")






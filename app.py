# FLASK SETUP CODE FROM FINANCE:

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
        fileName = "test{i}.wav".format(i=numWavFiles)
        numWavFiles += 1
        f = wave.open(fileName, 'wb')
        f.setnchannels(2)
        f.setnframes(len(n))
        f.setsampwidth(1)
        f.setframerate(44100)
        f.writeframes(n)
        f.close()

    # pl = PyAudio.open(format = PyAudio.get_format_from_width(width=1), channels=2, rate=44100, input=True, frames_per_buffer=1024)

    # soundStore = []
    # for i in range(44100//1024):
    #     test = pl.read(1024)
    #     soundStore.append(test)
    # #print(soundStore)
    # soundStore = bytes(soundStore)
    # print(type(soundStore))

    # pl.stop_stream()
    # pl.close()
    
    # pl = PyAudio.open(format = PyAudio.get_format_from_width(width=1), channels=2, rate=44100, output=True)
    # pl.write(soundStore)
    # pl.stop_stream()
    # pl.close()


def waveform(hz, m):
    sampleRate = 44100.0
    if m == 1:
        note = numpy.sin(numpy.pi*numpy.arange(0,50000,1)*(hz/sampleRate)).astype(numpy.float32)
    elif m == 2:
        note = numpy.arctan(1/numpy.tan(numpy.pi*numpy.arange(0,50000,1)*hz/sampleRate)).astype(numpy.float32)
    else:
        r = numpy.round(numpy.sin(numpy.pi*numpy.arange(0,50000,1)*hz/sampleRate))
        note = r.astype(numpy.float32);
    return note



# jpype.startJVM(classpath=['../target/sound.jar'])

# from target import Sound;

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Sets this so we can put a number in the file once we have multiple notes
numWavFiles = 0

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# New flask !

# @app.route("/play")
# def playFromSite(note):
#     PyAudio = pyaudio.PyAudio()
#     playNote(note, PyAudio)
#     PyAudio.terminate()

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

@app.route("/inst4")
def inst4():
    return render_template("inst4.html")






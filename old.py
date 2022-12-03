# FLASK SETUP CODE FROM FINANCE:

import os

import math
import numpy
import pyaudio
import wave

# import jpype
# import jpype.imports
# from jpype.types import *

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

def playNote(note, PyAudio):

    if note == 8:
        # Reads from wav file and plays sound
        f = wave.open("test.wav", 'rb')
        pl = PyAudio.open(format = PyAudio.get_format_from_width(width=1), channels=2, rate=44100, output=True)
        pl.write(f.readframes(100000))
        pl.stop_stream()
        pl.close()
        f.close()

    else:
        hz = 440 * math.pow(2, (note-4)/12)
        print(hz)
        n = sine(hz)
        print(len(n))

        # Plays sound immediately
        pl = PyAudio.open(format = pyaudio.paFloat32, channels=2, rate=44100, output=True)
        pl.write(n)
        pl.stop_stream()
        pl.close()

        # Writes to wav file
        f = wave.open("test.wav", 'wb')
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


def sine(hz):
    sampleRate = 44100.0
    note = numpy.sin(numpy.pi*numpy.arange(5000)*(hz/sampleRate)).astype(numpy.float32)
    return note



# jpype.startJVM(classpath=['../target/sound.jar'])

# from target import Sound;

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

# New flask !

@app.route("/play")
def playFromSite(note):
    PyAudio = pyaudio.PyAudio()
    playNote(note, PyAudio)
    PyAudio.terminate()

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
        playNote(int(request.form["button"]), PyAudio)
        PyAudio.terminate()
    return render_template("xylo.html")

@app.route("/inst2")
def inst2():
    return render_template("inst2.html")

@app.route("/inst3")
def inst3():
    return render_template("inst2.html")

@app.route("/inst4")
def inst4():
    return render_template("inst2.html")






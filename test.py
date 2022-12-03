import math
import pyaudio


def playNote(note):
    hz = 440 * math.pow(2, (note-4)/12)
    print(hz)
    n = bytes(sine(hz))

    pl = PyAudio.open(format = PyAudio.get_format_from_width(width=1), channels=2, rate=44100, output=True)
    pl.write(n)
    pl.stop_stream()
    pl.close()

def sine(hz):
    sampleRate = 44100.0
    note = []
    for i in range(50000):
        note.append(abs(round(math.sin(math.pi*i*(hz/sampleRate)))))
    return note


PyAudio = pyaudio.PyAudio()

playNote(4)
PyAudio.terminate()

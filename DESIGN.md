# Design Documentation

## Components
* Interactive interface
* Sound synthesis

### Interactive Interface

We used HTML, CSS, and Flask to create an interactive web-based user interface for the platform. 

#### Design Decisions
* HTML inheritance(?): We extended all the webpages from `layout.html`, including another template, `inst.html`, from which the four instrument pages all extended. This reduced redundancy and made it easier to make formatting changes to many pages on the website at a time.
* Bootstrap Components: We used a lot of Bootstrap components and Bootstrap CSS classes in order to improve the website's aesthetics and organization. Components / classes used include:
    * Navbar (component)
    * display-1, display-2, lead (display fonts)
    * ml-2 (margins)
    * text-center, text-left (alignment)
    * Row, col, card
    * Note; lot of redundancy to be removed probably
* 
* Writing to individual `.wav` files -- will make it easier to overlay stuff later
    * We could also delete one note at a time lol
* Each instrument on a separate webpage: felt like an intuitive way of ...
* Buttons for notes -- definitely a process to get here.

### Sound Synthesis

We used Python with the library PortAudio, through PyAudio.

#### Design Decisions
* We synthesized all melodic (sine, saw, and square) sounds in 'app.py', inside of 'def waveform'. There, we used the NumPy library to generate ndarrays (created using Numpy) that were later written to a waveform. We synthesized drum sounds inside of a separate function to ensure that they could be overlaid. The drum sounds were more complexed, and they were synthesized through creating formulas to adjust the frequency of the waveforms over the length of the ndarray (created using Numpy) later written to a waveform.
* We mapped buttons to notes on the keyboard by using the algorithm in 'def playNote' to convert arbitrary numerical input into a specific frequency corresponding with the labelled note on the button pressed. This allowed for easy mapping that could be consistent across disparate sounds.

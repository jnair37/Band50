# Design Documentation

## Components
* Interactive interface
* Sound synthesis

### Interactive Interface

We used HTML, CSS, and Flask to create an interactive web-based user interface for the platform. 

#### Design Decisions
* Using Flask: Since we wanted a very interactive web interface as well as complex sound generation algorithms in the back end, it made the most sense to integrate Python code with HTML/CSS using Flask.
* Basic structure: We decided to include a home page which would link to each instrument, an about page which would explain how to use the platform, and a page for each instrument as well as a navbar with a dropdown so that users could easily switch between instruments and play back their work at any time. 
* HTML templating/extending: We extended all the webpages from `layout.html`, including another template, `inst.html`, from which the four instrument pages all extended. This reduced redundancy and made it easier to implement formatting changes to many pages on the website at a time.
* Bootstrap Components: We used several of Bootstrap's components and CSS classes in order to improve the website's aesthetics and organization. 
    * Navbar (component used in layout.html)
    * `display-1`, `display-2`, `lead` (display fonts)
    * `ml-2` (margins)
    * `text-center`, `text-left` (alignment)
    * `row`, `col`, `card` (cards on home page)
    * `btn` and `btn-primary` (buttons)
* We created buttons to represent each note in the C Major scale. We chose this scale and these notes to simplify usage for users who may not have been exposed to music theory. Each button is labelled with its note and a numerical value, which is then interpreted in 'app.py', where it is either used to calculate a frequency value or used as an indicator to play back or clear audio. For the drum kit, we used similar buttons that, instead of representing notes on the scale, represented elements of a drum kit, and we labelled these buttons as such.
* We wrote each note the user played to a separate `.wav` file and combined them for the "PLAYBACK" function. This was because one of our original "better" goals was to include the ability to overlay different instruments simultaneously, and having the files already separated out would make it easier to add this feature. Although we faced issues with this feature and were not able to make this work reliably within the timeframe of the project, we tried to make our design as conducive to iterative changes as possible, so we could add features on top.

### Sound Synthesis

We used Python with the library PortAudio, through PyAudio. 

#### Design Decisions
* We synthesized all melodic (sine, saw, and square) sounds in 'app.py', inside of 'def waveform'. There, we used the NumPy library to generate ndarrays (created using Numpy) that were later written to a waveform. 
* We synthesized drum sounds inside of a separate function to ensure that they could be overlaid. The drum sounds were more complexed, and they were synthesized through creating formulas to adjust the frequency of the waveforms over the length of the ndarray (created using Numpy) later written to a waveform.
* We mapped buttons to notes on the keyboard by using the algorithm in 'def playNote' to convert arbitrary numerical input into a specific frequency corresponding with the labelled note on the button pressed. This allowed for easy mapping that could be consistent across disparate sounds.
* The sound synthesis algorithm was originally written in Java, and at first we tried to package the Java code such that it would work with Python, but eventually realized that it was possible to create the same effects in Python directly.
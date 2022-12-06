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

### Our Process

Our Process

* We began with basic code for generation of sound in Java that Cliff had written previously. We heavily modified this code to interact with the original sketch of the project (with an image of a xylophone) and take numerical input instead of MIDI input. 
* On the front-end side, we started out by trying to map the user’s clicks on an image of a xylophone to the sound. First, we tried literally cropping the image into each of its pieces and displaying them together so that each “note” was one separate image that the user could click on. We weren’t really satisfied with how this looked display-wise, so we looked for an alternate solution and found HTML’s <map> tag, which would allow us to map pixelated regions of an image. However, we had a lot of trouble getting this tag to interact with Flask as a form. Eventually, we decided to go with buttons to represent the notes rather than the instrument image display we had originally decided on, and we chose the C Major scale. We used Bootstrap to make these buttons look more aesthetic and to give the website an overall more organized look. 
*Returning to the back-end, we attempted to package the code as a .jar file, but realized that it may be simpler to translate the code to Python using the PortAudio library through PyAudio. We learned how to use this library, but ran into a roadblock when we attempted to loop through the array of sound using functions from the Math library. We found the solution to this problem; the NumPy library, which would allow us to use ndarrays instead of regular arrays, allowing for PyAudio to interpret the input into data. The only caveat with this was we had to use numpy’s ‘arange’ rather than a loop to create the ndarray in the correct format. 
* Perfecting the algorithms in Python was challenging, especially with the drum sounds. These presented another challenge because we had to use arange, but the drum sounds changed over time, and so they needed to be calculated in a for loop, as opposed to a one-liner within ‘arange’. Therefore, we synthesized these sounds in Java and tried to save the .wav files directly into the project and have Python just play them from the files. However, we ran into issues because Java saves .wav files as 16 bit integers while Python needs them as 32 bit floats. After a lot of trial and error, we realized there was actually a way to use a for loop in Python to successfully create the sound in an ndarray directly. 
* We incorporated the drums into Python, and subsequently tried to add the overlay functionality where we could play the drums simultaneously with the notes. However, this caused more issues as overlaying using AudioSegment distorted the sound considerably. At this point, we were running out of time and decided it was best to focus on completing the documentation and video before the submission deadline rather than adding another module, and we liked how the project turned out. We learned a lot about debugging, troubleshooting and adapting to the varying needs of a project within a timeline, and we are happy with the scale of the project and hope you enjoy it.




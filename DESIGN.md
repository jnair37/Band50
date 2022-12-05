# Design Documentation

## Components
* Interactive interface
* Sound synthesis

### Interactive Interface

We used HTML, CSS, and Flask to create an interactive web-based user interface for the platform. 

#### Design Decisions
* HTML extending: We extended all the webpages from `layout.html`, including another template, `inst.html`, from which the four instrument pages all extended. This reduced redundancy and made it easier
to make formatting changes to many pages on the website at a time.
* I literally can't think of any others lol
* Writing to individual `.wav` files -- will make it easier to overlay stuff later
    * We could also delete one note at a time lol
* Uhhhh what else

### Sound Synthesis
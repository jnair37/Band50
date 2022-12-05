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
    * Note; lot of redundancy to be removed probably
* 
* Writing to individual `.wav` files -- will make it easier to overlay stuff later
    * We could also delete one note at a time lol
* Each instrument on a separate webpage: felt like an intuitive way of ...
* Buttons for notes -- definitely a process to get here.

### Sound Synthesis
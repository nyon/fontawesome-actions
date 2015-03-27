Work in progress

# Usage

Just copy the fonts and css folder to your project and use them like the normal Font Awesome. 


# Contribute
Be aware, that contributing means installing a lot of dependencies. The following install guide is for debian-based systems but could be easily ported to other systems (contribution appreciated!).

## Prerequisites

Download and compile font forge:
    
    git clone https://github.com/fontforge/fontforge.git
    cd fontforge
    sudo apt-get install packaging-dev pkg-config python-dev libpango1.0-dev libglib2.0-dev libxml2-dev giflib-dbg libjpeg-dev libtiff-dev uthash-dev libspiro-dev
    ./bootstrap
    ./configure --enable-python-scripting --enable-python-extension
    make
    sudo make install
    sudo ldconfig

Clone this repository

    git clone --recursive https://github.com/nyon/fontawesome-actions.git
    cd fontawesome-actions

## Run

Edit settings in main.py as you like and run main.py

    python main.py



# Thanks

Thanks @davegandy and @tagliala for making and managing [Font Awesome](http://fontawesome.io).

Thanks @google for supporting webfonts and providing an easy way to compress them to [woff2](https://github.com/google/woff2).

Thanks George Williams and all contributors of [fontforge](https://fontforge.github.io/en-US/). 

Thanks taviso for providing an easy way to convert [ttf2eot](https://code.google.com/p/ttf2eot/).
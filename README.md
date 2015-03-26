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

Install node packet manager

    sudo apt-get install npm node
    sudo npm install -g ttf2eot

Clone this repository

    git clone --recursive https://github.com/nyon/fontawesome-actions.git
    cd fontawesome-actions
    python main.py

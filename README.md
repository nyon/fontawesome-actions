# Usage

Just copy the fonts and css folder to your project and use them like the normal Font Awesome. 

You can still use Font Awesome as before:

    <i class="fa fa-folder"></i>

With fontawesome-actions you can combine two icons into an action icon. Several icons are precompiled. See the CSS-file for the full list (when this is stable, a list will be released):

    <i class="fa fa-folder-plus fa-2x"></i>

![simple example](https://raw.github.com/nyon/fontawesome-actions/master/demo/simple.png)

But even better, you can also combine two icons in a stack and use color on each seperate part. Just use the alpha and beta suffix:

    <span class="fa-stack">
      <i class="fa fa-folder-plus-alpha fa-2x fa-stack-1x"></i>
      <i class="fa fa-folder-plus-beta fa-2x fa-stack-1x" style="color: #F012BE;"></i>
    </span>

![stacked example](https://raw.github.com/nyon/fontawesome-actions/master/demo/stacked.png)

Another feature is the possibility to slash out icons, similar to the effect shown by the normal fa-bell-slash:

    <i class="fa fa-folder-slash fa-2x"></i>

![slashed example](https://raw.github.com/nyon/fontawesome-actions/master/demo/slashed.png)


# Customize
Be aware, that customizing means installing a lot of dependencies. The following install guide is for debian-based systems but could be easily ported to other systems (contribution appreciated!).

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
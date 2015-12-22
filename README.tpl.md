# Introduction

This repository contains a superset of Dave Gandy's FontAwesome icons. It is based on FontAwesome [[VERSION]] and extends
the original [[ORIG-COUNT]] icons to a total amount of ~[[NEW-COUNT]]. See the bottom of this document for a list of all icons.

# Installation

## Static

Just copy the fonts and css folder to your project and use them like the normal Font Awesome.

## With bower

    bower install fontawesome-actions

## With bundler < 1.8.4

Edit your Gemfile:

    # At the top
    source 'https://rails-assets.org'

    # somewhere in your Gemfile
    gem 'rails-assets-fontawesome-actions'

Then run

    bundle

And include the following in application.css

    *= require fontawesome-actions

## With bundler >= 1.8.4

Edit your Gemfile:

    # somewhere in your Gemfile
    source 'https://rails-assets.org' do
      gem 'rails-assets-fontawesome-actions'
    end

Then run

    bundle

And include the following in application.css

    *= require fontawesome-actions

# Usage

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

As some icons got no outline version, this project tries to implement these automatically. So some of the icons also support the -o suffix:

    <i class="fa fa-comment-o fa-2x"></i>

![stroked example](https://raw.github.com/nyon/fontawesome-actions/master/demo/stroked.png)


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

Thanks Yahoo! Inc. and Yury Selivanov for providing and porting the YUI css minimizer [csscompressor](https://pypi.python.org/pypi/csscompressor).

# Icon list

You can clone this repository and open demo.html for a full graphical representation of all icons.


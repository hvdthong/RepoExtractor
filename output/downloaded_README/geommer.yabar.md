# Yabar

A modern and lightweight status bar for X window managers.
[![Build Status](https://travis-ci.org/geommer/yabar.svg?branch=master)](https://travis-ci.org/geommer/yabar)

## Screenshots

![screen 01](examples/screenshots/scr01.png)
![screen 02](examples/screenshots/scr02.png)
![screen 03](examples/screenshots/scr03.png)

## Description

Yabar is a modern and lightweight status bar that is intended to be used along with minimal X window managers like `bspwm` and `i3`. Yabar has the following features:

* Extremely configurable with easy configuration system using a single config file.
* A growing set of ready-to-use internal blocks developed in plain c.
* Pango font rendering with support of [Pango Markup Language](https://developer.gnome.org/pango/stable/PangoMarkupFormat.html).
* Support for icons and images.
* Support for transparency.
* Multi-monitor support using RandR.
* Entirely clickable.
* Support for several environment variables to help button commands.
* Multiple bars within the same session.

**Warning**: Yabar is still in its infancy and far from being mature. Feel free to contribute or report bugs!

## Terminology

A Yabar session should contain one or more *bars* within the same session. Each bar should contain one or more *blocks*. Each block should display some useful info to the user (free memory, CPU temperature, etc...).

## Installation

### Packages

#### ArchLinux

AUR: [yabar](https://aur.archlinux.org/packages/yabar/) and [yabar-git](https://aur.archlinux.org/packages/yabar-git/)

#### Debian

Yabar is available in the official repositories since Debian Stretch (9.0):
```sh
# apt install yabar
```

#### Ubuntu

[yabar](http://packages.ubuntu.com/search?keywords=yabar&searchon=names&suite=all&section=all) in [Yakkety Yak](http://packages.ubuntu.com/yakkety/yabar)

#### NixOS / Nix

[yabar](https://nixos.org/nixos/packages.html#yabar) is available in the official `nixpkgs` package set and can be installed easily:

```sh
nix-env -iA nixos.yabar
```

Since NixOS 18.03 (Impala) there's a [yabar-unstable](https://github.com/NixOS/nixpkgs/blob/master/pkgs/applications/window-managers/yabar/unstable.nix) package which is built from the latest master.

### From Source
Yabar initially requires a C compiler (e.g. gcc or clang), make as well as the libraries libconfig, cairo, pango and alsa. The feature `DYA_INTERNAL_EWMH` in `Makefile` additionaly xcb-ewmh (or xcb-util-wm in some distros) and the feature `-DYA_ICON` requires gdk-pixbuf2. These dependencies can be installed through your distribution's package manager:

* Fedora: `dnf install libconfig-devel cairo-devel pango-devel gdk-pixbuf2-devel alsa-lib-devel xcb-util-wm-devel wireless-tools-devel libxkbcommon-devel libxkbcommon-x11-devel asciidoc`
* Debian / Ubuntu: `apt-get install libcairo2-dev libpango1.0-dev libconfig-dev libxcb-randr0-dev libxcb-ewmh-dev libxcb-icccm4-dev libgdk-pixbuf2.0-dev libasound2-dev libiw-dev libxkbcommon-dev libxkbcommon-x11-dev libxcb-xkb-dev`

You can install yabar as follows:

		$ git clone https://github.com/geommer/yabar
		$ cd yabar
		$ make yabar
		$ sudo make install

If you use libconfig 1.4.x (still used in Ubuntu 14.04 and Debian Jessie), please type `export CPPFLAGS=-DOLD_LIBCONFIG` then build using `make` as usual.

Building the documentation (man page) requires AsciiDoc and a few other dependencies: `asciidoc docbook-xml xsltproc`

		$ make docs

This will generate the yabar man page inside `doc/yabar.1`.

## Configuration

Please see [our documentation](doc/yabar.1.asciidoc) for in-depth configuration details. Also check the provided [example configuration](examples/example.config).

## License

Yabar is licensed under the MIT license. For more info check out the file `LICENSE`.

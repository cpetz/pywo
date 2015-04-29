# PyWO - Python Window Organizer #

## Introduction ##
PyWO allows you to easily organize windows on the desktop using keyboard shortcuts. It's inspired by Quicktile, Compiz plugins: Grid, Put, and Maximumize.

## Features: ##
  * Move window in any direction and snap it to other windows' edges
  * Resize (expand or shrink) window in any direction
  * Place window in predefined places on the desktop
  * Use grid-like layout (place window and cycle predefined sizes)
  * Switch windows' positions
  * Highly customizable

Watch [PyWO in action](PywoInAction.md)

## Download ##
Download archive with PyWO-0.2 for stable version.

Checkout project's Subversion repository for development version (`/trunk` folder). This version contains latest features and bugfixes, but I can't guarantee that it will be stable!

## Requirements ##
You need Python 2.5 or higher with [python-xlib](http://python-xlib.sourceforge.net/) module installed (on Ubuntu you need to install `python-xlib` package).

PyWO works with (or at least should work with) any EWMH compliant window manager.

Seems to work OK (or almost OK) with:
  * Compiz _(tested with 0.7.8, and 0.8.4)_ (does not work with 0.9.x used by Unity)
  * Metacity _(tested with 2.24 and 2.30.1)_
  * KDE (KWin) _(tested with 4.3.0)_
  * XFCE (Xfwm4) _(tested with 4.6.1)_
  * Enlightment (e16) _(tested with 1.0.0)_
  * Openbox _(tested with 3.4.10)_
  * FVWM _(tested with 2.5.28)_

In 0.2 version there are problems with:
  * Blackox _(tested with 0.70.1)_, IceWM _(tested with 1.36)_ - no support for `_NET_FRAME_EXTENTS`, but I should be able to write a hack to get borders' size anyway _(fixed in development version)_
  * Fluxbox _(tested with 1.1.1)_, WindowMaker - window is moved 1px (to right and bottom) too far, not sure why... _(fixed in development version)_
  * Sawfish _(tested with 1.3.5.2)_ - _(fixed in development version)_
  * pekwm _(tested with 0.1.11)_ - some strange behaviour _(fixed in development version)_
  * JWM - some strange behaviour
  * Afterstep - `_NET_WORKAREA` returns None

Development version works OK with GNOME 3 (Mutter)

## Usage ##
Just run `./pywo.py`

Create `~/.pyworc` file to configure PyWO. Read [PyWO Configuration](PywoConfiguration.md) for reference. Defaults can be found in `pyworc` file. You can choose one of the predefined grid layouts: 2x2, 3x2 (default), 3x3, or define your own.

PyWO creates `/tmp/PyWO.log` file where all debugging informations are logged.

#### Default keyboard shortcuts: ####
```
Alt-Ctrl-Shift-Q    - exit PyWO
Alt-Ctrl-Shift-R    - reload configuration file
Alt-Ctrl-Shift-I    - print debug information about window manager and current window

Alt-KP_Divide       - switch windows (change position of the window)
Alt-Shift-KP_Divide - cycle windows (change contents of the window)

Alt-KP_1-9          - move window in a direction (KP_1-9 - numpad keys)
Shift-KP_1-9        - expand window in a direction (5 works as maximumize compiz plugin)
Alt-Shift-KP_1-9    - shrink window
Alt-Ctrl-KP_1-9     - put window to predefined position
Ctrl_KP_1-9         - put and resize (grid), and cycle widths
Ctrl-Shift_KP_1-9   - put and resize (grid), and cycle heights
```

Cycle/Switch - press keyboard shortcut and select other window (using Alt-Tab, or using mouse). If you want to cancel switch/cycle press again the keyboard shortcut

## Known bugs ##
  * shrinking with MIDDLE direction is not always working as expected
  * windows set to appear on all desktops can cause some problems _(fixed in development version)_
  * problems with windows with border\_width > 0

## TODO ##
  * ~~keyboard setting for laptop users (withou keypad) - maybe vim like HJKL, or UIOJKLM<>?~~
  * Undo feature
  * test with more than one monitor connected - if you want to help me with multi monitor support please send me output of [this script](http://dl.dropbox.com/u/69843/Xlib_test/screen_info.py) - it will check diplays, screens, resolutions
  * more settings for move and expand actions
  * ~~prepare for easy\_install~~ _(implemented in development version)_
  * ~~use `pkg_resources` and `entry_points` for plugins system~~ _(implemented in development version)_
  * snap only to visible windows only (skip windows that are covered by others)
  * unit testing _(in progress)_
  * ~~add D-Bus communication~~ _(implemented in development version)_

## Changelog ##
**developmnet version** (check out `/trunk` from repository)
  * fixed support for Fluxbox, Blackbox, IceWM, Sawfish, Window Maker, pekwm
  * fixed handling of sticky windows
  * added `capslock` setting
  * grid\_2x2 and grid\_3x2 ignore grid\_height action by default
  * new actions: activate, close, sticky, shade, fullscreen, maximize(_vert|_horz), iconify, above, below
  * aliases for action and section names
  * D-Bus communication with PyWO
  * matching windows by name, and classname
  * commandline support (similar to wmctrl)
  * distribution as Python package (easy\_install / pip support)
  * major refactoring - it is now possible to use pywo as wrapper for Xlib library
  * support for third-party plugins
  * modal mode - for use without keypad
  * Xinerama support

**0.2**
  * added switch and cycle actions
  * added `ignore` options for `[SETTINGS]` section and layout definition sections

**0.1.1**
  * changed license to GPLv3 (I've noticed that python-xlib is under GPLv2 so it seems I can't use Apache License 2.0)
  * some changes in events module

**0.1**
  * first release
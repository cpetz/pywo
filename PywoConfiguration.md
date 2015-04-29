

# `.pyworc` #

Create `.pyworc` file in your $HOME directory if you want to use custom settings in Python Window Organizer. If no `~/.pyworc` is found the defaults are used. You can specify only settings you want to change, the rest will be loaded from defaults.

`.pyworc` must contain two sections `[SETTINGS]` and `[KEYS]` described below. Any other section will be treated as a definition of layout sections.

Lines starting with `;` character are not parsed.

## `[SETTINGS]` ##

This section contains main settings:

### `numlock` ###

How `Numlock state should be treated.

> `numlock = on` - PyWO keyboard shortcuts work only when Numlock is on

> `numlock = off` - PyWO keyboard shortcuts work only when Numlock is off

> `numlock = ignore`  - ignore Numlock state **(default)**


### `capslock` ###

How Capslock state should be treated. **Work's only in the `/trunk` version!**

> `capslock = on` - PyWO keyboard shortcuts work only when Capslock is on

> `capslock = off` - PyWO keyboard shortcuts work only when Capslock is off

> `capslock = ignore`  - ignore Capslock state **(default)**


### `invert_on_resize` ###

Some windows (for example terminals) can be resized only using incremental steps. This option define if window's gravity should be inverted when window was resized by Window Manager on grid action.

![http://kosciak.blox.pl/resource/PyWO_invert_on_resize.png](http://kosciak.blox.pl/resource/PyWO_invert_on_resize.png)

> `invert_on_resize = yes` - invert window's gravity **(default)**

> `invert_on_resize = no` - keep defined gravity


### `vertical_first` ###

Behaviour of diagonal movement/resizing.

![http://kosciak.blox.pl/resource/PyWO_vertical_first.png](http://kosciak.blox.pl/resource/PyWO_vertical_first.png)

> `vertical_first = yes` - First try to move/resize vertically, then horizontally **(default)**

> `vertical_first = no` - First try to move/resize horizontally, then vertically


### `layout` ###

Select predefined layout of the grid.

> `layout = grid_2x2` - use predefined 2 by 2 grid layout

> `layout = grid_3x2` - use predefined 3 by 2 grid layout **(default)**

> `layout = grid_3x3` - use predefined 3 by 3 grid layout

> `layout = custom` - define your own layout in `.pyworc` file

> `layout = FILE_NAME` - use layout defined in `~/FILE_NAME` file


### `ignore_actions` ###

List of ignored actions. Valid actions names: `float, expand, shrink, grid, grid_width, grid_height, put, switch, cycle`

> `ignore_actions = shrink` - ignore only

> `ignore_actions = cycle, switch` - ignore cycle and switch actions

> `ignore_actions = grid` - ignore grid action

> `ignore_actions = grid_height` - ignore height cycling in grid


## `[KEYS]` ##

This section defines keyboard shortcuts definitions. Use `MOD1-MOD2-KEY` format.

Valid key modifiers: `Shift, Ctrl, Alt, Super`

PyWO uses key names used by [python-xlib](http://python-xlib.sourceforge.net/).


### `float` ###

Modifier(s) for float action.

> `float = Alt `

### `expand` ###

Modifier(s) for expand action.

> `expand = Shift`

### `shrink` ###

Modifier(s) for shrink action.

> `shrink = Alt-Shift`

### `put` ###

Modifier(s) for put action.

> `put = Alt-Cltrl`

### `grid_width` ###

Modifier(s) for grid action - cycle widths.

> `grid_width = Ctrl`

### `grid_height` ###

Modifier(s) for grid action - cycle heihts.

> `grid_height = Shift-Ctrl`

### `switch` ###

Modifier(s) and key for switch action.

> `switch = Alt-KP_Divide`

### `cycle` ###

Modifier(s) and key for cycle action.

> `cycle = Alt-Shift-KP_Divide`

### `exit` ###

Modifier(s) and key for exiting PyWO.

> `exit = Ctrl-Alt-Shift-Q`

### `reload` ###

Modifier(s) and key for reloading configuration file(s).

> `reload = Ctrl-Alt-Shift-R`

### `debug` ###

Modifier(s) and key for printing debug informations about window manager and current window.

> `debug = Ctrl-Alt-Shift-I`

### `layout sections` ###

Keys for defined layout sections. Use `SECTION_NAME = KEY` format. Keys for all defined sections must be provided. Predefined layouts consist of following sections:

```
top-left = KP_7
top = KP_8
top-right = KP_9
left = KP_4
middle = KP_5
right = KP_6
bottom-right = KP_3
bottom = KP_2
bottom-left = KP_1
```

# Layout definition #

Layout definition consists of sections describing snap points on the screen, and windows movement/resizing direction.

### `[layout-section-name]` ###

The name of the layout section. Corresponding key shortcut must be assigned in `[KEYS]` section of `.pyworc`

### `ignore_actions` ###

List of ignored actions for this section.

### `direction` ###

Direction of move, expand, shrink actions. You can use one of the predefined directions: `TOP_LEFT, TOP, TOP_RIGHT, LEFT, MIDDLE, RIGHT, BOTTOM_LEFT, BOTTOM, BOTTOM_RIGHT` or define your own direction by providing values for percentage of x and y.

![http://kosciak.blox.pl/resource/PyWO_directions.png](http://kosciak.blox.pl/resource/PyWO_directions.png)

```
direction = RIGHT
direction = 1.0, 0.5
direction = FULL, HALF
direction = 1.0, 1.0/2
direction = FULL, 1.0/2
```


### `position` ###

Position on the screen (snap point), used by put and grid actions. You can use one of the predefined positions: `TOP_LEFT, TOP, TOP_RIGHT, LEFT, MIDDLE, RIGHT, BOTTOM_LEFT, BOTTOM, BOTTOM_RIGHT` or define your own direction by providing values for percentage of x and y. See examples for `direction`.

### `gravity` ###

Gravity of a window, if not specified same value as for `position` will be used. You can use one of the predefined gravities: `TOP_LEFT, TOP, TOP_RIGHT, LEFT, MIDDLE, RIGHT, BOTTOM_LEFT, BOTTOM, BOTTOM_RIGHT` or define your own direction by providing values for percentage of x and y. See examples for `direction`.

### `widths` ###

List of window widths to be used in grid action. You can use predefined sizes: `QUARTER, THIRD, HALF, FULL` or provide your own value:

```
widths = THIRD, HALF
widths = FULL
widths = 0.25, 0.5, 0.75
widths = HALF, THIRD*2
widths = HALF, 1.0/3*2
```

### `heights` ###

List of window heights to be used in grid action. You can use predefined sizes: `QUARTER, THIRD, HALF, FULL` or provide your own value. See examples for `widths`.

## Sample section definition ##
```
[top-left]
direction = TOP_LEFT
position = TOP_LEFT
gravity = TOP_LEFT
widths = THIRD, HALF, THIRD*2
heights = THIRD, HALF, THIRD*2
```
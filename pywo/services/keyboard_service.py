#
# PyWO - Python Window Organizer
# Copyright 2010, Wojciech 'KosciaK' Pietrzok
#
# This file is part of PyWO.
#
# PyWO is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyWO is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyWO.  If not, see <http://www.gnu.org/licenses/>.
#

"""keyboard_service.py - provides keyboard shortcuts handling."""

import logging

from pywo import actions
from pywo.core import WindowManager
from pywo.core import events


__author__ = "Wojciech 'KosciaK' Pietrzok"


log = logging.getLogger(__name__)

WM = WindowManager()


class PywoModeKeyPressHandler(events.KeyHandler):

    """EventHandler for "PyWO mode" keyboard shortcuts."""

    def __init__(self, config=None):
        events.KeyHandler.__init__(self)
        self.config = config
        self.mappings = {} # {(modifiers, keycode): (action, section), }
        if self.config:
            self.set_config(self.config)

    def key_press(self, event):
        """Event handler method for KeyPressEventHandler."""
        if not (event.modifiers, event.keycode) in self.mappings:
            return
        log.debug('%s' % (event,))
        action, section = self.mappings[event.modifiers, event.keycode]
        try:
            window = WM.active_window()
            kwargs = action.get_kwargs(self.config, section)
            action(window, **kwargs)
        except actions.ActionException, exc:
            log.error(exc)
        except Exception, exc:
            log.exception(exc)
    
    def set_config(self, config):
        """Set key mappings from config."""
        self.config = config
        self.mappings.clear()
        for action in actions.manager.get_all():
            if action.need_section:
                mask = config.keys.get(action.name)
                if not mask:
                    continue
                for section in config.sections.values():
                    key = section.key
                    if key and action.name not in section.ignored_actions:
                        try:
                            (mod, keycode) = WM.str2modifiers_keycode(mask, key)
                        except ValueError:
                            log.exception('Invalid key for section %s' % section)
                        self.mappings[(mod, keycode)] = (action, section)
            else:
                key = config.keys.get(action.name)
                if key and action not in config.ignored_actions:
                    (mod, keycode) = WM.str2modifiers_keycode(key)
                    self.mappings[(mod, keycode)] = (action, None)
        self.keys = self.mappings.keys()
        self.numlock = config.numlock
        self.capslock = config.capslock


class ModalKeyHandler(events.KeyHandler):

    """Support for modality.

    Depending on config settings work as decorator for PywoModeKeyPressHandler,
    or separate KeyPressHandler responsible of handling key shortcuts for
    entering and exiting "Pywo mode"

    """

    def __init__(self, config=None):
        events.KeyHandler.__init__(self)
        self.use_modal_mode = False
        self.in_pywo_mode = False
        self.pywo_handler = PywoModeKeyPressHandler()
        keys = [WM.str2modifiers_keycode('Escape')]
        self.escape_handler = events.KeyHandler(key_press=self.normal_mode,
                                                keys=keys)
        self.visual_bell = False
        self.bell_color = 'white'
        self.bell_width = 0
        self.bell_duration = 0
        self.scroll_lock_led = False
        if config:
            self.set_config(config)

    def key_press(self, event):
        """On key press enter or leave pywo_mode."""
        if not (event.modifiers, event.keycode) in self.keys:
            return
        if self.in_pywo_mode:
            self.normal_mode(event)
        else:
            self.pywo_mode(event)

    def pywo_mode(self, event):
        """Enter PyWO mode.

        To indicate entering into PyWO mode use visual bell, 
        and turn on ScrollLock LED.
        Press ESC to go back to normal mode.
        
        """
        log.debug('%s' % (event,))
        if self.scroll_lock_led:
            WM.scroll_lock_led(True)
        if self.visual_bell:
            WM.visual_bell(self.bell_color, self.bell_width, self.bell_duration)
        self.pywo_handler.grab_keys(WM)
        self.escape_handler.grab_keys(WM)
        self.in_pywo_mode = True

    def normal_mode(self, event):
        """Leave PyWO mode, enter normal mode."""
        log.debug('%s' % (event,))
        if self.scroll_lock_led:
            WM.scroll_lock_led(False)
        if self.visual_bell:
            WM.visual_bell(self.bell_color, self.bell_width, self.bell_duration)
        self.ungrab_keys(WM)
        self.in_pywo_mode = False

    def set_config(self, config):
        """Set key mappings from config."""
        self.pywo_handler.set_config(config)
        pywo_mode_key = config.keys.get('pywo_mode')
        if not pywo_mode_key:
            self.use_modal_mode = False
            return
        self.keys = [WM.str2modifiers_keycode(pywo_mode_key)]
        self.numlock = config.numlock
        self.capslock = config.capslock
        self.use_modal_mode = config.modal_mode
        self.visual_bell = config.visual_bell
        self.bell_color = config.bell_color
        self.bell_width = config.bell_width
        self.bell_duration = config.bell_duration
        self.scroll_lock_led = config.scroll_lock_led
        if not self.use_modal_mode:
            self.in_pywo_mode = True

    def grab_keys(self, window):
        """Grab keys for self, or PywoKeyPressHandler."""
        if self.use_modal_mode:
            events.KeyHandler.grab_keys(self, window)
        else:
            self.pywo_handler.grab_keys(window)

    def ungrab_keys(self, window):
        """Ungrab keys for self, or PywoKeyPressHandler."""
        if self.in_pywo_mode and self.use_modal_mode:
            self.escape_handler.ungrab_keys(window)
        if self.in_pywo_mode:
            self.pywo_handler.ungrab_keys(window)
        else:
            events.KeyHandler.ungrab_keys(self, window)


HANDLER = ModalKeyHandler()


def setup(config):
    HANDLER.set_config(config)


def start():
    log.info('Registering keyboard shortcuts')
    HANDLER.grab_keys(WM)


def stop():
    WM.scroll_lock_led(False)
    WM.flush()
    HANDLER.ungrab_keys(WM)
    log.info('Keyboard shortcuts unregistered')



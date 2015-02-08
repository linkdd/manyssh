# -*- coding: utf-8 -*-

from gi.repository import Gtk

from manyssh.toolbar import Toolbar
from manyssh.input import Input


class Layout(Gtk.HBox):
    """
    Header layout.
    """

    def __init__(self, win, *args, **kwargs):
        """
        :param win: Main window
        :type win: manyssh.win.Window
        """

        super(Layout, self).__init__(*args, **kwargs)

        self.label = Gtk.Label()
        self.label.set_markup(' <b>$</b>')

        self.input = Input(win)
        self.toolbar = Toolbar(win)

        self.pack_start(self.label, False, True, 5)
        self.pack_start(self.input, True, True, 5)
        self.pack_end(self.toolbar, False, True, 5)

        self.input.grab_focus()

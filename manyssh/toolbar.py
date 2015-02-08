# -*- coding: utf-8 -*-

from gi.repository import Gtk
from manyssh.about import About


class Toolbar(Gtk.Toolbar):
    """
    ManySSH toolbar.
    """

    def __init__(self, win, *args, **kwargs):
        """
        :param win: ManySSH window
        :type win: manyssh.win.Window
        """

        super(Toolbar, self).__init__(*args, **kwargs)

        self.toggle = Gtk.ToolButton.new_from_stock(Gtk.STOCK_CONVERT)
        self.toggle.connect(
            'clicked',
            lambda s: map(
                lambda term: term.toggle_active(s),
                win.terms
            )
        )
        self.insert(self.toggle, -1)

        self.refresh = Gtk.ToolButton.new_from_stock(Gtk.STOCK_REFRESH)
        self.refresh.connect(
            'clicked',
            lambda s: map(
                lambda term: term.refresh(s),
                win.terms
            )
        )
        self.insert(self.refresh, -1)

        self.about = Gtk.ToolButton.new_from_stock(Gtk.STOCK_ABOUT)
        self.about.connect('clicked', lambda s, r: About(parent=win))
        self.insert(self.about, -1)

        self.exit = Gtk.ToolButton.new_from_stock(Gtk.STOCK_QUIT)
        self.exit.connect('clicked', Gtk.main_quit)
        self.insert(self.exit, -1)

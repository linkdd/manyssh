# -*- coding: utf-8 -*-

from gi.repository import Gtk
from manyssh.terminals import Notebook
from manyssh.header import Layout


class Window(Gtk.Window):
    """
    ManySSH main window.
    """

    def __init__(self, hosts, *args, **kwargs):
        """
        :param hosts: list of SSH server
        :type hosts: list of str
        """

        super(Window, self).__init__(*args, **kwargs)

        self.set_title('ManySSH')

        self.status = Gtk.Statusbar()
        self.terms = Notebook(hosts)
        self.header = Layout(self)

        self.layout = Gtk.VBox()
        self.layout.pack_start(self.header, False, True, 0)
        self.layout.pack_start(self.terms, True, True, 0)
        self.layout.pack_end(self.status, False, True, 0)

        self.add(self.layout)

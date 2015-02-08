# -*- coding: utf-8 -*-

from gi.repository import GLib, Gtk, Vte
import signal
import os


class TerminalTab(Vte.Terminal):
    def __init__(self, notebook, host, *args, **kwargs):
        super(TerminalTab, self).__init__(*args, **kwargs)

        self.notebook = notebook
        self.host = host

        self.activator = Gtk.CheckButton()
        self.activator.set_active(True)
        self.activator.connect(
            'toggled',
            lambda s: self.emit('window-title-changed')
        )

        self.label = Gtk.Label()
        self.label.set_markup(self.get_term_title())

        self.connect('window-title-changed', self.on_title_changed)
        self.connect('child-exited', self.refresh)

    def get_tab(self):
        layout = Gtk.HBox(spacing=5)

        layout.pack_start(self.activator, False, True, 0)
        layout.pack_start(self.label, True, True, 0)

        refresh = Gtk.ToolButton.new_from_stock(Gtk.STOCK_REFRESH)
        refresh.connect('clicked', self.refresh)
        layout.pack_end(refresh, False, True, 0)

        layout.show_all()
        return layout

    def refresh(self, sender):
        try:
            os.kill(self.pid, signal.SIGINT)

        except OSError:
            pass

        self.reset(True, True)
        self()

    def get_term_title(self, nomarkup=False):
        title = self.get_window_title() or self.host

        if nomarkup:
            return title

        elif self.activator.get_active():
            return '<b>{0}</b>'.format(title)

        else:
            return '<i>{0}</i>'.format(title)

    def on_title_changed(self, sender):
        self.label.set_markup(self.get_term_title())

    def toggle_active(self, sender):
        self.activator.set_active(not self.activator.get_active())
        self.emit('window-title-changed')

    def __call__(self):
        _, self.pid = self.fork_command_full(
            Vte.PtyFlags.DEFAULT,
            os.environ['HOME'],
            [
                os.environ['SHELL'] or '/bin/sh',
                '-c',
                'ssh {0}'.format(self.host)
            ],
            [],
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None
        )


class Notebook(Gtk.Notebook):
    def __init__(self, hosts, *args, **kwargs):
        super(Notebook, self).__init__(*args, **kwargs)

        self.set_scrollable(True)

        for host in hosts:
            # Create VTE Terminal with SSH connection
            term = TerminalTab(self, host)
            term()

            self.append_page_menu(term, term.get_tab(), term.label)

    @property
    def current(self):
        return self.get_nth_page(self.get_current_page())

# -*- coding: utf-8 -*-

from gi.repository import Gdk, Gtk


class Input(Gtk.Entry):
    """
    ManySSH command line.
    """

    def __init__(self, win, *args, **kwargs):
        """
        :param win: ManySSH window
        :type win: manyssh.win.Window
        """

        super(Input, self).__init__(*args, **kwargs)

        self.win = win
        self.ctx = win.status.get_context_id('ManySSH command line')

        self.status = lambda *args, **kwargs: self.win.status.push(
            self.ctx,
            *args,
            **kwargs
        )

        self.status('-- INSERT --')
        self.insertmode = True

        for ev in ['key-press-event', 'key-release-event']:
            self.connect(ev, self.sendevent, ev)

        self.connect('activate', self.parse_command)

    def sendevent(self, sender, event, eventname):
        """
        If in INSERT mode, redirect events to terminals.

        :param sender: Event emitter
        :type sender: Gtk.Widget

        :param event: Keyboard event
        :type event: Gdk.EventKey

        :param eventname: Event's name
        :type eventname: str

        :returns: True if event was handled, False otherwise
        """

        modifier = Gdk.ModifierType.CONTROL_MASK

        if self.insertmode:
            if event.keyval == Gdk.KEY_Escape and event.state & modifier:
                self.status('-- COMMAND --')
                self.insertmode = False
                return True

            else:
                for term in self.win.terms:
                    if term.activator.get_active():
                        term.grab_focus()
                        term.emit(eventname, event.copy())

                self.grab_focus()
                return True

        elif event.keyval == Gdk.KEY_Insert and event.state & modifier:
            self.status('-- INSERT --')
            self.set_text('')
            self.insertmode = True
            return True

        return False

    def parse_command(self, sender):
        """
        Parse command line.

        :param sender: Event emitter
        :type sender: Gtk.Widget
        """

        command = self.get_text()
        method = 'cmd_{0}'.format(command)

        if not hasattr(self, method):
            self.status.push(
                self.ctx,
                '-- COMMAND -- Error: Unknown command: {0}'.format(command)
            )

        else:
            handler = getattr(self, method)
            handler()
            self.status('-- COMMAND --')

        self.set_text('')

    def cmd_p(self):
        """ Previous page command. """
        self.win.terms.prev_page()

    def cmd_n(self):
        """ Next page command. """
        self.win.terms.next_page()

    def cmd_r(self):
        """ Refresh page command. """
        self.terms.current.refresh(self)

    def cmd_ra(self):
        """ Refresh all pages command. """
        for term in self.win.terms:
            term.refresh(self)

    def cmd_t(self):
        """ Toggle page command. """
        self.win.terms.current.toggle_active(self)

    def cmd_ta(self):
        """ Toggle all pages command. """
        for term in self.win.terms:
            term.toggle_active(self)

    def cmd_q(self):
        """ Exit command. """
        Gtk.main_quit()

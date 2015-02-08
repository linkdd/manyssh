# -*- coding: utf-8 -*-

from gi.repository import Gtk
from manyssh import meta


class About(Gtk.AboutDialog):
    """
    ManySSH about dialog.
    """

    def __init__(self, *args, **kwargs):
        kwargs['title'] = '{0} {1}'.format(meta.PROGRAM_NAME, meta.VERSION)

        super(About, self).__init__(*args, **kwargs)

        self.set_program_name(meta.PROGRAM_NAME)
        self.set_version(meta.VERSION)
        self.set_authors(meta.AUTHORS)
        self.set_license(meta.LICENSE)

        self.connect('response', lambda s, r: self.destroy())
        self.show_all()

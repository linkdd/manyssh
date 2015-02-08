# -*- coding: utf-8 -*-

from gi.repository import GLib, Gtk
from manyssh.win import Window

import json
import os


class Application(object):
    """
    ManySSH application.
    """

    def __init__(self, argv, *args, **kwargs):
        """
        :param argv: argument list
        :type argv: list of str
        """

        super(Application, self).__init__(*args, **kwargs)

        self.argv = argv

    def load_config(self):
        """ Load configuration. """

        paths = []
        dirs = GLib.get_system_config_dirs()
        dirs.append(GLib.get_user_config_dir())

        paths = [
            p
            for p in [
                os.path.join(d, 'manyssh', 'clusters.conf')
                for d in dirs
            ] + ['clusters.conf']
            if os.path.exists(p)
        ]

        self.config = {}

        for path in paths:
            print('-- Loading configuration: {0}'.format(path))
            with open(path) as f:
                self.config.update(json.load(f))

    def parse_commandline(self):
        """ Parse argument list. """

        if len(self.argv) < 2:
            raise RuntimeError('No cluster specified')

        cluster = self.argv[1]

        if cluster not in self.config:
            raise RuntimeError('Cluster {0} not found'.format(cluster))

        self.hosts = self.config[cluster]

    def init_ui(self):
        """ Initialize user interface. """

        win = Window(self.hosts)
        win.connect('delete-event', Gtk.main_quit)
        win.show_all()

        Gtk.main()

    def __call__(self):
        """ Entry point. """

        try:
            self.load_config()
            self.parse_commandline()
            self.init_ui()

        except RuntimeError as err:
            print('Error: {0}'.format(err))
            return 1

        return 0

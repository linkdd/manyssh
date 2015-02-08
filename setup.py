#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.install import install


class ManySSHInstall(install):
    """ Check for python-gi. """

    def run(self):
        try:
            from gi.repository import GLib, Gdk, Gtk, Vte

        except ImportError as err:
            import sys

            print('python-gi module not found: {0}'.format(err))
            sys.exit(1)

        install.run(self)


setup(
    name='manyssh',
    version='1.0',
    license='MIT',

    author='David Delassus',
    author_email='david.jose.delassus@gmail.com',
    description='One command line to control multiple SSH connections',
    url='https://github.com/linkdd/manyssh',
    download_url='https://github.com/linkdd/manyssh/tarball/1.0',
    keywords=['manyssh', 'gtk', 'ssh'],
    classifiers=[],

    scripts=['scripts/manyssh'],
    packages=find_packages(),

    cmdclass={
        'install': ManySSHInstall
    }
)

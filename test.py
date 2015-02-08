#!/usr/bin/env python
# -*- coding: utf-8 -*-

from manyssh.app import Application
import unittest


class ManySSHTest(unittest.TestCase):
    def setUp(self):
        self.argv = ['manyssh', 'mycluster0']
        self.expected_hosts = [
            'root@myhost0',
            'root@myhost1',
            'root@myhost2'
        ]

        self.app = Application(self.argv)
        self.app.load_config()
        self.app.parse_commandline()

    def test_manyssh(self):
        self.assertEqual(
            self.app.config.get('mycluster0', []),
            self.expected_hosts
        )

        self.assertEqual(self.app.hosts, self.expected_hosts)


if __name__ == '__main__':
    unittest.main()

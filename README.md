# ManySSH

<a href="https://travis-ci.org/linkdd/manyssh">
    <img src="https://travis-ci.org/linkdd/manyssh.svg"/>
</a>

One command line to control multiple SSH connections.

## Installation

    # apt-get install gir1.2-gtk-3.0 gir1.2-vte-2.90 python-gi python-gobject python-gobject-2 python-gobject-dev
    $ git clone https://github.com/linkdd/manyssh.git
    $ cd manyssh
    $ python setup.py install

## Usage

*ManySSH* reads the following configuration files, if found:

 * /etc/xdg/manyssh/clusters.conf
 * ~/.config/manyssh/clusters.conf
 * ./clusters.conf

The ``clusters.conf`` file contains clusters definition as JSON:

    {
        "mycluster0": [
            "root@myhost0",
            "root@myhost1",
            "root@myhost2"
        ],
        "mycluster1": [
            "user@myhost0",
            "user@myhost1",
            "user@myhost2"
        ]
    }

You're now able to open your cluster with:

    $ manyssh mycluster0

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
        ],
        "mytunnel0": [
            "root@myhost0 -L8001:localhost:8000",
            "root@myhost1 -L8002:localhost:8000",
            "root@myhost2 -L8003:localhost:8000"
        ]
    }

You're now able to open your cluster with:

    $ manyssh mycluster0

## User Interface

![Main Window](https://raw.githubusercontent.com/linkdd/manyssh/master/doc/ui.png)

Here, your in **INSERT** mode, everything you type will be sent through all activated connections.

Using ``<Control>+Escape``, you will switch to the **COMMAND** mode, allowing you to type commands (instead of clicking).
Use ``<Control>+Insert`` to switch back to the **INSERT** mode.

A connection can be activated or disabled via:

 * the checkbox in its tab ;
 * the command ``t``.

You can also toggle the state of all connections with:

 * the *convert* button (first one of the toolbar) ;
 * the command ``ta``.

A connection can be refreshed, it will eventually kill the current process and start a new one.

You an do this via:

 * the refresh button in its tab ;
 * the command ``r`` ;
 * the refresh button in the toolbar, to refresh all ;
 * the command ``ra``, to refresh all.

You have two more commands, to navigate into tabs:

 * ``p`` : go to previous page ;
 * ``n`` : go to last page.

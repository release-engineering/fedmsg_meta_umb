fedmsg_meta_umb
=================================

.. split here

fedmsg metadata providers for the Unified Message Bus
----------------------------------------------------------------

`fedmsg <http://fedmsg.com>`_ is a set of tools for knitting together services
and webapps into a realtime messaging net.  This package contains metadata
provider plugins for internal Red Hat services attached to the Unified
Message Bus.

If you were to deploy fedmsg at another site, you would like want to write your
own module like this one that could provide textual representations of *your*
messages.

Pop into ``#fedora-apps`` on freenode if you have questions or comments.

Build Status
------------

.. |master| image:: https://secure.travis-ci.org/release-engineering/fedmsg_meta_umb.png?branch=master
   :alt: Build Status - master branch
   :target: http://travis-ci.org/#!/release-engineering/fedmsg_meta_umb

+----------+-----------+
| Branch   | Status    |
+==========+===========+
| master   | |master|  |
+----------+-----------+

Running the Tests
-----------------

::

    # install the test tool
    $ sudo dnf install detox
    # Run it.
    $ detox

If `detox` is unavailable on your system, you can also use plain old `tox`.

Building the Docs
-----------------

::

    # Install additional dependencies
    $ pip install -r doc/requirements.txt
    $ sphinx-build doc/ htmldocs/

Getting started with fedmsg_meta_umb
====================================

This project provides a mapping that converts a specific
`Unified Message Bus <https://mojo.redhat.com/docs/DOC-1046330>`_
message into a single string of information describing the action
that lead to this message.


Quick introduction to fedmsg_meta
---------------------------------

Sometimes an example is worth more than just words:

::

    import requests

    import fedmsg
    import fedmsg.meta
    config = fedmsg.config.load_config()
    fedmsg.meta.make_processors(**config)

    req = requests.get('https://apps.fedoraproject.org/datagrepper/raw/')
    data = req.json()

    for message in data['raw_messages']:
        print fedmsg.meta.msg2subtitle(message)
        print fedmsg.meta.msg2usernames(message)
        print fedmsg.meta.msg2packages(message)


This simple script will retrieve recent messages from datagrepper and for
each message returned will print a one-line description of the action as
well as the persons and packages involved.

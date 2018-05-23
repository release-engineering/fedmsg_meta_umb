# Copyright (C) 2017 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Ralph Bean <rbean@redhat.com>

import fedmsg.tests.test_meta
from .common import add_doc


class TestPungiStart(fedmsg.tests.test_meta.Base):
    """ Pungi (also called distill) is the compose tool on which RCM is trying
    to standardize... and it's on the message bus!

    Here's an example message published when a compose starts.
    """
    expected_title = "pungi.status-change"
    expected_subti = "pungi compose of OracleJava-7.4-RHEL-7-20170602.n.0 started"
    expected_link = ("http://download.lab.bos.redhat.com/nightly/"
                     "OracleJava-7.4-RHEL-7-20170602.n.0")
    expected_icon = "https://apps.fedoraproject.org/img/icons/pungi.png"
    msg = {
        "msg": {
            "status": "STARTED",
            "location": "/mnt/redhat/nightly/OracleJava-7.4-RHEL-7-20170602.n.0/compose",
            "compose_id": "OracleJava-7.4-RHEL-7-20170602.n.0"
        },
        "timestamp": 1449600728.0,
        "topic": "/topic/VirtualTopic.eng.pungi.status-change"
    }


class TestPungiComplete(fedmsg.tests.test_meta.Base):
    """ Pungi (also called distill) is the compose tool on which RCM is trying
    to standardize... and it's on the message bus!

    Here's an example message published when a compose completes.
    """
    expected_title = "pungi.status-change"
    expected_subti = "pungi compose of OracleJava-7.4-RHEL-7-20170602.n.0 just finished"
    expected_link = ("http://download.lab.bos.redhat.com/nightly/"
                     "OracleJava-7.4-RHEL-7-20170602.n.0")
    expected_icon = "https://apps.fedoraproject.org/img/icons/pungi.png"
    msg = {
        "msg": {
            "status": "FINISHED",
            "location": "/mnt/redhat/nightly/OracleJava-7.4-RHEL-7-20170602.n.0/compose",
            "compose_id": "OracleJava-7.4-RHEL-7-20170602.n.0"
        },
        "timestamp": 1449600728.0,
        "topic": "/topic/VirtualTopic.eng.pungi.status-change"
    }


class TestPungiTerminated(fedmsg.tests.test_meta.Base):
    """ Pungi (previously known as distill) is the compose tool on which RCM is
    trying to standardize... and it's on the message bus!

    Here's an example message published when a compose is killed.
    """
    expected_title = "pungi.status-change"
    expected_subti = "pungi compose of OracleJava-7.4-RHEL-7-20170602.n.0 was terminated"
    expected_link = ("http://download.lab.bos.redhat.com/nightly/"
                     "OracleJava-7.4-RHEL-7-20170602.n.0")
    expected_icon = "https://apps.fedoraproject.org/img/icons/pungi.png"
    msg = {
        "msg": {
            "status": "TERMINATED",
            "location": "/mnt/redhat/nightly/OracleJava-7.4-RHEL-7-20170602.n.0/compose",
            "compose_id": "OracleJava-7.4-RHEL-7-20170602.n.0"
        },
        "timestamp": 1449600728.0,
        "topic": "/topic/VirtualTopic.eng.pungi.status-change"
    }


class TestPungiPhaseStart(fedmsg.tests.test_meta.Base):
    """ Pungi (also called distill) is the compose tool on which RCM is trying
    to standardize... and it's on the message bus!

    Here's an example message published when the ``createrepo`` phase of a
    compose starts.
    """
    expected_title = "pungi.phase-start"
    expected_subti = "pungi started the createrepo phase of the " + \
        "RHEL-7.4-20170602.n.3 compose"
    expected_link = "http://download.lab.bos.redhat.com/nightly/RHEL-7.4-20170602.n.3"
    expected_icon = "https://apps.fedoraproject.org/img/icons/pungi.png"
    msg = {
        "i": 1,
        "timestamp": 1449605930.0,
        "topic": "/topic/VirtualTopic.eng.pungi.phase-start",
        "msg": {
            "phase_name": "createrepo",
            "location": "http://download.lab.bos.redhat.com/nightly/RHEL-7.4-20170602.n.3/compose",
            "compose_id": "RHEL-7.4-20170602.n.3"
        }
    }


class TestPungiCreateISOTargets(fedmsg.tests.test_meta.Base):
    """ Pungi (also called distill) is the compose tool on which RCM is trying
    to standardize... and it's on the message bus!

    Here's an example message published when createiso targets are assigned.
    """
    expected_title = "pungi.createiso-targets"
    expected_subti = "pungi assigned 13 createiso targets for RHEL-7.4-20170602.n.3"
    expected_link = "http://download.lab.bos.redhat.com/nightly/RHEL-7.4-20170602.n.3"
    expected_icon = "https://apps.fedoraproject.org/img/icons/pungi.png"
    msg = {
        "i": 1,
        "timestamp": 1449605930.0,
        "msg_id": "2015-05ea75ce-f648-41b5-9e29-da56202a2ba5",
        "topic": "/topic/VirtualTopic.eng.pungi.createiso-targets",
        "msg": {
            "deliverables": [
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Client/x86_64/iso/RHEL-7.4-20170602.n.3-Client-x86_64-dvd1.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Client/source/iso/RHEL-7.4-20170602.n.3-Client-source-dvd1.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Client/source/iso/RHEL-7.4-20170602.n.3-Client-source-dvd2.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Server/aarch64/iso/RHEL-7.4-20170602.n.3-Server-aarch64-dvd1.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Server/ppc64/iso/RHEL-7.4-20170602.n.3-Server-ppc64-dvd1.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Server/ppc64le/iso/RHEL-7.4-20170602.n.3-Server-ppc64le-dvd1.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Server/s390x/iso/RHEL-7.4-20170602.n.3-Server-s390x-dvd1.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Server/x86_64/iso/RHEL-7.4-20170602.n.3-Server-x86_64-dvd1.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Server/source/iso/RHEL-7.4-20170602.n.3-Server-source-dvd1.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Server/source/iso/RHEL-7.4-20170602.n.3-Server-source-dvd2.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Workstation/x86_64/iso/RHEL-7.4-20170602.n.3-Workstation-x86_64-dvd1.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Workstation/source/iso/RHEL-7.4-20170602.n.3-Workstation-source-dvd1.iso",
                "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/"
                "Workstation/source/iso/RHEL-7.4-20170602.n.3-Workstation-source-dvd2.iso",
            ],
            "compose_id": "RHEL-7.4-20170602.n.3",
            "location": "http://download.lab.bos.redhat.com/nightly/RHEL-7.4-20170602.n.3/compose"

        }
    }


class TestPungiCreateISOWin(fedmsg.tests.test_meta.Base):
    """ Pungi (also called distill) is the compose tool on which RCM is trying
    to standardize... and it's on the message bus!

    Here's an example message published when a createiso target completes.
    """
    expected_title = "pungi.createiso-imagedone"
    expected_subti = "pungi finished createiso for " + \
        "Server/s390x/iso/RHEL-7.4-20170602.n.3-Server-s390x-dvd1.iso"
    expected_link = "http://download.lab.bos.redhat.com/nightly/RHEL-7.4-20170602.n.3"
    expected_icon = "https://apps.fedoraproject.org/img/icons/pungi.png"
    msg = {
        "i": 1,
        "timestamp": 1449605930.0,
        "topic": "/topic/VirtualTopic.eng.pungi.createiso-imagedone",
        "msg": {
            "variant": "Server",
            "arch": "s390x",
            "file": "/mnt/redhat/nightly/RHEL-7.4-20170602.n.3/compose/Server/"
            "s390x/iso/RHEL-7.4-20170602.n.3-Server-s390x-dvd1.iso",
            "compose_id": "RHEL-7.4-20170602.n.3",
            "location": "http://download.lab.bos.redhat.com/nightly/RHEL-7.4-20170602.n.3/compose"
        }
    }


class TestPungiOstree(fedmsg.tests.test_meta.Base):
    """ Pungi (also called distill) is the compose tool on which RCM is trying
    to standardize... and it's on the message bus!

    It *can* produce ostrees... but it doesn't seem to be used in production yet.

    Here's an example message published from Fedora when an ostree phase
    completed succesfully.
    """
    cid = 'f99114401ffce2753bd7cd5401bff056a029bb80474859ab769f68586978248d'
    expected_title = "pungi.ostree"
    expected_subti = "pungi ostree compose Fedora-25-20161002.n.0 " + \
        "produced ostree commit %s for x86_64 " % cid + \
        "fedora-atomic/25/x86_64/docker-host"
    expected_link = "http://kojipkgs.fedoraproject.org/" + \
        "compose//branched/Fedora-25-20161002.n.0"
    expected_icon = "https://apps.fedoraproject.org/img/icons/pungi.png"
    msg = {
        "i": 1,
        "timestamp": 1475402944.0,
        "topic": "/topic/VirtualTopic.eng.pungi.ostree",
        "msg": {
            "arch": "x86_64",
            "variant": "Atomic",
            "commitid": "f99114401ffce2753bd7cd5401bff056a029bb80474859ab769f68586978248d",
            "location": "http://kojipkgs.fedoraproject.org/compose//branched/Fedora-25-20161002.n.0/compose",
            "ref": "fedora-atomic/25/x86_64/docker-host",
            "compose_id": "Fedora-25-20161002.n.0"
        }
    }


add_doc(locals())

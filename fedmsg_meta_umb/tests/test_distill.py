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


class TestDistillStart(fedmsg.tests.test_meta.Base):
    """ Pungi (also called distill) is the compose tool on which RCM is trying
    to standardize... and it's on the message bus!

    Sometimes, older versions of distill need to be used for older products (to
    ensure the metadata is compatible).

    Here's an example message published when a compose starts.
    """
    expected_title = "distill.compose-started"
    expected_subti = "distill compose of Supp-6.10-RHEL-6-20170703.n.0 started"
    expected_link = ("http://download.lab.bos.redhat.com/nightly/"
                     "Supp-6.10-RHEL-6-20170703.n.0")
    msg = {
        "topic": "/topic/VirtualTopic.eng.distill.compose-started",
        "msg": {
            "compose-path": "/mnt/redhat/nightly/Supp-6.10-RHEL-6-20170703.n.0",
            "compose-label": "",
            "compose-type": "nightly",
            "compose-id": "Supp-6.10-RHEL-6-20170703.n.0",
            "compose-state": "STARTED",
            "release-id": "Supp-6.10-RHEL-6"
        }
    }


class TestDistillComplete(fedmsg.tests.test_meta.Base):
    """ Pungi (also called distill) is the compose tool on which RCM is trying
    to standardize... and it's on the message bus!

    Sometimes, older versions of distill need to be used for older products (to
    ensure the metadata is compatible).

    Here's an example message published when a compose completes.
    """
    expected_title = "distill.compose-finished"
    expected_subti = "distill compose of Supp-6.10-RHEL-6-20170703.n.0 just finished"
    expected_link = ("http://download.lab.bos.redhat.com/nightly/"
                     "Supp-6.10-RHEL-6-20170703.n.0")
    msg = {
        "topic": "/topic/VirtualTopic.eng.distill.compose-finished",
        "msg": {
            "compose-path": "/mnt/redhat/nightly/Supp-6.10-RHEL-6-20170703.n.0",
            "compose-label": "",
            "compose-type": "nightly",
            "compose-id": "Supp-6.10-RHEL-6-20170703.n.0",
            "compose-state": "FINISHED",
            "release-id": "Supp-6.10-RHEL-6"
        }
    }

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


class TestRobosignatoryContainerSign(fedmsg.tests.test_meta.Base):
    """ Robosignatory is an auto-signing service driven by the UMB.  Our plugin
    for it is called RADAS (RAD auto-signing service).

    It publishes messages when it signs containers!  Here's an example:
    """
    expected_title = "robosignatory.container.sign"
    expected_subti = (
        "robosignatory's attempt to sign the redhat-e2e-container-e2e-"
        "container-test-product container with F21541EB was met with "
        "success")
    msg = {
        "headers": {
            "content-type": "text/plain",
            "destination": "/topic/VirtualTopic.eng.robosignatory.container.sign",
            "expires": "1503893646415",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-36838-1502307902532-3:2760:-1:1:3",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "timestamp": "1503288846415"
        },
        "i": 5403,
        "msg": {
            "errors": [],
            "manifest_digest": "sha256:9eba6f4b34e7d4b7223a97268eac35de335d9530c39f0bc4e3b3d41106d511f6",
            "pub_task_id": 135422,
            "repo": "redhat-e2e-container-e2e-container-test-product",
            "request_id": "f9e63af7-256d-4bd1-b83d-32fa1ad6abbe",
            "request_received_time": "2017-08-21T04:14:04.692167",
            "sig_key_id": "F21541EB",
            "signed_claim": "owGbwMvMwME4uavh1CdRx9eMaxkLksTiiwpyizPT...",
            "signing_server_requested": "2017-08-21T04:14:05.748709",
            "signing_server_responded": "2017-08-21T04:14:06.322313",
            "signing_status": "success"
        },
        "msg_id": "2017-7868079f-621b-4e14-b139-ebfa95be2c9d",
        "timestamp": 1503288846.0,
        "topic": "/topic/VirtualTopic.eng.robosignatory.container.sign",
        "username": "fedmsg"
    }


add_doc(locals())

# Copyright (C) 2018 Red Hat, Inc.
#
# fedmsg_meta_umb is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg_meta_umb is distributed in the hope that it will be useful,
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


class TestNewcastleStateChange(fedmsg.tests.test_meta.Base):
    """ Project Newcastle is a buildsystem for the middleware org.

    Newcastle will publish messages to the message bus when builds
    change state.  This is an example of just such a message.
    """
    expected_title = 'pnc.builds'
    expected_subti = ("The state of pnc nickboldt-experiments build #7156 "
                      "changed from accepted to building")
    expected_link = "http://orch.cloud.pnc.engineering.redhat.com/pnc-web/#/build-records/7156"
    expected_packages = set([])
    expected_usernames = set([])
    expected_icon = (
        'https://datagrepper.engineering.redhat.com/'
        'umb/_static/img/icons/newcastle.png')
    msg = {
        "timestamp": 1534958190.0,
        "msg_id": "ID:orch-70-8z1lp-37781-1533892609865-3:1:250:1:1",
        "topic": "/topic/VirtualTopic.eng.pnc.builds",
        "headers": {
            "expires": "1535562990800",
            "name": "nickboldt-experiments",
            "producer": "PNC",
            "attribute": "state",
            "configurationId": "400",
            "destination": "/topic/VirtualTopic.eng.pnc.builds",
            "configurationRevision": "2348",
            "persistent": "true",
            "priority": "4",
            "oldStatus": "accepted",
            "timestamp": "1534958190800",
            "newStatus": "building",
            "message-id": "ID:orch-70-8z1lp-37781-1533892609865-3:1:250:1:1",
            "type": "BuildStateChange",
        },
        "msg": {
            "attribute": "state",
            "oldStatus": "accepted",
            "buildRecordId": "7156",
            "newStatus": "building"
        }
    }


add_doc(locals())

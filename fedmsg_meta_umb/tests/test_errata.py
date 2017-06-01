# Copyright (C) 2017 Red Hat, Inc.
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


class TestErrataStatusChange(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    Messages are published when an advisory **changes state**.  This is an
    example of an advisory moving from the QE state back to the NEW_FILES state
    (for modification by developers).
    """
    expected_title = 'errata.activity.status'
    expected_subti = ('fmuellne moved RHBA-2017:27087-02 from QE to NEW_FILES')
    expected_link = 'https://errata.devel.redhat.com/advisory/27087'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set(['fmuellne'])
    expected_agent = 'fmuellne'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')

    msg = {
        "username": None,
        "i": 0,
        "timestamp": 1496252132.0,
        "msg_id": "ID\\cmessaging-devops-broker01.web.prod.ext.phx2.redhat."
        "com-32888-1493960489068-4\\c472412\\c0\\c0\\c1",
        "topic": "/topic/VirtualTopic.eng.errata.activity.status",
        "headers": {
            "errata_status": "NEW_FILES",
            "expires": "0",
            "errata_id": "27087",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "to": "NEW_FILES",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.activity.status",
            "when": "2017-05-31 17:35:24 UTC",
            "persistent": "true",
            "who": "fmuellne@redhat.com",
            "priority": "4",
            "synopsis": "mutter/shell/extensions bug fix and enhancement update",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": "ID\\cmessaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-32888-1493960489068-4\\c472412\\c0\\c0\\c1",
            "fulladvisory": "RHBA-2017:27087-02",
            "timestamp": "0",
            "from": "QE",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "errata.activity.status",
            "subject": "errata.activity.status"
        },
        "msg": ""
    }

class TestErrataActivityCreated(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    Messages like this one are published when an advisory is **created**.
    """
    expected_title = 'errata.activity.created'
    expected_subti = ('bkearney filed a new RHBA advisory for '
                      'Sat-Tools-6.2-ASYNC')
    expected_link = 'https://errata.devel.redhat.com/advisory/28816'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set(['bkearney'])
    expected_agent = 'bkearney'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "username": None,
        "i": 0,
        "timestamp": 1496273395.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-32888-1493960489068-4:480845:0:0:1",
        "topic": "/topic/VirtualTopic.eng.errata.activity.created",
        "headers": {
            "expires": "0",
            "errata_id": "28816",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.activity.created",
            "when": "2017-05-31 23:29:54 UTC",
            "persistent": "true",
            "who": "bkearney@redhat.com",
            "priority": "4",
            "synopsis": "Satellite Tools 6.2.10 Async Bug Release",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-32888-1493960489068-4:480845:0:0:1",
            "timestamp": "0",
            "release": "Sat-Tools-6.2-ASYNC",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "RHBA",
            "subject": "errata.activity.created"
        },
        "source_version": "0.7.0",
        "msg": ""
    }

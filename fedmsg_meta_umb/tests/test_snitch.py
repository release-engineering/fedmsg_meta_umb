# Copyright (C) 2020 Red Hat, Inc.
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
# Authors:  Ales Raszka <araszka@redhat.com>

import fedmsg.tests.test_meta
from .common import add_doc


class TestSnitch(fedmsg.tests.test_meta.Base):
    """
    Simple parser of Snitch messages
    """

    expected_title = "snitch"
    expected_subti = "New DB event (replace): containerImage - 5e17f347dd19c77896f4f7c0"
    expected_icon = "_static/img/icons/snitch.png"

    msg = {
        "i": 0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-46538-1578341806859-3:541553:0:0:1",
        "topic": "/topic/VirtualTopic.eng.snitch",
        "timestamp": 1578902763.0,
        "certificate": None,
        "signature": None,
        "username": None,
        "crypto": None,
        "msg": {
            "entityData": {
                "@mongoHidden": {"docver": [{"$oid": "5e1c24e8dd19c77896f587d4"}]},
                "_id": {"$oid": "5e17f347dd19c77896f4f7c0"},
                "architecture": "arm64",
                "certifications#": 0,
                "certified": False,
                "content_sets": [],
                "content_sets#": 0,
                "cpe_ids#": 0,
                "cpe_ids_rh_base_images#": 0,
                "createdBy": "metaxor",
                "creationDate": {"$date": 1578627911612},
            },
            "entityName": "containerImage",
        },
        "headers": {
            "JMSXUserID": "msg-snitch",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "amq6100_destination": "queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "amq6100_originalDestination": "topic://VirtualTopic.eng.snitch",
            "correlation-id": "6b37e9b3-2c2d-4b3b-a2c1-26521f75b494",
            "database": "data",
            "destination": "/topic/VirtualTopic.eng.snitch",
            "entityName": "containerImage",
            "expires": "0",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-465383:541553:0:0:1",
            "operationType": "replace",
            "original-destination": "/topic/VirtualTopic.eng.snitch",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "timestamp": "0",
        },
        "source_name": "datanommer",
        "source_version": "0.9.1",
    }


add_doc(locals())

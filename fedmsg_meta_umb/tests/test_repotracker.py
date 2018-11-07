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
# Authors:  Mike Bonnet <mikeb@redhat.com>

import fedmsg.tests.test_meta
from .common import add_doc


class TestRepotrackerAdded(fedmsg.tests.test_meta.Base):
    """ repotracker tracks container repositories, and publishes a message when they change.

    An "added" message is published whenever a new tag is added to a repo.
    """
    expected_title = 'repotracker.container.tag.added'
    expected_subti = 'testtag tag was added to the repotracker container repository'
    expected_link = 'https://quay.io/factory2/repotracker'
    expected_icon = '/umb/_static/img/icons/repotracker.png'

    msg = {
        "i": 0,
        "timestamp": 1541166247.0,
        "msg_id": "ID:messaging-devops-broker01.dev1.ext.devlab.redhat.com-39068-1541025216899-3:4075:0:0:1",
        "topic": "/topic/VirtualTopic.eng.repotracker.container.tag.added",
        "headers": {
            "correlation-id": "8cbc21b0-785f-4bff-a456-53cd9d51dbd8",
            "JMS_AMQP_PROPERTIES": "true",
            "tag": "testtag",
            "reponame": "repotracker",
            "digest": "sha256:05329d12087818843f353c7d566b4442ceb67d871a049b3b1b88923b72635772",
            "JMS_AMQP_ORIGINAL_ENCODING": "5",
            "JMS_AMQP_HEADER": "true",
            "original-destination": "/topic/VirtualTopic.eng.repotracker.container.tag.added",
            "destination": "/topic/VirtualTopic.eng.repotracker.container.tag.added",
            "amq6100-destination": "queue://Consumer.client-datanommer.upshift-dev.VirtualTopic.eng.>",
            "old_digest": "null",
            "timestamp": "0",
            "expires": "0",
            "repo": "quay.io/factory2/repotracker",
            "arch": "amd64",
            "subscription": "/queue/Consumer.client-datanommer.upshift-dev.VirtualTopic.eng.>",
            "amq6100-originalDestination": "topic://VirtualTopic.eng.repotracker.container.tag.added",
            "created": "2018-11-02T00:38:43.931368396Z",
            "action": "added",
            "message-id": "ID:messaging-devops-broker01.dev1.ext.devlab.redhat.com-39068-1541025216899-3:4075:0:0:1",
            "os": "linux",
            "priority": "4"
        },
        "msg": {
            "old_digest": None,
            "created": "2018-11-02T00:38:43.931368396Z",
            "os": "linux",
            "labels": {
                "vendor": "Factory 2.0",
                "name": "repotracker",
                "license": "GPLv3"
            },
            "repo": "quay.io/factory2/repotracker",
            "tag": "testtag",
            "reponame": "repotracker",
            "action": "added",
            "arch": "amd64",
            "digest": "sha256:05329d12087818843f353c7d566b4442ceb67d871a049b3b1b88923b72635772"
        }
    }


class TestRepotrackerUpdated(fedmsg.tests.test_meta.Base):
    """ repotracker tracks container repositories, and publishes a message when they change.

    An "updated" message is published whenever the image referenced by a tag changes.
    """
    expected_title = 'repotracker.container.tag.updated'
    expected_subti = 'testtag tag was updated in the repotracker container repository'
    expected_link = 'https://quay.io/factory2/repotracker'
    expected_icon = '/umb/_static/img/icons/repotracker.png'

    msg = {
        "i": 0,
        "timestamp": 1541167705.0,
        "msg_id": "ID:messaging-devops-broker01.dev1.ext.devlab.redhat.com-39068-1541025216899-3:4150:0:0:1",
        "topic": "/topic/VirtualTopic.eng.repotracker.container.tag.updated",
        "headers": {
            "correlation-id": "399f1e13-51fb-435f-ada9-5513d6739cf4",
            "JMS_AMQP_PROPERTIES": "true",
            "tag": "testtag",
            "reponame": "repotracker",
            "digest": "sha256:edf137791b86ac018ea1c29ddfddf7501fc4b383dc1a805d47aa83c2ff6ef9bc",
            "JMS_AMQP_ORIGINAL_ENCODING": "5",
            "JMS_AMQP_HEADER": "true",
            "original-destination": "/topic/VirtualTopic.eng.repotracker.container.tag.updated",
            "destination": "/topic/VirtualTopic.eng.repotracker.container.tag.updated",
            "amq6100-destination": "queue://Consumer.client-datanommer.upshift-dev.VirtualTopic.eng.>",
            "old_digest": "sha256:05329d12087818843f353c7d566b4442ceb67d871a049b3b1b88923b72635772",
            "timestamp": "0",
            "expires": "0",
            "repo": "quay.io/factory2/repotracker",
            "arch": "amd64",
            "subscription": "/queue/Consumer.client-datanommer.upshift-dev.VirtualTopic.eng.>",
            "amq6100-originalDestination": "topic://VirtualTopic.eng.repotracker.container.tag.updated",
            "created": "2018-11-01T23:29:20.140308268Z",
            "action": "updated",
            "message-id": "ID:messaging-devops-broker01.dev1.ext.devlab.redhat.com-39068-1541025216899-3:4150:0:0:1",
            "os": "linux",
            "priority": "4"
        },
        "msg": {
            "old_digest": "sha256:05329d12087818843f353c7d566b4442ceb67d871a049b3b1b88923b72635772",
            "created": "2018-11-01T23:29:20.140308268Z",
            "os": "linux",
            "labels": {
                "vendor": "Factory 2.0",
                "name": "repotracker",
                "license": "GPLv3"
            },
            "repo": "quay.io/factory2/repotracker",
            "tag": "testtag",
            "reponame": "repotracker",
            "action": "updated",
            "arch": "amd64",
            "digest": "sha256:edf137791b86ac018ea1c29ddfddf7501fc4b383dc1a805d47aa83c2ff6ef9bc"
        }
    }


class TestRepotrackerRemoved(fedmsg.tests.test_meta.Base):
    """ repotracker tracks container repositories, and publishes a message when they change.

    A "removed" message is published whenever a tag is removed from a repo.
    """
    expected_title = 'repotracker.container.tag.removed'
    expected_subti = 'testtag tag was removed from the repotracker container repository'
    expected_link = 'https://quay.io/factory2/repotracker'
    expected_icon = '/umb/_static/img/icons/repotracker.png'

    msg = {
        "i": 0,
        "timestamp": 1541169058.0,
        "msg_id": "ID:messaging-devops-broker01.dev1.ext.devlab.redhat.com-39068-1541025216899-3:4206:0:0:1",
        "topic": "/topic/VirtualTopic.eng.repotracker.container.tag.removed",
        "headers": {
            "correlation-id": "d59e960c-f7a7-403d-a7f5-c0ff980fd512",
            "JMS_AMQP_PROPERTIES": "true",
            "tag": "testtag",
            "reponame": "repotracker",
            "digest": "null",
            "JMS_AMQP_ORIGINAL_ENCODING": "5",
            "JMS_AMQP_HEADER": "true",
            "original-destination": "/topic/VirtualTopic.eng.repotracker.container.tag.removed",
            "destination": "/topic/VirtualTopic.eng.repotracker.container.tag.removed",
            "amq6100-destination": "queue://Consumer.client-datanommer.upshift-dev.VirtualTopic.eng.>",
            "old_digest": "sha256:edf137791b86ac018ea1c29ddfddf7501fc4b383dc1a805d47aa83c2ff6ef9bc",
            "timestamp": "0",
            "expires": "0",
            "repo": "quay.io/factory2/repotracker",
            "arch": "null",
            "subscription": "/queue/Consumer.client-datanommer.upshift-dev.VirtualTopic.eng.>",
            "amq6100-originalDestination": "topic://VirtualTopic.eng.repotracker.container.tag.removed",
            "created": "null",
            "action": "removed",
            "message-id": "ID:messaging-devops-broker01.dev1.ext.devlab.redhat.com-39068-1541025216899-3:4206:0:0:1",
            "os": "null",
            "priority": "4"
        },
        "msg": {
            "old_digest": "sha256:edf137791b86ac018ea1c29ddfddf7501fc4b383dc1a805d47aa83c2ff6ef9bc",
            "created": None,
            "os": None,
            "labels": {},
            "repo": "quay.io/factory2/repotracker",
            "tag": "testtag",
            "reponame": "repotracker",
            "action": "removed",
            "arch": None,
            "digest": None
        }
    }


add_doc(locals())

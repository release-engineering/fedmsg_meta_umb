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


class TestODCSStateChange(fedmsg.tests.test_meta.Base):

    expected_title = 'odcs.state.change'
    expected_subti = 'osbs\'s compose of osbs-test-odcs transitioned to done.'
    expected_link = (
        'http://odcs.host.stage.eng.bos.redhat.com/'
        'composes/latest-odcs-185-1/compose/Temporary/odcs-185.repo')
    expected_icon = (
        'https://datagrepper-prod-datanommer.int.open.paas.redhat.com/'
        'umb/_static/img/icons/odcs.png')
    expected_usernames = set(['osbs'])

    msg = {
        "i": 0,
        "timestamp": 1512981522.0,
        "msg_id": "ID:broker.domain-45752-1512505691529-2:38975:0:0:1",
        "topic": "/topic/VirtualTopic.eng.odcs.state.change",
        "headers": {
            "content-length": "629",
            "destination": "/topic/VirtualTopic.eng.odcs.state.change",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "expires": "0",
            "priority": "4",
            "message-id": "ID:broker.domain-45752-1512505691529-2:38975:0:0:1",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-"
            "stage.VirtualTopic.eng.>"
        },
        "msg": {
            "compose": {
                "state_name": "done",
                "source_type": 1,
                "sigkeys": "37017186 FD431D51 DB42A60E",
                "time_submitted": "2017-12-11T08:38:33Z",
                "results": ["repository"],
                "time_removed": None,
                "source": "osbs-test-odcs",
                "state": 2,
                "time_to_expire": "2017-12-12T08:38:33Z",
                "flags": [],
                "time_done": "2017-12-11T08:38:41Z",
                "owner": "UID=osbs,OU=users,DC=redhat,DC=com",
                "result_repo": "http://odcs.host.stage.eng.bos.redhat.com/"
                "composes/latest-odcs-185-1/compose/Temporary",
                "id": 185,
                "result_repofile": "http://odcs.host.stage.eng.bos.redhat.com/"
                "composes/latest-odcs-185-1/compose/Temporary/odcs-185.repo"
            },
            "event": "state-changed"
        }
    }

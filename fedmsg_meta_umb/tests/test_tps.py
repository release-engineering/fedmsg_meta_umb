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
# Authors:  Gowrishankar Rajaiyan <grajaiya@redhat.com>

import fedmsg.tests.test_meta


class TestTPSStart(fedmsg.tests.test_meta.Base):
    """ TPS performs basic package sanity testing of rpms.

    Messages (like the example given here) are published when an **TPS**
    job is **starting**. (A TPS job performs basic sanity testing for the given brew build).
    """
    expected_title = 'tps.starting'
    expected_packages = set(['systemd'])
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1508850608.0,
        "msg_id": "ID\\somebroker-43669-1508744086399-2\\83144\\0\\0\\1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.tps.starting",
        "headers": {
            "ci_type": "ci-tps",
            "content-length": "43",
            "expires": "0",
            "brew_task_id": "14346234",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.tps.starting",
            "component": "systemd-219-45.el7",
            "priority": "4",
            "message-id": "ID\\somebroker-43669-1508744086399-2\\83144\\0\\0\\1",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "start_time": "2017-10-24T13:06:35+00:00"
        }
    }

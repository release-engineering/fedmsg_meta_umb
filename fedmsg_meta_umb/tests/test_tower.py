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
# Authors:  Ales Raszka <araszka@redhat.com>

import fedmsg.tests.test_meta

class TestTower(fedmsg.tests.test_meta.Base):
    """
    Test of Tower2UMB handler

    Messages (like the example given here) are published when
    a job in Tower finishes
    """
    expected_title = 'tower'
    expected_subti = 'Tower template Tower2UMB - ping finished - failed'
    expected_link = ('https://tower.engineering.redhat.com/#/jobs/37121')
    expected_objects = set([37121])
    expected_usernames = {'araszka'}

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1537454841.0,
        "msg_id": "ID:messaging-devops-broker01.web.stage.ext.phx2.redhat.com-39834-1537414777669-3:506:-1:1:2",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.tower",
        "headers": {
            "status": "failed",
            "project": "Tower2UMB",
            "expires": "1538059641455",
            "name": "Tower2UMB - ping",
            "timestamp": "1537454841455",
            "destination": "/topic/VirtualTopic.eng.tower",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker01.web.stage.ext.phx2.redhat.com-39834-1537414777669-3:506:-1:1:2",
            "content-type": "application/json",
            "subscription": "/queue/Consumer.client-datanommer.upshift-stage.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.9.1",
        "msg": {
            "status": "failed",
            "credential": "ansible",
            "name": "Tower2UMB - ping",
            "started": "2018-09-20T14:47:04.527121Z",
            "extra_vars": "{}",
            "traceback": "",
            "friendly_name": "Job",
            "created_by": "araszka",
            "project": "Tower2UMB",
            "url": "https://tower.engineering.redhat.com/#/jobs/37121",
            "finished": "2018-09-20T14:47:20.823051Z",
            "hosts": {
                "localhost": {
                    "skipped": 0,
                    "ok": 0,
                    "changed": 0,
                    "dark": 1,
                    "failed": True,
                    "processed": 1,
                    "failures": 0
                }
            },
            "inventory": "Tower2UMB",
            "limit": "",
            "id": 37121,
            "playbook": "playbooks/ping.yml"
        }
    }

class TestTowerUnknownMessage(fedmsg.tests.test_meta.Base):
    """
    Test of Tower2UMB handler - unknown message format

    Messages (like the example given here) are published when
    a job in Tower finishes
    """
    expected_title = 'tower'
    expected_subti = 'Unknown message format'

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1537454841.0,
        "msg_id": "ID:messaging-devops-broker01.web.stage.ext.phx2.redhat.com-39834-1537414777669-3:506:-1:1:2",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.tower",
        "headers": {
            "status": "failed",
            "project": "Tower2UMB",
            "expires": "1538059641455",
            "name": "Tower2UMB - ping",
            "timestamp": "1537454841455",
            "destination": "/topic/VirtualTopic.eng.tower",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker01.web.stage.ext.phx2.redhat.com-39834-1537414777669-3:506:-1:1:2",
            "content-type": "application/json",
            "subscription": "/queue/Consumer.client-datanommer.upshift-stage.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.9.1",
        "msg": "Bad message format"
    }

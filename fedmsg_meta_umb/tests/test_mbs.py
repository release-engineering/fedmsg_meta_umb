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
from .common import add_doc


class TestMBSStateChange(fedmsg.tests.test_meta.Base):
    """ The Module Build Service (MBS) builds modules.

    During the course of a "module build", the build will transition through a
    number of states.  Every time it changes, the MBS will publish a message
    much like this one:
    """
    expected_title = 'mbs.module.state.change'
    expected_subti = ('tdawson\'s build of foobar-linux-9000 '
                      'transitioned to the "done" state.')
    expected_link = 'https://mbsweb.engineering.redhat.com/module/40'
    expected_agent = 'tdawson'
    expected_usernames = set(['tdawson'])
    expected_packages = set(['foobar'])
    expected_icon = (
        'https://datagrepper-prod-datanommer.int.open.paas.redhat.com/'
        'umb/_static/img/icons/mbs.png')

    msg = {
        "username": None,
        "i": 0,
        "timestamp": 1509048641.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-43669-1508744086399-3:5230:-1:1:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.mbs.module.state.change",
        "headers": {
            "content-length": "3904",
            "expires": "1509653413799",
            "timestamp": "1509048613799",
            "destination": "/topic/VirtualTopic.eng.mbs.module.state.change",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-43669-1508744086399-3:5230:-1:1:1",
            "content-type": "text/json",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "msg": {
            "state_reason": None,
            "component_builds": [
                2182,
                2179,
                2177,
                2180,
                2178,
                2181
            ],
            "name": "foobar",
            "stream": "linux-9000",
            "time_submitted": "2017-10-26T17:13:18Z",
            "tasks": {
                "rpms": {
                    "keyutils": {
                        "state": 1,
                        "nvr": "keyutils-1.5.10-3.el8+a8c57dc5",
                        "task_id": 14380509,
                        "state_reason": ""
                    },
                    "kernel": {
                        "state": 1,
                        "nvr": "kernel-4.14.0-0.rc3.git0.1.el8+a8c57dc5",
                        "task_id": 14380510,
                        "state_reason": ""
                    },
                    "quota": {
                        "state": 1,
                        "nvr": "quota-4.03-9.el8+a8c57dc5",
                        "task_id": 14380517,
                        "state_reason": ""
                    },
                    "e2fsprogs": {
                        "state": 1,
                        "nvr": "e2fsprogs-1.43.6-1.el8+a8c57dc5",
                        "task_id": 14380519,
                        "state_reason": ""
                    },
                    "cachefilesd": {
                        "state": 1,
                        "nvr": "cachefilesd-0.10.10-3.el8+a8c57dc5",
                        "task_id": 14380514,
                        "state_reason": ""
                    },
                    "module-build-macros": {
                        "state": 1,
                        "nvr": "module-build-macros-0.1-1.el8+a8c57dc5",
                        "task_id": 14380271,
                        "state_reason": ""
                    }
                }
            },
            "state_url": "http://localhost/module-build-service/1/module-builds/40",
            "time_modified": "2017-10-26T20:10:13Z",
            "scmurl": "git://pkgs.devel.redhat.com/modules/foobar?#e160b976daf28d17770c3cd1b33f388155688944",
            "state": 3,
            "modulemd": "data:\n    components:\n        rpms:\n  ...",
            "koji_tag": "module-a8c57dc51895c3b4",
            "time_completed": "2017-10-26T20:10:13Z",
            "version": "20171026171229",
            "owner": "tdawson",
            "state_trace": [
                {
                    "reason": None,
                    "time": "2017-10-26T17:13:22Z",
                    "state": 1,
                    "state_name": "wait"
                },
                {
                    "reason": None,
                    "time": "2017-10-26T17:13:40Z",
                    "state": 1,
                    "state_name": "wait"
                },
                {
                    "reason": None,
                    "time": "2017-10-26T17:13:44Z",
                    "state": 2,
                    "state_name": "build"
                },
                {
                    "reason": None,
                    "time": "2017-10-26T17:13:46Z",
                    "state": 2,
                    "state_name": "build"
                },
                {
                    "reason": None,
                    "time": "2017-10-26T17:21:53Z",
                    "state": 2,
                    "state_name": "build"
                },
                {
                    "reason": None,
                    "time": "2017-10-26T17:23:55Z",
                    "state": 2,
                    "state_name": "build"
                }
            ],
            "id": 40,
            "state_name": "done"
        }
    }


add_doc(locals())

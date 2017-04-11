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
# Authors:  Mike Bonnet <mikeb@redhat.com>

import test_brew

class BrewTaskBase(test_brew.BrewBase):
    @property
    def expected_title(self):
        return 'brew.task.' + self.expected_state

class TestBrewTaskFree(BrewTaskBase):
    expected_state = 'free'
    expected_subti = 'newRepo task 18064 has been created'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taskinfo?taskID=18064'
    msg = {
        "i": 0,
        "timestamp": 1488318030.0,
        "msg_id": "239f9b70-84cb-4774-9365-dfbf0264602b",
        "topic": "/topic/VirtualTopic.eng.brew.task.free",
        "msg": {
            "info": {
                "parent": None,
                "request": "<?xml version='1.0'?>\n<methodCall>\n<methodName>newRepo</methodName>\n<params>\n<param>\n<value><string>rhel-7.4-candidate</string></value>\n</param>\n</params>\n</methodCall>\n",
                "id": 18064,
                "priority": 15,
                "channel_id": 2,
                "state": 0,
                "owner": 1,
                "label": None,
                "arch": "noarch",
                "method": "newRepo",
                "channel": "createrepo"
            },
            "attribute": "state",
            "old": None,
            "new": "FREE"
        }
    }

class TestBrewTaskOpen(BrewTaskBase):
    expected_state = 'open'
    expected_subti = 'build task 12812867 has started'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taskinfo?taskID=12812867'
    msg = {
        "i": 0,
        "timestamp": 1490052482.0,
        "msg_id": "1c1ed177-d137-403c-bfc2-2905e6171c52",
        "topic": "/topic/VirtualTopic.eng.brew.task.open",
        "msg": {
            "info": {
                "weight": 1.0,
                "parent": None,
                "completion_time": None,
                "start_ts": 1490052504.07159,
                "start_time": "2017-03-20 23:28:24.071589",
                "request": [
                    "git://pkgs.devel.redhat.com/rpms/kernel-rt?#8211e397155a7bc5edc36d3a4499ad53454a2b94",
                    "rhel-7.4-candidate",
                    {}
                ],
                "waiting": None,
                "awaited": None,
                "label": None,
                "priority": 20,
                "channel_id": 11,
                "state": 1,
                "create_time": "2017-03-20 23:28:12.506607",
                "create_ts": 1490052492.50661,
                "owner": 588,
                "host_id": 95,
                "method": "build",
                "completion_ts": None,
                "arch": "noarch",
                "id": 12812867
            },
            "attribute": "state",
            "old": "FREE",
            "new": "OPEN"
        }
    }

class TestBrewTaskClosed(BrewTaskBase):
    expected_state = 'closed'
    expected_subti = 'buildArch task 12812639 has completed'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taskinfo?taskID=12812639'
    msg = {
        "i": 0,
        "timestamp": 1490052905.0,
        "msg_id": "f5aabce8-abf4-4607-86da-bf8ac4668144",
        "topic": "/topic/VirtualTopic.eng.brew.task.closed",
        "msg": {
            "info": {
                "weight": 2.93294190937,
                "parent": 12812634,
                "completion_time": "2017-03-20 23:35:26.957282",
                "start_ts": 1490049676.79981,
                "start_time": "2017-03-20 22:41:16.799812",
                "request": [
                    "cli-build/1490047793.281109.ZJGYFfrz/kernel-2.6.32-504.38.1.el6.01739954.src.rpm",
                    9114,
                    "i686",
                    False,
                    {
                        "repo_id": 1939802
                    }
                ],
                "waiting": None,
                "awaited": True,
                "label": "i686",
                "priority": 19,
                "channel_id": 9,
                "state": 2,
                "create_time": "2017-03-20 22:40:53.128651",
                "create_ts": 1490049653.12865,
                "owner": 2121,
                "host_id": 147,
                "method": "buildArch",
                "completion_ts": 1490052926.95728,
                "arch": "i386",
                "id": 12812639,
                "result": {
                    "rpms": [
                        "tasks/2639/12812639/kernel-debug-2.6.32-504.38.1.el6.01739954.i686.rpm",
                        "tasks/2639/12812639/kernel-debuginfo-2.6.32-504.38.1.el6.01739954.i686.rpm",
                        "tasks/2639/12812639/perf-debuginfo-2.6.32-504.38.1.el6.01739954.i686.rpm",
                        "tasks/2639/12812639/python-perf-debuginfo-2.6.32-504.38.1.el6.01739954.i686.rpm",
                        "tasks/2639/12812639/kernel-debuginfo-common-i686-2.6.32-504.38.1.el6.01739954.i686.rpm",
                        "tasks/2639/12812639/kernel-devel-2.6.32-504.38.1.el6.01739954.i686.rpm",
                        "tasks/2639/12812639/kernel-headers-2.6.32-504.38.1.el6.01739954.i686.rpm",
                        "tasks/2639/12812639/python-perf-2.6.32-504.38.1.el6.01739954.i686.rpm",
                        "tasks/2639/12812639/perf-2.6.32-504.38.1.el6.01739954.i686.rpm",
                        "tasks/2639/12812639/kernel-debug-devel-2.6.32-504.38.1.el6.01739954.i686.rpm",
                        "tasks/2639/12812639/kernel-debug-debuginfo-2.6.32-504.38.1.el6.01739954.i686.rpm",
                        "tasks/2639/12812639/kernel-2.6.32-504.38.1.el6.01739954.i686.rpm"
                    ],
                    "brootid": 3253546,
                    "srpms": [],
                    "logs": [
                        "tasks/2639/12812639/build.log",
                        "tasks/2639/12812639/root.log",
                        "tasks/2639/12812639/state.log"
                    ]
                }
            },
            "attribute": "state",
            "old": "OPEN",
            "new": "CLOSED"
        }
    }

class TestBrewTaskCanceled(BrewTaskBase):
    expected_state = 'canceled'
    expected_subti = 'buildArch task 12822614 has been canceled'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taskinfo?taskID=12822614'
    msg = {
        "i": 0,
        "timestamp": 1490118460.0,
        "msg_id": "3cb070b4-faf9-4c80-b6dc-cbe0fa6f5812",
        "topic": "/topic/VirtualTopic.eng.brew.task.canceled",
        "msg": {
            "info": {
                "weight": 2.26420799958,
                "parent": 12822603,
                "completion_time": "2017-03-21 17:48:01.703416",
                "start_ts": 1490117230.58976,
                "start_time": "2017-03-21 17:27:10.589763",
                "request": [
                    "cli-build/1490117191.258269.JHwzgjKh/python-2.7.5-54.el7.src.rpm",
                    9899,
                    "ppc64le",
                    False,
                    {
                        "repo_id": 1943198
                    }
                ],
                "waiting": None,
                "awaited": True,
                "label": "ppc64le",
                "priority": 19,
                "channel_id": 11,
                "state": 3,
                "create_time": "2017-03-21 17:27:02.871697",
                "create_ts": 1490117222.8717,
                "owner": 3344,
                "host_id": 136,
                "method": "buildArch",
                "completion_ts": 1490118481.70342,
                "arch": "ppc64le",
                "id": 12822614
            },
            "attribute": "state",
            "old": "OPEN",
            "new": "CANCELED"
        }
    }

class TestBrewTaskAssigned(BrewTaskBase):
    expected_state = 'assigned'
    expected_subti = 'buildSRPMFromSCM task 12812517 has been assigned'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taskinfo?taskID=12812517'
    msg = {
        "i": 0,
        "timestamp": 1490047718.0,
        "msg_id": "b4f23ea0-af61-44d2-b9c1-cf82dffb8470",
        "topic": "/topic/VirtualTopic.eng.brew.task.assigned",
        "msg": {
            "info": {
                "weight": 1.0,
                "parent": 12812515,
                "completion_time": None,
                "start_ts": 1490047724.80226,
                "start_time": "2017-03-20 22:08:44.802256",
                "request": [
                    "git://pkgs.devel.redhat.com/rpms/ntp?#acd9a8595b68518ded106bb4a7ea8518f6f7c129",
                    9899,
                    {
                        "repo_id": 1941359
                    }
                ],
                "waiting": None,
                "awaited": True,
                "label": "srpm",
                "priority": 19,
                "channel_id": 11,
                "state": 4,
                "create_time": "2017-03-20 22:08:44.115594",
                "create_ts": 1490047724.11559,
                "owner": 2,
                "host_id": 176,
                "method": "buildSRPMFromSCM",
                "completion_ts": None,
                "arch": "noarch",
                "id": 12812517
            },
            "attribute": "state",
            "old": "OPEN",
            "new": "ASSIGNED"
        }
    }

class TestBrewTaskFailed(BrewTaskBase):
    expected_state = 'failed'
    expected_subti = 'buildArch task 12826300 has failed'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taskinfo?taskID=12826300'
    msg = {
        "i": 0,
        "timestamp": 1490134717.0,
        "msg_id": "2a82d688-0679-4312-b03f-cd6434b07f62",
        "topic": "/topic/VirtualTopic.eng.brew.task.failed",
        "msg": {
            "info": {
                "weight": 6.0,
                "parent": 12826299,
                "completion_time": "2017-03-21 22:18:59.777722",
                "start_ts": 1490132075.80638,
                "start_time": "2017-03-21 21:34:35.806375",
                "request": [
                    "cli-build/1490131138.120602.GoxqgsQj/libreoffice-5.0.6.2-6.el7.src.rpm",
                    10495,
                    "x86_64",
                    True,
                    {
                        "repo_id": 1943876
                    }
                ],
                "waiting": None,
                "awaited": True,
                "label": "x86_64",
                "priority": 19,
                "channel_id": 11,
                "state": 5,
                "create_time": "2017-03-21 21:34:20.977687",
                "create_ts": 1490132060.97769,
                "owner": 740,
                "host_id": 110,
                "method": "buildArch",
                "completion_ts": 1490134739.77772,
                "arch": "x86_64",
                "id": 12826300
            },
            "attribute": "state",
            "old": "OPEN",
            "new": "FAILED"
        }
    }

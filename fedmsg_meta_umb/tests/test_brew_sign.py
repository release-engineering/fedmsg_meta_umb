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

class TestBrewSignRPM(test_brew.BrewBase):
    expected_title = 'brew.sign.rpm'
    expected_subti = 'libvirt-devel-3.2.0-2.el7.x86_64.rpm has been signed with key fd431d51'
    expected_packages = set(['libvirt'])
    expected_usernames = set(['jdenemar'])
    msg = {
        "i": 0,
        "timestamp": 1491937664.0,
        "msg_id": "80d5593a-db12-49ab-9419-5516bdd55ea8",
        "topic": "/topic/VirtualTopic.eng.brew.sign.rpm",
        "msg": {
            "sighash": "fc030b062b00969ece88b42099adc306",
            "sigkey": "fd431d51",
            "rpm": {
                "build_id": 549993,
                "name": "libvirt-devel",
                "extra": None,
                "arch": "x86_64",
                "buildtime": 1491832854,
                "id": 4634284,
                "epoch": None,
                "version": "3.2.0",
                "metadata_only": False,
                "external_repo_id": 0,
                "release": "2.el7",
                "size": 300924,
                "buildroot_id": 3284277,
                "external_repo_name": "INTERNAL",
                "payloadhash": "3ef74d49c41e85c9979a149c3d05275d"
            },
            "build": {
                "package_name": "libvirt",
                "extra": None,
                "creation_time": "2017-04-10 13:55:25.254418",
                "completion_time": "2017-04-10 14:12:25.27925",
                "package_id": 1989,
                "id": 549993,
                "build_id": 549993,
                "state": 1,
                "source": None,
                "epoch": None,
                "version": "3.2.0",
                "completion_ts": 1491833545.27925,
                "owner_id": 798,
                "owner_name": "jdenemar",
                "nvr": "libvirt-3.2.0-2.el7",
                "start_time": "2017-04-10 13:55:25.254418",
                "creation_event_id": 15394787,
                "start_ts": 1491832525.25442,
                "volume_id": 0,
                "creation_ts": 1491832525.25442,
                "name": "libvirt",
                "task_id": 12980391,
                "volume_name": "DEFAULT",
                "release": "2.el7"
            }
        }
    }

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

class TestBrewPackageAdd(test_brew.BrewBase):
    expected_title = 'brew.package.add'
    expected_subti = 'package jboss-logging was added to tag jb-eap-7.1-rhel-7'
    expected_packages = set(['jboss-logging'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/packageinfo?packageID=32324'
    msg = {
        "i": 0,
        "timestamp": 1490890860.0,
        "msg_id": "47f155fe-549c-4fc1-b6cd-738d4e1995bc",
        "topic": "/topic/VirtualTopic.eng.brew.package.add",
        "msg": {
            "force": None,
            "package": {
                "id": 32324,
                "name": "jboss-logging"
            },
            "extra_arches": None,
            "update": False,
            "owner": 3099,
            "tag": {
                "maven_support": False,
                "locked": True,
                "name": "jb-eap-7.1-rhel-7",
                "extra": {},
                "perm": None,
                "perm_id": None,
                "arches": None,
                "maven_include_all": False,
                "id": 9356
            },
            "action": "add",
            "block": False
        }
    }

class TestBrewPackageUpdate(test_brew.BrewBase):
    expected_title = 'brew.package.update'
    expected_subti = 'package iotop was updated in tag rhel-7.4-set'
    expected_packages = set(['iotop'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/packageinfo?packageID=12877'
    msg = {
        "i": 0,
        "timestamp": 1490709503.0,
        "msg_id": "93d5cf48-d6ad-4a42-90cf-3b790f6e2bb9",
        "topic": "/topic/VirtualTopic.eng.brew.package.update",
        "msg": {
            "force": True,
            "package": {
                "id": 12877,
                "name": "iotop"
            },
            "extra_arches": None,
            "update": True,
            "owner": 746,
            "tag": {
                "maven_support": False,
                "locked": False,
                "name": "rhel-7.4-set",
                "extra": {},
                "perm": "admin",
                "perm_id": 1,
                "arches": None,
                "maven_include_all": False,
                "id": 10819
            },
            "action": "update",
            "block": False
        }
    }

class TestBrewPackageBlock(test_brew.BrewBase):
    expected_title = 'brew.package.block'
    expected_subti = 'package python-mock was blocked in tag extras-rhel-7.4-set'
    expected_packages = set(['python-mock'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/packageinfo?packageID=34523'
    msg = {
        "i": 0,
        "timestamp": 1490195003.0,
        "msg_id": "ee19ce13-a0a3-46bd-91c5-921bef874016",
        "topic": "/topic/VirtualTopic.eng.brew.package.block",
        "msg": {
            "force": False,
            "package": {
                "id": 34523,
                "name": "python-mock"
            },
            "extra_arches": None,
            "update": False,
            "owner": 2838,
            "tag": {
                "maven_support": False,
                "locked": False,
                "name": "extras-rhel-7.4-set",
                "extra": {},
                "perm": "trusted",
                "perm_id": 6,
                "arches": None,
                "maven_include_all": False,
                "id": 10767
            },
            "action": "block",
            "block": True
        }
    }

class TestBrewPackageUnblock(test_brew.BrewBase):
    expected_title = 'brew.package.unblock'
    expected_subti = 'package rdma-core was unblocked in tag rhel-7.4'
    expected_packages = set(['rdma-core'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/packageinfo?packageID=61658'
    msg = {
        "i": 0,
        "timestamp": 1489765815.0,
        "msg_id": "aa80f510-feec-4577-8886-b2645b4de58b",
        "topic": "/topic/VirtualTopic.eng.brew.package.unblock",
        "msg": {
            "action": "unblock",
            "tag": {
                "maven_support": False,
                "locked": False,
                "name": "rhel-7.4",
                "extra": {},
                "perm": "admin",
                "perm_id": 1,
                "arches": None,
                "maven_include_all": False,
                "id": 9894
            },
            "package": {
                "id": 61658,
                "name": "rdma-core"
            }
        }
    }

class TestBrewPackageRemove(test_brew.BrewBase):
    expected_title = 'brew.package.remove'
    expected_subti = 'package python-nose was removed from tag rhel-7.4-build'
    expected_packages = set(['python-nose'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/packageinfo?packageID=4323'
    msg = {
        "i": 0,
        "timestamp": 1490351237.0,
        "msg_id": "369459c1-a8ce-4bb6-9778-293c2bfe0c4b",
        "topic": "/topic/VirtualTopic.eng.brew.package.remove",
        "msg": {
            "action": "remove",
            "tag": {
                "maven_support": False,
                "locked": False,
                "name": "rhel-7.4-build",
                "extra": {},
                "perm": "admin",
                "perm_id": 1,
                "arches": "i686 x86_64 ppc ppc64 ppc64le s390 s390x aarch64",
                "maven_include_all": False,
                "id": 9899
            },
            "package": {
                "id": 4323,
                "name": "python-nose"
            }
        }
    }

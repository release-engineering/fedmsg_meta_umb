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

class TestBrewRepoInit(test_brew.BrewBase):
    expected_title = 'brew.repo.init'
    expected_subti = 'repo 1961878 for rhel-7.4-build is being created'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taginfo?tagID=9899'
    msg = {
        "i": 0,
        "timestamp": 1490973066.0,
        "msg_id": "806a55b1-5014-43a5-9362-817c090996be",
        "topic": "/topic/VirtualTopic.eng.brew.repo.init",
        "source_version": "0.6.5",
        "signature": None,
        "msg": {
            "with_src": False,
            "with_debuginfo": False,
            "repo_id": 1961878,
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
            "event": None
        }
    }

class TestBrewRepoDone(test_brew.BrewBase):
    expected_title = 'brew.repo.done'
    expected_subti = 'repo 1961874 for jb-eap-6.3-jdk7-rhel-6-build has been created'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taginfo?tagID=6626'
    msg = {
        "i": 0,
        "timestamp": 1490973142.0,
        "msg_id": "b99b6445-f8cb-4532-a7b3-1cb06540439e",
        "topic": "/topic/VirtualTopic.eng.brew.repo.done",
        "msg": {
            "repo": {
                "create_event": 15291857,
                "creation_time": "2017-03-31 15:01:41.106243",
                "tag_name": "jb-eap-6.3-jdk7-rhel-6-build",
                "tag_id": 6626,
                "state": 0,
                "create_ts": 1490972501.10624,
                "id": 1961874
            },
            "expire": False,
            "data": {
                "x86_64": [
                    "tasks/8792/12918792",
                    [
                        "1e4feca4ea3d5f598d1be8666d90a4af0c803316a0ffa166f1023c666237f374-comps.xml.gz",
                        "primary.xml.gz",
                        "c7ac64e14242c5417436cfc10225f4a559d989a180ece78769a68542d1916839-other.sqlite.bz2",
                        "f143b4220b9237fe62c6a5ae699f270d1cc0fe9b9c44582e1f85bf5a40ab21dc-filelists.sqlite.bz2",
                        "repomd.xml",
                        "781f361c7323db0891e799b16c0cb3f30102259d56e3a63869d6a8b1a7a8d9a9-comps.xml.gz",
                        "filelists.xml.gz",
                        "other.xml.gz",
                        "1b05ee5edf3b6b2b598cb3dcb55a38a45b267ae9ae5f08374dcf0180d04f3c9e-primary.xml.gz",
                        "84ea58b0b9889961fc0f706f69763fde8ca463f9fe2a5694fadf459d130592f9-comps.xml",
                        "91ab4470004bdae24e8e8a16f43c025c451923f3fa0eb632226ecdc7dff44b4d-primary.sqlite.bz2",
                        "6e230ed35977838a9c5a68281948788dc9efa7359b1029450c8c152297d091c9-filelists.xml.gz",
                        "9b0e3103f1f2a6e46d1f2739b5e571018e9508b056e1b81bd7bef2bbbe34c9d5-other.xml.gz",
                        "38cd9b4022b5adf14ebed57de9195a83a7b2538abac4ce01879bde1f014d35b7-comps.xml"
                    ]
                ]
            }
        }
    }

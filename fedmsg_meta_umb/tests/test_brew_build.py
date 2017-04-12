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

from . import test_brew

class TestBrewBuildBuilding(test_brew.BrewBase):
    expected_title = 'brew.build.building'
    expected_subti = 'selinux-policy-3.13.1-136.el7 is building'
    expected_packages = set(['selinux-policy'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/buildinfo?buildID=547678'
    msg = {
        "i": 0,
        "timestamp": 1490891323.0,
        "msg_id": "9b697089-c192-49eb-a110-4754209a43f5",
        "topic": "/topic/VirtualTopic.eng.brew.build.building",
        "msg": {
            "info": {
                "start_time": "NOW",
                "name": "selinux-policy",
                "task_id": 12910431,
                "extra": None,
                "pkg_id": 2989,
                "state": 0,
                "completion_time": None,
                "epoch": None,
                "version": "3.13.1",
                "source": None,
                "volume_id": 0,
                "owner": 2752,
                "release": "136.el7",
                "id": 547678
            },
            "attribute": "state",
            "old": 3,
            "new": 0
        }
    }

class TestBrewBuildComplete(test_brew.BrewBase):
    expected_title = 'brew.build.complete'
    expected_subti = 'org.jboss-jboss-dmr-1.4.0.Final_redhat_1-1 has been built successfully'
    expected_packages = set(['org.jboss-jboss-dmr'])
    expected_usernames = set(['psakar'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/buildinfo?buildID=547865'
    msg = {
        "i": 0,
        "timestamp": 1490946728.0,
        "msg_id": "5372c2d5-ff01-49b4-97f5-71445264fece",
        "topic": "/topic/VirtualTopic.eng.brew.build.complete",
        "msg": {
            "info": {
                "package_name": "org.jboss-jboss-dmr",
                "extra": None,
                "creation_time": "2017-03-31 07:52:33.843957",
                "completion_time": None,
                "package_id": 31785,
                "id": 547865,
                "build_id": 547865,
                "state": 0,
                "source": None,
                "epoch": None,
                "version": "1.4.0.Final_redhat_1",
                "completion_ts": None,
                "owner_id": 3099,
                "owner_name": "psakar",
                "nvr": "org.jboss-jboss-dmr-1.4.0.Final_redhat_1-1",
                "start_time": "2017-03-31 07:52:33.843957",
                "creation_event_id": 15289596,
                "start_ts": 1490946753.84396,
                "volume_id": 0,
                "creation_ts": 1490946753.84396,
                "name": "org.jboss-jboss-dmr",
                "task_id": 12915073,
                "volume_name": "DEFAULT",
                "release": "1"
            },
            "attribute": "state",
            "old": 0,
            "new": 1
        }
    }

class TestBrewBuildCompleteDocker(test_brew.BrewBase):
    expected_title = 'brew.build.complete'
    expected_subti = 'metrics-cassandra-docker-3.6.0-3 has been built successfully'
    expected_packages = set(['metrics-cassandra-docker'])
    expected_usernames = set()
    expected_link = 'https://brewweb.engineering.redhat.com/brew/buildinfo?buildID=550925'
    msg = {
        "i": 0,
        "timestamp": 1491951183.0,
        "msg_id": "ffcbdc40-1435-492f-83f9-51b9892b9524",
        "topic": "/topic/VirtualTopic.eng.brew.build.complete",
        "msg": {
            "info": {
                "start_time": "2017-04-11 22:42:53",
                "name": "metrics-cassandra-docker",
                "task_id": None,
                "extra": "{\"image\": {\"autorebuild\": false, \"help\": null}, \"container_koji_task_id\": 12996137}",
                "pkg_id": 54389,
                "state": 1,
                "completion_time": "2017-04-11 22:52:49",
                "epoch": None,
                "version": "3.6.0",
                "source": "git://pkgs.devel.redhat.com/rpms/metrics-cassandra-docker#"
                "1c9ebc26c5066ed4894d45878bc90fd66046a292",
                "volume_id": 0,
                "owner": 3436,
                "release": "3",
                "id": 550925
            },
            "attribute": "state",
            "old": None,
            "new": 1
        }
    }

class TestBrewBuildDeleted(test_brew.BrewBase):
    expected_title = 'brew.build.deleted'
    expected_subti = 'elasticsearch-2.4.1-2.el7 has been deleted'
    expected_packages = set(['elasticsearch'])
    expected_usernames = set(['rmeggins'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/buildinfo?buildID=524863'
    msg = {
        "i": 0,
        "timestamp": 1490786161.0,
        "msg_id": "06a492c3-8758-4a08-aa34-279435de49d9",
        "topic": "/topic/VirtualTopic.eng.brew.build.deleted",
        "msg": {
            "info": {
                "package_name": "elasticsearch",
                "extra": None,
                "creation_time": "2016-11-16 23:56:35.580377",
                "completion_time": "2016-11-16 23:57:14.887771",
                "package_id": 34337,
                "id": 524863,
                "build_id": 524863,
                "state": 1,
                "source": None,
                "epoch": None,
                "version": "2.4.1",
                "completion_ts": 1479340634.88777,
                "owner_id": 425,
                "owner_name": "rmeggins",
                "nvr": "elasticsearch-2.4.1-2.el7",
                "start_time": "2016-11-16 23:56:35.580377",
                "creation_event_id": 14433958,
                "start_ts": 1479340595.58038,
                "volume_id": 0,
                "creation_ts": 1479340595.58038,
                "name": "elasticsearch",
                "task_id": 12116211,
                "volume_name": "DEFAULT",
                "release": "2.el7"
            },
            "attribute": "state",
            "old": 1,
            "new": 2
        }
    }

class TestBrewBuildFailed(test_brew.BrewBase):
    expected_title = 'brew.build.failed'
    expected_subti = 'build of libreoffice-5.0.6.2-8.el7 has failed'
    expected_packages = set(['libreoffice'])
    expected_usernames = set(['caolanm'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/buildinfo?buildID=547932'
    msg = {
        "i": 0,
        "timestamp": 1490978317.0,
        "msg_id": "9ff79b2a-67c2-4425-93d0-d7132f343b17",
        "topic": "/topic/VirtualTopic.eng.brew.build.failed",
        "msg": {
            "info": {
                "package_name": "libreoffice",
                "extra": None,
                "creation_time": "2017-03-31 16:17:10.988945",
                "completion_time": None,
                "package_id": 33948,
                "id": 547932,
                "build_id": 547932,
                "state": 0,
                "source": None,
                "epoch": 1,
                "version": "5.0.6.2",
                "completion_ts": None,
                "owner_id": 89,
                "owner_name": "caolanm",
                "nvr": "libreoffice-5.0.6.2-8.el7",
                "start_time": "2017-03-31 16:17:10.988945",
                "creation_event_id": 15292221,
                "start_ts": 1490977030.98895,
                "volume_id": 0,
                "creation_ts": 1490977030.98895,
                "name": "libreoffice",
                "task_id": 12919327,
                "volume_name": "DEFAULT",
                "release": "8.el7"
            },
            "attribute": "state",
            "old": 0,
            "new": 3
        }
    }

class TestBrewBuildCanceled(test_brew.BrewBase):
    expected_title = 'brew.build.canceled'
    expected_subti = 'build of libgpod-0.8.2-12.el7 has been canceled'
    expected_packages = set(['libgpod'])
    expected_usernames = set(['klember'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/buildinfo?buildID=543196'
    msg = {
        "i": 0,
        "timestamp": 1489097838.0,
        "msg_id": "073a7b61-8e23-4448-9c09-6e59aa2f911d",
        "topic": "/topic/VirtualTopic.eng.brew.build.canceled",
        "msg": {
            "info": {
                "package_name": "libgpod",
                "extra": None,
                "creation_time": "2017-03-09 22:16:04.788558",
                "completion_time": "2017-03-09 22:17:31.160826",
                "package_id": 1924,
                "id": 543196,
                "build_id": 543196,
                "state": 4,
                "source": None,
                "epoch": None,
                "version": "0.8.2",
                "completion_ts": 1489097851.16083,
                "owner_id": 3004,
                "owner_name": "klember",
                "nvr": "libgpod-0.8.2-12.el7",
                "start_time": "2017-03-09 22:16:04.788558",
                "creation_event_id": 15116085,
                "start_ts": 1489097764.78856,
                "volume_id": 0,
                "creation_ts": 1489097764.78856,
                "name": "libgpod",
                "task_id": 12732117,
                "volume_name": "DEFAULT",
                "release": "12.el7"
            },
            "attribute": "state",
            "old": 4,
            "new": 4
        }
    }

class TestBrewBuildTag(test_brew.BrewBase):
    expected_title = 'brew.build.tag'
    expected_subti = 'python-gssapi-1.2.0-3.el7 tagged into rhel-7.4-candidate'
    expected_packages = set(['python-gssapi'])
    expected_usernames = set(['rharwood'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/buildinfo?buildID=550575'
    msg = {
        "i": 0,
        "timestamp": 1491926538.0,
        "msg_id": "4307e30e-70c5-4d4a-9244-53b8860c067b",
        "topic": "/topic/VirtualTopic.eng.brew.build.tag",
        "msg": {
            "tag": {
                "maven_support": False,
                "locked": False,
                "name": "rhel-7.4-candidate",
                "extra": {},
                "perm": None,
                "perm_id": None,
                "arches": None,
                "maven_include_all": False,
                "id": 9895
            },
            "force": False,
            "build": {
                "package_name": "python-gssapi",
                "extra": None,
                "creation_time": "2017-04-11 15:57:37.130866",
                "completion_time": "2017-04-11 16:02:27.825432",
                "package_id": 52097,
                "id": 550575,
                "build_id": 550575,
                "state": 1,
                "source": None,
                "epoch": None,
                "version": "1.2.0",
                "completion_ts": 1491926547.82543,
                "owner_id": 2717,
                "owner_name": "rharwood",
                "nvr": "python-gssapi-1.2.0-3.el7",
                "start_time": "2017-04-11 15:57:37.130866",
                "creation_event_id": 15403058,
                "start_ts": 1491926257.13087,
                "volume_id": 0,
                "creation_ts": 1491926257.13087,
                "name": "python-gssapi",
                "task_id": 12990769,
                "volume_name": "DEFAULT",
                "release": "3.el7"
            },
            "user": {
                "status": 0,
                "krb_principal": "rharwood@REDHAT.COM",
                "usertype": 0,
                "id": 2717,
                "name": "rharwood"
            }
        }
    }

class TestBrewBuildUntag(test_brew.BrewBase):
    expected_title = 'brew.build.untag'
    expected_subti = 'luci-0.26.0-75.el6 untagged from RHEL-6.8-candidate'
    expected_packages = set(['luci'])
    expected_usernames = set(['host/x86-013.build.bos.redhat.com', 'rmccabe'])
    expected_link = 'https://brewweb.engineering.redhat.com/brew/buildinfo?buildID=480574'
    msg = {
        "i": 0,
        "timestamp": 1491940321.0,
        "msg_id": "a4b5d91a-c4db-4e09-99eb-f460609f22b3",
        "topic": "/topic/VirtualTopic.eng.brew.build.untag",
        "msg": {
            "strict": True,
            "tag": {
                "maven_support": False,
                "locked": False,
                "name": "RHEL-6.8-candidate",
                "extra": {},
                "perm": None,
                "perm_id": None,
                "arches": None,
                "maven_include_all": False,
                "id": 8179
            },
            "force": False,
            "build": {
                "package_name": "luci",
                "extra": None,
                "creation_time": "2016-02-16 07:21:48.354511",
                "completion_time": "2016-02-16 07:25:20.776579",
                "package_id": 18835,
                "id": 480574,
                "build_id": 480574,
                "state": 1,
                "source": None,
                "epoch": None,
                "version": "0.26.0",
                "completion_ts": 1455607520.77658,
                "owner_id": 471,
                "owner_name": "rmccabe",
                "nvr": "luci-0.26.0-75.el6",
                "start_time": "2016-02-16 07:21:48.354511",
                "creation_event_id": 12616125,
                "start_ts": 1455607308.35451,
                "volume_id": 0,
                "creation_ts": 1455607308.35451,
                "name": "luci",
                "task_id": 10500836,
                "volume_name": "DEFAULT",
                "release": "75.el6"
            },
            "user": {
                "status": 0,
                "krb_principal": "host/x86-013.build.bos.redhat.com@REDHAT.COM",
                "usertype": 0,
                "id": 1181,
                "name": "host/x86-013.build.bos.redhat.com"
            }
        }
    }

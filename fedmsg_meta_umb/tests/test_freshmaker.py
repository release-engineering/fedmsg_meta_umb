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
# Authors:  Chenxiong Qi <cqi@redhat.com>

import fedmsg.tests.test_meta


class TestManualRebuild(fedmsg.tests.test_meta.Base):

    expected_title = 'freshmaker.manual.rebuild'
    expected_subti = 'Manual rebuild is triggered for Errata advisory 31360.'
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/31360'
    expected_icon = '/umb/_static/img/icons/freshmaker.png'
    expected_packages = set([])

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1511940834.0,
        "msg_id": "ID:localhost-45704-1510236486219-2:66659:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.freshmaker.manual.rebuild",
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "errata_id": 31360
        }
    }


class TestBuildStateIsDone(fedmsg.tests.test_meta.Base):

    expected_title = 'freshmaker.build.state.changed'
    expected_subti = ('IMAGE rh-nodejs6-docker is successfully rebuilt '
                      'from original build rh-nodejs6-docker-6-14.11 to new '
                      'build rh-nodejs6-docker-6-14.1511360844.')
    expected_link = 'https://pipeline.engineering.redhat.com/freshmakerevent/58'
    expected_icon = '/umb/_static/img/icons/freshmaker.png'
    expected_packages = set([])

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1511940834.0,
        "msg_id": "ID:localhost-45704-1510236486219-2:66659:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.freshmaker.build.state.changed",
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "build_id": 13,
            "state_reason": "Built successfully.",
            "time_completed": "2017-11-29T07:07:49Z",
            "name": "rh-nodejs6-docker",
            "time_submitted": "2017-11-22T14:27:24Z",
            "event_id": 58,
            "original_nvr": "rh-nodejs6-docker-6-14.11",
            "type_name": "IMAGE",
            "state_name": "DONE",
            "url": "http://freshmaker.localhost/api/1/builds/32",
            "state": 1,
            "build_args": {
                "repository": "rpms/rh-nodejs6-docker",
                "parent": "s2i-base-docker-1-6.1511360843",
                "odcs_pulp_compose_id": 18,
                "branch": "rhscl-2.4-rh-nodejs6-rhel-7",
                "commit": "7173d2ef184d571a5dda71794217f3ceae27d270",
                "target": "rhscl-2.4-rh-nodejs6-rhel-7-docker-candidate"
            },
            "dep_on": "s2i-base-docker",
            "type": 1,
            "id": 32,
            "rebuilt_nvr": "rh-nodejs6-docker-6-14.1511360844"
        }
    }


class TestBuildStateIsNotDone(fedmsg.tests.test_meta.Base):

    expected_title = 'freshmaker.build.state.changed'
    expected_subti = ('IMAGE build state is switched to FAILED: '
                      '"Cannot build artifact, because its dependency '
                      'cannot be built."')
    expected_link = 'https://pipeline.engineering.redhat.com/freshmakerevent/60'
    expected_icon = '/umb/_static/img/icons/freshmaker.png'
    expected_packages = set([])

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1511940834.0,
        "msg_id": "ID:localhost-45704-1510236486219-2:66659:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.freshmaker.build.state.changed",
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "build_id": 62,
            "state_reason": "Cannot build artifact, because its "
            "dependency cannot be built.",
            "time_completed": "2017-11-29T11:05:49Z",
            "name": "rhmap-httpd-docker",
            "time_submitted": "2017-11-22T15:06:50Z",
            "event_id": 60,
            "original_nvr": "rhmap-httpd-docker-2.4-40",
            "type_name": "IMAGE",
            "state_name": "FAILED",
            "url": "http://freshmaker.localhost/api/1/builds/96",
            "state": 2,
            "build_args": {
                "repository": "rpms/rhmap-httpd-docker",
                "parent": "httpd24-docker-2.4-36.1511363210",
                "odcs_pulp_compose_id": 84,
                "branch": "rhmap-4.5-rhel-7",
                "commit": "3135dd5c0d1199ff6688f4d50c702a789fea5b09",
                "target": "rhmap-4.5-rhel-7-docker-candidate"
            },
            "dep_on": "httpd24-docker",
            "type": 1,
            "id": 96,
            "rebuilt_nvr": "rhmap-httpd-docker-2.4-40.1511363210"
        }
    }


class TestEventStateChanged(fedmsg.tests.test_meta.Base):

    expected_title = 'freshmaker.event.state.changed'
    expected_subti = ('Event state is switched to COMPLETE: "Generated '
                      'ErrataAdvisoryRPMsSignedEvent '
                      '(ID:messaging-devops-broker01.localhost-46295-'
                      '1510954431290-2:473881:0:0:1) '
                      'for errata: RHSA-2017:29110"')
    expected_link = 'https://pipeline.engineering.redhat.com/freshmakerevent/81'
    expected_icon = '/umb/_static/img/icons/freshmaker.png'
    expected_packages = set(['pkg', 'another-pkg'])

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1511940834.0,
        "msg_id": "ID:localhost-45704-1510236486219-2:66659:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.freshmaker.event.state.changed",
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "state_reason": ("Generated ErrataAdvisoryRPMsSignedEvent "
                             "(ID:messaging-devops-broker01.localhost-"
                             "46295-1510954431290-2:473881:0:0:1) "
                             "for errata: RHSA-2017:29110"),
            "builds": ['pkg-0.1-1', 'another-pkg-1.0-7'],
            "url": "http://freshmaker.localhost/api/1/events/81",
            "search_key": "ID:messaging-devops-broker01.localhost-"
            "46295-1510954431290-2:473881:0:0:1",
            "id": 81,
            "state": 2,
            "event_type_id": 11,
            "message_id": "ID:messaging-devops-broker01.localhost-"
            "46295-1510954431290-2:473881:0:0:1",
            "state_name": "COMPLETE"
        }
    }


class TestUnknownMessageComes(fedmsg.tests.test_meta.Base):

    expected_title = 'freshmaker.some.new.event'
    expected_subti = 'Unknown message.'
    expected_link = None
    expected_icon = '/umb/_static/img/icons/freshmaker.png'
    expected_packages = set([])

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1511940834.0,
        "msg_id": "ID:localhost-45704-1510236486219-2:66659:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.freshmaker.some.new.event",
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "state_reason": "No container images to rebuild for "
            "advisory u'RHSA-2017:31570'",
            "builds": [],
            "url": "http://freshmaker.localhost/api/1/events/83",
            "search_key": "31570",
            "id": 83,
            "state": 4,
            "event_type_id": 8,
            "message_id": "ID:messaging-devops-broker01.localhost-"
            "46295-1510954431290-2:474199:0:0:1.RHSA-2017:31570",
            "state_name": "SKIPPED"
        }
    }


class TestAllBuildsDone(fedmsg.tests.test_meta.Base):
    expected_title = 'freshmaker.event.state.changed'
    expected_subti = ('Event state is switched to COMPLETE: "All docker '
                      'images have been rebuilt."')
    expected_link = 'https://pipeline.engineering.redhat.com/freshmakerevent/242'
    expected_icon = '/umb/_static/img/icons/freshmaker.png'
    expected_packages = set(['someimage', 'someimage2'])
    msg = {
        "headers": {
            "JMS_AMQP_FirstAcquirer": "false",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "content-length": "1938",
            "destination": "/topic/VirtualTopic.eng.freshmaker."
            "event.state.changed",
            "expires": "0",
            "message-id": "ID:messaging-devops-broker01.localhost-"
            "45704-1510236486219-2:121170:0:0:1",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas"
            "-stage.VirtualTopic.eng.>",
            "timestamp": "0"},
        "i": 0,
        "msg": {
            "builds": [{
                "build_args": {
                    "branch": "somebranch",
                    "commit": "61c79adcc6db5f62cf62d358329042831b153f63",
                    "odcs_pulp_compose_id": 18,
                    "parent": "someimage3-docker-7.0.6-3",
                    "repository": "rpms/someimage4-docker",
                    "target": "somebranch-docker-candidate"
                },
                "build_id": None,
                "dep_on": None,
                "event_id": 242,
                "id": 122,
                "name": "someimage",
                "original_nvr": "someimage-1.4-36",
                "rebuilt_nvr": "someimage-1.4-36.1512495241",
                "state": 4,
                "state_name": "PLANNED",
                "state_reason": None,
                "time_completed": None,
                "time_submitted": "2017-12-05T17:34:01Z",
                "type": 1,
                "type_name": "IMAGE",
                "url": "http://freshmaker.localhost/api/1/builds/122"
            }, {
                "build_args": {
                    "branch": "somebranch2",
                    "commit": "07d6e35c241500a68fdaa02f208c6c098cc00835",
                    "odcs_pulp_compose_id": 19,
                    "parent": "someimage-1.4-36.1512495241",
                    "repository": "rpms/someimage2",
                    "target": "somebranch2-docker-candidate"
                },
                "build_id": None,
                "dep_on": "someimage",
                "event_id": 242,
                "id": 123,
                "name": "someimage2",
                "original_nvr": "someimage2-v3.7.9-21",
                "rebuilt_nvr": "someimage2-v3.7.9-21.1512495241",
                "state": 4,
                "state_name": "PLANNED",
                "state_reason": None,
                "time_completed": None,
                "time_submitted": "2017-12-05T17:34:01Z",
                "type": 1,
                "type_name": "IMAGE",
                "url": "http://freshmaker.localhost/api/1/builds/123"
            }],
            "event_type_id": 8,
            "id": 242,
            "message_id": "ID:messaging-devops-broker02.localhost-33824-"
            "1512422606448-2:64621:0:0:1.RHSA-2017:31059",
            "search_key": "31059",
            "state": 2,
            "state_name": "COMPLETE",
            "state_reason": "All docker images have been rebuilt.",
            "url": "http://freshmaker.localhost/api/1/events/242"
        },
        "msg_id": "ID:messaging-devops-broker01.localhost-45704-"
        "1510236486219-2:121170:0:0:1",
        "timestamp": 1512495243.0,
        "topic": "/topic/VirtualTopic.eng.freshmaker.event.state.changed",
        "username": None,
    }

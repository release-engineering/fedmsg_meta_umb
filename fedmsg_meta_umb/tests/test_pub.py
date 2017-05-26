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

class TestPubPushStop(fedmsg.tests.test_meta.Base):
    """ "Pub" is the system used to push Red Hat releases for distribution.

    Pub will publish a message to the message bus when pushes start and stop.
    This is an example of a stop message announced when a push **completes
    successfully**.
    """
    expected_title = 'pub.push_stop'
    expected_subti = ("errata's advisory push to code-stage of "
                      "RHBA-2017:28733 completed successfully")
    expected_link = "http://pub.devel.redhat.com/pub/push/121870/"
    expected_packages = set([])
    expected_usernames = set(['errata'])
    expected_agent = 'errata'
    # TODO - pub needs an icon to be cool...
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "username": None,
        "i": 0,
        "timestamp": 1495759713.0,
        "msg_id": "ID\\cmessaging-devops-broker02.web.prod.ext.phx2.redhat."
        "com-35060-1495137834512-7\\c198478\\c0\\c0\\c1",
        "topic": "/topic/VirtualTopic.eng.pub.push_stop",
        "headers": {
            "content-length": "422",
            "mtype": "push_stop",
            "JMS_AMQP_FirstAcquirer": "false",
            "push_id": "121870",
            "priority": "4",
            "service": "pub",
            "destination": "/topic/VirtualTopic.eng.pub.push_stop",
            "environment": "production",
            "source": "advisory",
            "state": "CLOSED",
            "pushed_item_count": "1",
            "timestamp": "0",
            "method": "PushAdvisory",
            "owner_id": "pub/pub.app.eng.bos.redhat.com",
            "JMS_AMQP_NATIVE": "false",
            "expires": "0",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "nochannel": "false",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "task_id": "121870",
            "target": "code-stage",
            "message-id": "ID\\cmessaging-devops-broker02.web.prod.ext.phx2."
            "redhat.com-35060-1495137834512-7\\c198478\\c0\\c0\\c1"
        },
        "msg": {
            "comment": "",
            "nochannel": False,
            "target": "code-stage",
            "task_id": 121870,
            "source": "advisory",
            "hostname": "pub.app.eng.bos.redhat.com",
            "push_url": "http://pub.devel.redhat.com/pub/push/121870/",
            "task_url": "http://pub.devel.redhat.com/pub/task/121870/",
            "owner": "errata",
            "state": "CLOSED",
            "pushed_by": None,
            "pushed_item_count": 1,
            "file_list": [
                "RHBA-2017:28733"
            ],
            "push_id": 121870,
            "method": "PushAdvisory"
        }
    }


class TestPubPushFail(fedmsg.tests.test_meta.Base):
    """ "Pub" is the system used to push Red Hat releases for distribution.

    Pub will publish a message to the message bus when pushes start and stop.
    This is an example of a stop message announced when a push **fails**.
    """
    expected_title = 'pub.push_stop'
    expected_subti = ("rhartman's advisory push to live of "
                      "RHBA-2017:1322, RHBA-2017:1323, and 9 others failed")
    expected_link = "http://pub.devel.redhat.com/pub/push/121923/"
    expected_packages = set([])
    expected_usernames = set(['rhartman', 'errata'])
    expected_agent = 'rhartman'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "username": None,
        "i": 0,
        "timestamp": 1495807290.0,
        "msg_id": "ID\\cmessaging-devops-broker02.web.prod.ext.phx2.redhat"
        ".com-35060-1495137834512-7\\c220960\\c0\\c0\\c1",
        "topic": "/topic/VirtualTopic.eng.pub.push_stop",
        "headers": {
            "content-length": "613",
            "mtype": "push_stop",
            "JMS_AMQP_FirstAcquirer": "false",
            "push_id": "121923",
            "priority": "4",
            "service": "pub",
            "destination": "/topic/VirtualTopic.eng.pub.push_stop",
            "environment": "production",
            "source": "advisory",
            "state": "FAILED",
            "pushed_item_count": "55",
            "timestamp": "0",
            "method": "PushAdvisory",
            "owner_id": "pub/pub.app.eng.bos.redhat.com",
            "JMS_AMQP_NATIVE": "false",
            "expires": "0",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "nochannel": "false",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "task_id": "121923",
            "target": "live",
            "message-id": "ID\\cmessaging-devops-broker02.web.prod.ext.phx2."
            "redhat.com-35060-1495137834512-7\\c220960\\c0\\c0\\c1"
        },
        "msg": {
            "comment": "",
            "nochannel": False,
            "target": "live",
            "task_id": 121923,
            "source": "advisory",
            "hostname": "pub.app.eng.bos.redhat.com",
            "push_url": "http://pub.devel.redhat.com/pub/push/121923/",
            "task_url": "http://pub.devel.redhat.com/pub/task/121923/",
            "owner": "errata",
            "state": "FAILED",
            "pushed_by": "rhartman@redhat.com",
            "pushed_item_count": 55,
            "file_list": [
                "RHEA-2017:1321",
                "RHBA-2017:1322",
                "RHBA-2017:1323",
                "RHBA-2017:1324",
                "RHBA-2017:1325",
                "RHEA-2017:1326",
                "RHBA-2017:1327",
                "RHEA-2017:1328",
                "RHEA-2017:1329",
                "RHBA-2017:1330",
                "RHBA-2017:1331"
            ],
            "push_id": 121923,
            "method": "PushAdvisory"
        }
    }


class TestPubPushStart(fedmsg.tests.test_meta.Base):
    """ "Pub" is the system used to push Red Hat releases for distribution.

    Pub will publish a message to the message bus when pushes start and stop.
    This is an example of a stop message announced when a push starts.
    """
    expected_title = 'pub.push_start'
    expected_subti = ("lismith's staged push to cdn-qa of "
                      "rhel-x86_64-server-optional-7.1.eus just started")
    expected_link = "http://pub.devel.redhat.com/pub/push/121932/"
    expected_packages = set([])
    expected_usernames = set(['lismith'])
    expected_agent = 'lismith'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "username": None,
        "i": 0,
        "timestamp": 1495813073.0,
        "msg_id": "ID\\cmessaging-devops-broker02.web.prod.ext.phx2.redhat."
        "com-35060-1495137834512-7\\c226859\\c0\\c0\\c1",
        "topic": "/topic/VirtualTopic.eng.pub.push_start",
        "headers": {
            "content-length": "520",
            "mtype": "push_start",
            "JMS_AMQP_FirstAcquirer": "false",
            "push_id": "121932",
            "priority": "4",
            "service": "pub",
            "destination": "/topic/VirtualTopic.eng.pub.push_start",
            "environment": "production",
            "source": "staged",
            "state": "OPEN",
            "pushed_item_count": "0",
            "timestamp": "0",
            "method": "PushStaged",
            "owner_id": "pub/pub.app.eng.bos.redhat.com",
            "JMS_AMQP_NATIVE": "false",
            "expires": "0",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "nochannel": "false",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "task_id": "121932",
            "target": "cdn-qa",
            "message-id": "ID\\cmessaging-devops-broker02.web.prod.ext.phx2."
            "redhat.com-35060-1495137834512-7\\c226859\\c0\\c0\\c1"
        },
        "msg": {
            "comment": "Push missing SRPMs (RCMWORK-1400)",
            "nochannel": False,
            "target": "cdn-qa",
            "task_id": 121932,
            "source": "staged",
            "hostname": "pub.app.eng.bos.redhat.com",
            "push_url": "http://pub.devel.redhat.com/pub/push/121932/",
            "task_url": "http://pub.devel.redhat.com/pub/task/121932/",
            "owner": "lismith",
            "state": "OPEN",
            "pushed_by": "lismith@redhat.com",
            "pushed_item_count": 0,
            "file_list": [
                "/mnt/redhat/devel/lismith/staging-dir/rhel-x86_64-server-optional-7.1.eus"
            ],
            "push_id": 121932,
            "method": "PushStaged"
        }
    }

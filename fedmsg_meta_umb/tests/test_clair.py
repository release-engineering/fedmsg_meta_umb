# Copyright (C) 2019 Red Hat, Inc.
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
from .common import add_doc


class TestClairNotification(fedmsg.tests.test_meta.Base):
    """
    Messages (like the example given here) are published when Clair gets
    new security vulnerability
    """

    expected_title = 'clair.notification'
    expected_subti = 'New notification 0c1346ff-a64b-4504-a673-ea95930eacf1'
    expected_link = (
        'http://clair-clair-prod.cloud.paas.psi.redhat.com/'
        'notifications/0c1346ff-a64b-4504-a673-ea95930eacf1?limit=10'
    )
    expected_icon = '_static/img/icons/clair.png'

    msg = {
        "i": 0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-35238-1560306230293-3:382125:-1:1:122",
        "topic": "/topic/VirtualTopic.eng.clair.notification",
        "timestamp": 1561017066.0,
        "certificate": None,
        "signature": None,
        "username": None,
        "crypto": None,
        "msg": {"Notification": {"Name": "0c1346ff-a64b-4504-a673-ea95930eacf1"}},
        "headers": {
            "JMSXUserID": "msg-clair",
            "amq6100_destination": "queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "amq6100_originalDestination": "topic://VirtualTopic.eng.clair.notification",
            "content-type": "application/json",
            "correlation-id": "2ccad28b-0a6e-43d9-9376-ee238276fcbf",
            "destination": "/topic/VirtualTopic.eng.clair.notification",
            "expires": "1561103466372",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-' \
                '35238-1560306230293-3:382125:-1:1:122",
            "original-destination": "/topic/VirtualTopic.eng.clair.notification",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "timestamp": "1561017066372",
        },
        "source_name": "datanommer",
        "source_version": "0.9.1",
    }


class TestClairNotificationSplit(fedmsg.tests.test_meta.Base):
    """
    Messages (like the example given here) are published when Clair wrapper
    split notification with new security vulnerability
    """

    expected_title = 'clair.notification'
    expected_subti = 'New notification batch CVE-1234 - RHSA-2019:1234 with 5 image(s)'
    expected_link = (
        'http://clair-clair-prod.cloud.paas.psi.redhat.com/'
        'notifications/0c1346ff-a64b-4504-a673-ea95930eacf1?limit=10'
    )
    expected_icon = '_static/img/icons/clair.png'
    expected_usernames = set([])

    msg = {
        "i": 0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-35238-1560306230293-3:382125:-1:1:122",
        "topic": "/topic/VirtualTopic.eng.clair.notification",
        "timestamp": 1561017066.0,
        "certificate": None,
        "signature": None,
        "username": None,
        "crypto": None,
        "msg": {
            "Notification": {"Name": "0c1346ff-a64b-4504-a673-ea95930eacf1"},
            'affected_images': ['image1', 'image2', 'image3', 'image4', 'image5'],
            'vulnerability_name': 'CVE-1234 - RHSA-2019:1234',
        },
        "headers": {
            "JMSXUserID": "msg-clair",
            "amq6100_destination": "queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "amq6100_originalDestination": "topic://VirtualTopic.eng.clair.notification",
            "content-type": "application/json",
            "correlation-id": "2ccad28b-0a6e-43d9-9376-ee238276fcbf",
            "destination": "/topic/VirtualTopic.eng.clair.notification",
            "expires": "1561103466372",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-' \
                '35238-1560306230293-3:382125:-1:1:122",
            "original-destination": "/topic/VirtualTopic.eng.clair.notification",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "timestamp": "1561017066372",
        },
        "source_name": "datanommer",
        "source_version": "0.9.1",
    }


class TestClairWrapperScan(fedmsg.tests.test_meta.Base):
    """
    Messages (like the example given here) are published when Clair + Wrapper
    scan and grade new container image
    """

    expected_title = 'clair.scan'
    expected_subti = 'New image scanned: openstack-nova-compute-container-14.0-110.1561066899.ppc64le (A)'
    expected_link = (
        'http://clair-clair-prod.cloud.paas.psi.redhat.com/'
        'ancestry/openstack-nova-compute-container-14.0-110.1561066899.ppc64le'
    )
    expected_packages = set(['openstack-nova-compute-container'])
    expected_objects = set([])
    expected_icon = '_static/img/icons/clair.png'

    msg = {
        "i": 0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-35238-1560306230293-6:866563:0:0:1",
        "topic": "/topic/VirtualTopic.eng.clair.scan",
        "timestamp": 1561114556.0,
        "certificate": None,
        "signature": None,
        "username": None,
        "crypto": None,
        "msg": {
            "arch": "ppc64le",
            "grades": [{"grade": "A", "start_date": "20190621T06:55:00.000-0400"}],
            "nvr": "openstack-nova-compute-container-14.0-110.1561066899",
        },
        "headers": {
            "JMSXUserID": "msg-clair",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "amq6100_destination": "queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "amq6100_originalDestination": "topic://VirtualTopic.eng.clair.scan",
            "arch": "ppc64le",
            "content-length": "154",
            "correlation-id": "2ec19d5b-8820-4a9e-b8aa-ea3a11523057",
            "destination": "/topic/VirtualTopic.eng.clair.scan",
            "expires": "0",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.' \
                'com-35238-1560306230293-6:866563:0:0:1",
            "nvr": "openstack-nova-compute-container-14.0-110.1561066899",
            "original-destination": "/topic/VirtualTopic.eng.clair.scan",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "timestamp": "0",
        },
        "source_name": "datanommer",
        "source_version": "0.9.1",
    }


class TestClairWrapperScanISV(fedmsg.tests.test_meta.Base):
    """
    Messages (like the example given here) are published when Clair + Wrapper
    scan and grade new ISV container image
    """

    expected_title = 'clair.scan.isv'
    expected_subti = 'New image scanned: sha256:d994ce5745cd63d727d21a0c93d0811942d4e4d054d7704e7240b8e4471edf5f (B)'
    expected_link = (
        'http://clair-clair-prod.cloud.paas.psi.redhat.com/'
        'ancestry/sha256-d994ce5745cd63d727d21a0c93d0811942d4e4d054d7704e7240b8e4471edf5f'
    )
    expected_icon = '_static/img/icons/clair.png'

    msg = {
        "i": 0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-35238-1560306230293-6:867825:0:0:1",
        "topic": "/topic/VirtualTopic.eng.clair.scan.isv",
        "timestamp": 1561116055.0,
        "certificate": None,
        "signature": None,
        "username": None,
        "crypto": None,
        "msg": {
            "grades": [
                {
                    "end_date": "20190720T15:51:00.000-0400",
                    "grade": "B",
                    "start_date": "20190621T07:20:00.000-0400",
                },
                {
                    "end_date": "20190918T15:51:00.000-0400",
                    "grade": "C",
                    "start_date": "20190720T15:51:00.000-0400",
                },
                {
                    "end_date": "20200619T15:51:00.000-0400",
                    "grade": "D",
                    "start_date": "20190918T15:51:00.000-0400",
                },
                {"grade": "F", "start_date": "20200619T15:51:00.000-0400"},
            ],
            "image_id": "sha256:d994ce5745cd63d727d21a0c93d0811942d4e4d054d7704e7240b8e4471edf5f",
        },
        "headers": {
            "JMSXUserID": "msg-clair",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "amq6100_destination": "queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "amq6100_originalDestination": "topic://VirtualTopic.eng.clair.scan.isv",
            "content-length": "465",
            "correlation-id": "375c97f7-d03f-4f4b-87d5-ce82bb4b4712",
            "destination": "/topic/VirtualTopic.eng.clair.scan.isv",
            "expires": "0",
            "image_id": "sha256:d994ce5745cd63d727d21a0c93d0811942d4e4d054d7704e7240b8e4471edf5f",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-35238-' \
                '1560306230293-6:867825:0:0:1",
            "original-destination": "/topic/VirtualTopic.eng.clair.scan.isv",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "timestamp": "0",
        },
        "source_name": "datanommer",
        "source_version": "0.9.1",
    }


class TestCommandNVR(fedmsg.tests.test_meta.Base):
    """
    Messages (like the example given here) are published when user manually
    request scan of Red Hat image
    """

    expected_title = 'clair.command'
    expected_subti = 'Scan request: rhmap-fh-metrics-docker-2.0.0-1.amd64'
    expected_link = (
        'https://brewweb.engineering.redhat.com/brew/search?'
        'terms=rhmap-fh-metrics-docker-2.0.0-1&type=build&match=glob'
    )
    expected_packages = set(['rhmap-fh-metrics-docker'])
    expected_icon = '_static/img/icons/clair.png'
    expected_usernames = {'araszka'}

    msg = {
        "i": 0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-35238-1560306230293-6:1568663:0:0:1",
        "topic": "/topic/VirtualTopic.eng.clair.command",
        "timestamp": 1561927509.0,
        "certificate": None,
        "signature": None,
        "username": None,
        "crypto": None,
        "msg": {
            "architecture": "amd64",
            "brew_build": "rhmap-fh-metrics-docker-2.0.0-1",
            "user": "araszka",
        },
        "headers": {
            "JMSXUserID": "msg-clair",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "amq6100_destination": "queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "amq6100_originalDestination": "topic://VirtualTopic.eng.clair.command",
            "architecture": "amd64",
            "brew_build": "rhmap-fh-metrics-docker-2.0.0-1",
            "content-length": "93",
            "correlation-id": "19f27f03-68ae-480e-8aaa-220491678de0",
            "destination": "/topic/VirtualTopic.eng.clair.command",
            "expires": "0",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-"
            "35238-1560306230293-6:1568663:0:0:1",
            "original-destination": "/topic/VirtualTopic.eng.clair.command",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "timestamp": "0",
            "user": "araszka",
        },
        "source_name": "datanommer",
        "source_version": "0.9.1",
    }


class TestCommandISV(fedmsg.tests.test_meta.Base):
    """
    Messages (like the example given here) are published when user manually
    request scan of ISV image
    """

    expected_title = 'clair.command'
    expected_subti = 'Scan request: sha256:0b8363dcca5b19788e84c7642a8a272a7fa1736b0db05614a6cf38e8f3bcf3d4'
    expected_link = None
    expected_icon = '_static/img/icons/clair.png'
    expected_usernames = {'araszka'}

    msg = {
        "i": 0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-35238-1560306230293-6:1765358:0:0:1",
        "topic": "/topic/VirtualTopic.eng.clair.command",
        "timestamp": 1562157865.0,
        "certificate": None,
        "signature": None,
        "username": None,
        "crypto": None,
        "msg": {
            "containerProcessStatus": "SCAN_COMPLETE_CERTIFIED_PASS",
            "imageDigest": "sha256:0b8363dcca5b19788e84c7642a8a272a7fa1736b0db05614a6cf38e8f3bcf3d4",
            "user": "araszka",
        },
        "headers": {
            "JMSXUserID": "msg-clair",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "amq6100_destination": "queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "amq6100_originalDestination": "topic://VirtualTopic.eng.clair.command",
            "containerProcessStatus": "SCAN_COMPLETE_CERTIFIED_PASS",
            "content-length": "167",
            "correlation-id": "13a85146-45cb-48a9-97c0-7a92d5072b8f",
            "destination": "/topic/VirtualTopic.eng.clair.command",
            "expires": "0",
            "imageDigest": "sha256:0b8363dcca5b19788e84c7642a8a272a7fa1736b0db05614a6cf38e8f3bcf3d4",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2."
            "redhat.com-35238-1560306230293-6:1765358:0:0:1",
            "original-destination": "/topic/VirtualTopic.eng.clair.command",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "timestamp": "0",
            "user": "araszka",
        },
        "source_name": "datanommer",
        "source_version": "0.9.1",
    }


class TestClairUnknowFormat(fedmsg.tests.test_meta.Base):
    """
    Unknown format of message
    """

    expected_icon = '_static/img/icons/clair.png'
    expected_subti = 'Unknown message format'

    msg = {
        "i": 0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-35238-1560306230293-3:382125:-1:1:122",
        "topic": "/topic/VirtualTopic.eng.clair.notification",
        "timestamp": 1561017066.0,
        "certificate": None,
        "signature": None,
        "username": None,
        "crypto": None,
        "msg": 'string-msg',
        "headers": {
            "JMSXUserID": "msg-clair",
            "amq6100_destination": "queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "amq6100_originalDestination": "topic://VirtualTopic.eng.clair.notification",
            "content-type": "application/json",
            "correlation-id": "2ccad28b-0a6e-43d9-9376-ee238276fcbf",
            "destination": "/topic/VirtualTopic.eng.clair.notification",
            "expires": "1561103466372",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-' \
                '35238-1560306230293-3:382125:-1:1:122",
            "original-destination": "/topic/VirtualTopic.eng.clair.notification",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "timestamp": "1561017066372",
        },
        "source_name": "datanommer",
        "source_version": "0.9.1",
    }


add_doc(locals())

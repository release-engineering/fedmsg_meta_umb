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

    expected_title = "clair.v4.notification"
    expected_subti = "New notification - added: 2, removed: 1 vulnerabilities"
    expected_icon = "_static/img/icons/clair.png"

    msg = {
        "i": 0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-35238-1560306230293-3:382125:-1:1:122",
        "topic": "/topic/VirtualTopic.eng.clair.v4.notification",
        "timestamp": 1561017066.0,
        "certificate": None,
        "signature": None,
        "username": None,
        "crypto": None,
        "msg": [
            {
                "id": "001680dd-bf80-49d0-842d-255c06d0d2df",
                "manifest": "sha256:6066f95b13ae8b2c210c60c215ac93401e297f45e59b755ac14d2262157d9fea",
                "reason": "added",
                "vulnerability": {
                    "distribution": {
                        "arch": "",
                        "cpe": "cpe:2.3:o:redhat:enterprise_linux:8:*:*:*:*:*:*:*",
                        "did": "rhel",
                        "id": "",
                        "name": "Red Hat Enterprise Linux Server",
                        "pretty_name": "Red Hat Enterprise Linux Server 8",
                        "version": "8",
                        "version_code_name": "",
                        "version_id": "8",
                    },
                    "fixed_in_version": "0:6.0.0-25.5.module+el8.2.1+8680+ea98947b",
                    "links": "https://access.redhat.com/errata/RHSA-2020:5111",
                    "name": "RHSA-2020:5111: virt:8.2 and virt-devel:8.2 security and bug fix update (Moderate)",
                    "package": {
                        "arch": "aarch64|ppc64le|s390x|x86_64",
                        "cpe": "",
                        "id": "",
                        "kind": "binary",
                        "module": "virt:8.2",
                        "name": "libvirt-daemon",
                        "normalized_version": "",
                        "version": "",
                    },
                    "repo": {
                        "cpe": "",
                        "key": "rhel-cpe-repository",
                        "name": "cpe:/a:redhat:advanced_virtualization:8.2::el8",
                    },
                    "severity": "Medium",
                },
            },
            {
                "id": "009e3b28-ac0f-4bbc-8604-0f0d4ade08a4",
                "manifest": "sha256:30ea340057e23e6be8d6012453e709879ce29a23d9e5482164826ba4aa6ffe2b",
                "reason": "added",
                "vulnerability": {
                    "distribution": {
                        "arch": "",
                        "cpe": "cpe:2.3:o:redhat:enterprise_linux:8:*:*:*:*:*:*:*",
                        "did": "rhel",
                        "id": "",
                        "name": "Red Hat Enterprise Linux Server",
                        "pretty_name": "Red Hat Enterprise Linux Server 8",
                        "version": "8",
                        "version_code_name": "",
                        "version_id": "8",
                    },
                    "fixed_in_version": "0:6.0.0-25.5.module+el8.2.1+8680+ea98947b",
                    "links": "https://access.redhat.com/errata/RHSA-2020:5111",
                    "name": "RHSA-2020:5111: virt:8.2 and virt-devel:8.2 security and bug fix update (Moderate)",
                    "package": {
                        "arch": "aarch64|ppc64le|s390x|x86_64",
                        "cpe": "",
                        "id": "",
                        "kind": "binary",
                        "module": "virt:8.2",
                        "name": "libvirt-daemon",
                        "normalized_version": "",
                        "version": "",
                    },
                    "repo": {
                        "cpe": "",
                        "key": "rhel-cpe-repository",
                        "name": "cpe:/a:redhat:advanced_virtualization:8.2::el8",
                    },
                    "severity": "Medium",
                },
            },
            {
                "id": "00ae7a5b-bd08-468a-b3c6-dc95c249a435",
                "manifest": "sha256:05c7ad6e08d7f2203b5c35cfeabd7fd423959f5cfcdefc32d07b5a1e6e0581dc",
                "reason": "removed",
                "vulnerability": {
                    "distribution": {
                        "arch": "",
                        "cpe": "cpe:2.3:o:redhat:enterprise_linux:8:*:*:*:*:*:*:*",
                        "did": "rhel",
                        "id": "",
                        "name": "Red Hat Enterprise Linux Server",
                        "pretty_name": "Red Hat Enterprise Linux Server 8",
                        "version": "8",
                        "version_code_name": "",
                        "version_id": "8",
                    },
                    "fixed_in_version": "0:6.0.0-25.5.module+el8.2.1+8680+ea98947b",
                    "links": "https://access.redhat.com/errata/RHSA-2020:5111",
                    "name": "RHSA-2020:5111: virt:8.2 and virt-devel:8.2 security and bug fix update (Moderate)",
                    "package": {
                        "arch": "aarch64|ppc64le|s390x|x86_64",
                        "cpe": "",
                        "id": "",
                        "kind": "binary",
                        "module": "virt:8.2",
                        "name": "libvirt-daemon",
                        "normalized_version": "",
                        "version": "",
                    },
                    "repo": {
                        "cpe": "",
                        "key": "rhel-cpe-repository",
                        "name": "cpe:/a:redhat:advanced_virtualization:8.2::el8",
                    },
                    "severity": "Medium",
                },
            },
        ],
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


class TestClairWrapperScanNVR(fedmsg.tests.test_meta.Base):
    """
    Messages (like the example given here) are published when Clair + Wrapper
    scan and grade new container image
    """

    expected_title = "clair.scan"
    expected_subti = "New image scanned: openstack-nova-compute-container-14.0-110.1561066899.ppc64le (A)"
    expected_link = (
        "https://clair.engineering.redhat.com/"
        "matcher/api/v1/vulnerability_report/sha256:d994ce5745cd63d727d21a0c93d0811942d4e4d054d7704e7240b8e4471edf5f"
    )
    expected_packages = set(["openstack-nova-compute-container"])
    expected_objects = set([])
    expected_icon = "_static/img/icons/clair.png"

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
            "image_id": "sha256:d994ce5745cd63d727d21a0c93d0811942d4e4d054d7704e7240b8e4471edf5f",
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


class TestClairWrapperScanNVRA(fedmsg.tests.test_meta.Base):
    """
    Messages (like the example given here) are published when Clair + Wrapper
    scan and grade new container image
    """

    expected_title = "clair.scan"
    expected_subti = "New image scanned: openstack-nova-compute-container-14.0-110.1561066899.ppc64le (A)"
    expected_link = (
        "https://clair.engineering.redhat.com/"
        "matcher/api/v1/vulnerability_report/sha256:d994ce5745cd63d727d21a0c93d0811942d4e4d054d7704e7240b8e4471edf5f"
    )
    expected_packages = set(["openstack-nova-compute-container"])
    expected_objects = set([])
    expected_icon = "_static/img/icons/clair.png"

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
            "grades": [{"grade": "A", "start_date": "20190621T06:55:00.000-0400"}],
            "nvra": "openstack-nova-compute-container-14.0-110.1561066899.ppc64le",
            "image_id": "sha256:d994ce5745cd63d727d21a0c93d0811942d4e4d054d7704e7240b8e4471edf5f",
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

    expected_title = "clair.scan.isv"
    expected_subti = "New image scanned: sha256:d994ce5745cd63d727d21a0c93d0811942d4e4d054d7704e7240b8e4471edf5f (B)"
    expected_link = (
        "https://clair.engineering.redhat.com/"
        "matcher/api/v1/vulnerability_report/sha256:d994ce5745cd63d727d21a0c93d0811942d4e4d054d7704e7240b8e4471edf5f"
    )
    expected_icon = "_static/img/icons/clair.png"

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

    expected_title = "clair.command"
    expected_subti = "Scan request: rhmap-fh-metrics-docker-2.0.0-1.amd64"
    expected_link = (
        "https://brewweb.engineering.redhat.com/brew/search?"
        "terms=rhmap-fh-metrics-docker-2.0.0-1&type=build&match=glob"
    )
    expected_packages = set(["rhmap-fh-metrics-docker"])
    expected_icon = "_static/img/icons/clair.png"
    expected_usernames = {"araszka"}

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

    expected_title = "clair.command"
    expected_subti = "Scan request: sha256:0b8363dcca5b19788e84c7642a8a272a7fa1736b0db05614a6cf38e8f3bcf3d4"
    expected_link = None
    expected_icon = "_static/img/icons/clair.png"
    expected_usernames = {"araszka"}

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

    expected_icon = "_static/img/icons/clair.png"
    expected_subti = "Unknown message format"

    msg = {
        "i": 0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-35238-1560306230293-3:382125:-1:1:122",
        "topic": "/topic/VirtualTopic.eng.clair.notification",
        "timestamp": 1561017066.0,
        "certificate": None,
        "signature": None,
        "username": None,
        "crypto": None,
        "msg": "string-msg",
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

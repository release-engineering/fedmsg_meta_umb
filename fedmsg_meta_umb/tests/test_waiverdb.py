# Copyright (C) 2018 Red Hat, Inc.
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

import fedmsg.tests.test_meta
from .common import add_doc


class TestWaiverDBNewWaiver(fedmsg.tests.test_meta.Base):
    """ WaiverDB is a database for test waivers.

    This message gets published whenever a new waiver is created.
    """
    expected_title = 'waiverdb.waiver.new'
    expected_subti = 'lvrabec waived baseos-ci.brew-build.tier1.functional on selinux-policy-3.14.1-48.el8 (rhel-8)'
    expected_link = 'https://waiverdb.engineering.redhat.com/api/v1.0/waivers/36'
    expected_agent = 'lvrabec'
    expected_usernames = set(['lvrabec'])
    expected_packages = set(['selinux-policy'])
    expected_icon = '/umb/_static/img/icons/waiverdb.png'

    msg = {
        "i": 0,
        "timestamp": 1543418079.0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-39733-1543394753117-2:2457:-1:1:1",
        "topic": "/topic/VirtualTopic.eng.waiverdb.waiver.new",
        "headers": {
            "content-length": "451",
            "expires": "1544022879589",
            "timestamp": "1543418079589",
            "destination": "/topic/VirtualTopic.eng.waiverdb.waiver.new",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-39733-1543394753117-2:2457:-1:1:1",
            "subscription": "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>"
        },
        "msg": {
            "comment": "SELinux policy BaseOSCI tests(extended socket class tests) are broken not the build",
            "username": "lvrabec",
            "subject_type": "koji_build",
            "waived": True,
            "timestamp": "2018-11-28T15:14:39.056328",
            "product_version": "rhel-8",
            "testcase": "baseos-ci.brew-build.tier1.functional",
            "subject_identifier": "selinux-policy-3.14.1-48.el8",
            "proxied_by": None,
            "id": 36,
            "subject": {
                "item": "selinux-policy-3.14.1-48.el8",
                "type": "koji_build"
            }
        }
    }


class TestWaiverDBUnwaive(fedmsg.tests.test_meta.Base):
    """ WaiverDB is a database for test waivers.

    This message gets published whenever a test is "unwaived".
    """
    expected_title = 'waiverdb.waiver.new'
    expected_subti = 'mminar unwaived osci.brew-build.installability.functional on ' \
        'rh-amazon-rhui-client-3.0.9-1.el8 (rhel-8)'
    expected_link = 'https://waiverdb.engineering.redhat.com/api/v1.0/waivers/32'
    expected_agent = 'mminar'
    expected_usernames = set(['mminar'])
    expected_packages = set(['rh-amazon-rhui-client'])
    expected_icon = '/umb/_static/img/icons/waiverdb.png'

    msg = {
        "i": 0,
        "timestamp": 1543412594.0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-39733-1543394753117-2:1774:-1:1:1",
        "topic": "/topic/VirtualTopic.eng.waiverdb.waiver.new",
        "headers": {
            "content-length": "390",
            "expires": "1544017394359",
            "timestamp": "1543412594359",
            "destination": "/topic/VirtualTopic.eng.waiverdb.waiver.new",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-39733-1543394753117-2:1774:-1:1:1",
            "subscription": "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>"
        },
        "msg": {
            "comment": "Expected.",
            "username": "mminar",
            "subject_type": "koji_build",
            "waived": False,
            "timestamp": "2018-11-28T13:43:13.895190",
            "product_version": "rhel-8",
            "testcase": "osci.brew-build.installability.functional",
            "subject_identifier": "rh-amazon-rhui-client-3.0.9-1.el8",
            "proxied_by": None,
            "id": 32,
            "subject": {
                "item": "rh-amazon-rhui-client-3.0.9-1.el8",
                "type": "koji_build"
            }
        }
    }


add_doc(locals())

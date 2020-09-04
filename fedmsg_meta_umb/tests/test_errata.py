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
from .common import add_doc

class TestErrataStatusChange(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    Messages are published when an advisory **changes state**.  This is an
    example of an advisory moving from the QE state back to the NEW_FILES state
    (for modification by developers).
    """
    expected_title = 'errata.activity.status'
    expected_subti = ('fmuellne moved RHBA-2017:27087-02 from QE to NEW_FILES')
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/27087'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set(['fmuellne'])
    expected_agent = 'fmuellne'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')

    msg = {
        "username": None,
        "i": 0,
        "timestamp": 1496252132.0,
        "msg_id": "ID\\cmessaging-devops-broker01.web.prod.ext.phx2.redhat."
        "com-32888-1493960489068-4\\c472412\\c0\\c0\\c1",
        "topic": "/topic/VirtualTopic.eng.errata.activity.status",
        "headers": {
            "errata_status": "NEW_FILES",
            "expires": "0",
            "errata_id": "27087",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "to": "NEW_FILES",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.activity.status",
            "when": "2017-05-31 17:35:24 UTC",
            "persistent": "true",
            "who": "fmuellne@redhat.com",
            "priority": "4",
            "synopsis": "mutter/shell/extensions bug fix and enhancement update",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": "ID\\cmessaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-32888-1493960489068-4\\c472412\\c0\\c0\\c1",
            "fulladvisory": "RHBA-2017:27087-02",
            "timestamp": "0",
            "from": "QE",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "errata.activity.status",
            "subject": "errata.activity.status"
        },
        "msg": ""
    }


class TestErrataActivityCreated(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    Messages like this one are published when an advisory is **created**.
    """
    expected_title = 'errata.activity.created'
    expected_subti = ('bkearney filed a new RHBA advisory for '
                      'Sat-Tools-6.2-ASYNC')
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/28816'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set(['bkearney'])
    expected_agent = 'bkearney'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "username": None,
        "i": 0,
        "timestamp": 1496273395.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-32888-1493960489068-4:480845:0:0:1",
        "topic": "/topic/VirtualTopic.eng.errata.activity.created",
        "headers": {
            "expires": "0",
            "errata_id": "28816",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.activity.created",
            "when": "2017-05-31 23:29:54 UTC",
            "persistent": "true",
            "who": "bkearney@redhat.com",
            "priority": "4",
            "synopsis": "Satellite Tools 6.2.10 Async Bug Release",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-32888-1493960489068-4:480845:0:0:1",
            "timestamp": "0",
            "release": "Sat-Tools-6.2-ASYNC",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "RHBA",
            "subject": "errata.activity.created"
        },
        "source_version": "0.7.0",
        "msg": ""
    }


class TestErrataSecurityRequested(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    Messages like this one are published when someone *requests security approval*.
    """
    expected_title = 'errata.activity.security_approved'
    expected_subti = ('rbean requested security approval on '
                      'RHSA-2016:10000-01')
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/10000'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set(['rbean'])
    expected_agent = 'rbean'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1496275955.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat."
        "com-32888-1493960489068-4:481029:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.errata.activity.security_approved",
        "headers": {
            "errata_status": "QE",
            "expires": "0",
            "errata_id": "10000",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "to": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.activity.security_approved",
            "when": "2016-01-01 00:00:01 UTC",
            "persistent": "true",
            "who": "rbean@redhat.com",
            "priority": "4",
            "synopsis": "A mocked security update.  Not a real example.",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-32888-1493960489068-4:481029:0:0:1",
            "fulladvisory": "RHSA-2016:10000-01",
            "timestamp": "0",
            "from": "null",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "errata.activity.security_approved",
            "subject": "errata.activity.security_approved"
        },
        "signature": None,
        "source_version": "0.7.0",
        "msg": ""
    }


class TestErrataSignaturesReported(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    The Errata Tool pumps out messages like this one when cryptographic
    signatures are attached to builds (which are in turn attached to
    advisories).
    """
    expected_title = 'errata.activity.signing'
    expected_subti = ('robosignatory reported signing gssproxy-0.7.0-4.el7 for '
                      'RHBA-2017:26924-01')
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/26924'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set(['robosignatory'])
    expected_agent = 'robosignatory'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "i": 0,
        "timestamp": 1496271000.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
        "redhat.com-32888-1493960489068-4:479960:0:0:1",
        "topic": "/topic/VirtualTopic.eng.errata.activity.signing",
        "headers": {
            "errata_status": "QE",
            "expires": "0",
            "errata_id": "26924",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "to": "gssproxy-0.7.0-4.el7",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.activity.signing",
            "when": "2017-05-31 22:50:02 UTC",
            "persistent": "true",
            "who": "robosignatory/robosignatory.host.prod.eng.bos.redhat.com@REDHAT.COM",
            "priority": "4",
            "synopsis": "gssproxy bug fix and enhancement update",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-32888-1493960489068-4:479960:0:0:1",
            "fulladvisory": "RHBA-2017:26924-01",
            "timestamp": "0",
            "from": "null",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "errata.activity.signing",
            "subject": "errata.activity.signing"
        },
        "msg": ""
    }


class TestErrataBugsChanged(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    You'll see a message like this one when someone **changes bugs** on an
    advisory.
    """
    expected_title = 'errata.bugs.changed'
    expected_subti = ('rharwood changed bugs on an advisory')
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/26924'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set(['rharwood'])
    expected_agent = 'rharwood'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "i": 0,
        "timestamp": 1496269224.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
        "redhat.com-32888-1493960489068-4:478932:0:0:1",
        "topic": "/topic/VirtualTopic.eng.errata.bugs.changed",
        "headers": {
            "expires": "0",
            "errata_id": "26924",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.bugs.changed",
            "when": "2017-05-31 22:20:21 UTC",
            "persistent": "true",
            "who": "rharwood@redhat.com",
            "priority": "4",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-32888-1493960489068-4:478932:0:0:1",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "errata.bugs.changed",
            "subject": "errata.bugs.changed"
        },
        "msg": ""
    }


class TestErrataBuildsChanged(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    You'll see a message like this one when someone **changes the builds** on
    an advisory.
    """
    expected_title = 'errata.builds.changed'
    expected_subti = ('rharwood changed builds on an advisory')
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/26924'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set(['rharwood'])
    expected_agent = 'rharwood'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "i": 0,
        "timestamp": 1496269189.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
        "redhat.com-32888-1493960489068-4:478922:0:0:1",
        "topic": "/topic/VirtualTopic.eng.errata.builds.changed",
        "headers": {
            "expires": "0",
            "errata_id": "26924",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.builds.changed",
            "when": "2017-05-31 22:19:49 UTC",
            "persistent": "true",
            "who": "rharwood@redhat.com",
            "priority": "4",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-32888-1493960489068-4:478922:0:0:1",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "errata.builds.changed",
            "subject": "errata.builds.changed"
        },
        "msg": ""
    }


class TestErrataBatchChanged(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    You'll see a message like this one when someone **changes the batch**
    associated with an advisory.
    """
    expected_title = 'errata.activity.batch'
    expected_subti = ('lfriedma added RHEA-2017:28445-03 '
                      'to the RHEL-7.3.6-Containers advisory batch')
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/28445'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set(['lfriedma'])
    expected_agent = 'lfriedma'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "i": 0,
        "timestamp": 1496268967.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
        "redhat.com-32888-1493960489068-4:478875:0:0:1",
        "topic": "/topic/VirtualTopic.eng.errata.activity.batch",
        "headers": {
            "errata_status": "QE",
            "expires": "0",
            "errata_id": "28445",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "to": "RHEL-7.3.6-Containers",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.activity.batch",
            "when": "2017-05-31 22:16:04 UTC",
            "persistent": "true",
            "who": "lfriedma@redhat.com",
            "priority": "4",
            "synopsis": "New Red Hat Enterprise Linux Atomic Container Engine Container Image",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-32888-1493960489068-4:478875:0:0:1",
            "fulladvisory": "RHEA-2017:28445-03",
            "timestamp": "0",
            "from": "null",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "errata.activity.batch",
            "subject": "errata.activity.batch"
        },
        "msg": ""
    }


class TestErrataDocsApproved(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    Messages like these appear whenever someone **approves the docs** on an
    advisory.
    """
    expected_title = 'errata.activity.docs_approval'
    expected_subti = 'lbopf approved the docs on RHBA-2017:27244-01'
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/27244'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set(['lbopf'])
    expected_agent = 'lbopf'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "i": 0,
        "timestamp": 1496279793.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
        "redhat.com-32888-1493960489068-4:481523:0:0:1",
        "topic": "/topic/VirtualTopic.eng.errata.activity.docs_approval",
        "headers": {
            "errata_status": "QE",
            "expires": "0",
            "errata_id": "27244",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "to": "docs_approved",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.activity.docs_approval",
            "when": "2017-06-01 01:16:31 UTC",
            "persistent": "true",
            "who": "lbopf@redhat.com",
            "priority": "4",
            "synopsis": "openstack-packstack and openstack-puppet-modules bug fix advisory",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-32888-1493960489068-4:481523:0:0:1",
            "fulladvisory": "RHBA-2017:27244-01",
            "timestamp": "0",
            "from": "null",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "errata.activity.docs_approval",
            "subject": "errata.activity.docs_approval"
        },
        "msg": ""
    }


class TestErrataAssignedTo(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    Messages like these appear whenever someone **is assigned to** an advisory.
    """
    expected_title = 'errata.activity.assigned_to'
    expected_subti = 'cye assigned rbean to RHBA-2017:28809-02'
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/28809'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set(['rbean', 'cye', 'kernel-qe'])
    expected_agent = 'cye'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "i": 0,
        "timestamp": 1496284509.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
        "redhat.com-32888-1493960489068-4:482002:0:0:1",
        "topic": "/topic/VirtualTopic.eng.errata.activity.assigned_to",
        "headers": {
            "errata_status": "QE",
            "expires": "0",
            "errata_id": "28809",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "to": "rbean@redhat.com",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.activity.assigned_to",
            "when": "2017-06-01 02:35:03 UTC",
            "persistent": "true",
            "who": "cye@redhat.com",
            "priority": "4",
            "synopsis": "kernel bug fix update",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-32888-1493960489068-4:482002:0:0:1",
            "fulladvisory": "RHBA-2017:28809-02",
            "timestamp": "0",
            "from": "kernel-qe@redhat.com",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "errata.activity.assigned_to",
            "subject": "errata.activity.assigned_to"
        },
        "msg": ""
    }


class TestErrataRescheduleCCAT(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    Messages like these appear whenever someone **reschedules** a CCAT test.
    """
    expected_title = 'errata.ccat.reschedule_test'
    expected_subti = 'CCAT for erratum 29873 in cdn-live was rescheduled'
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/29873'
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_agent = None
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        'topic': '/topic/VirtualTopic.eng.errata.ccat.reschedule_test',
        'msg': {
            u'ERRATA_ID': u'29873',
            u'TARGET': u'cdn-live'
        },
        'headers': {
            'TARGET': 'cdn-live',
            'JMS_AMQP_FirstAcquirer': 'false',
            'ERRATA_ID': '29873',
            'JMS_AMQP_MESSAGE_FORMAT': '0',
            'timestamp': '0',
            'destination': '/topic/VirtualTopic.eng.errata.ccat.reschedule_test',
            'persistent': 'true',
            'expires': '0',
            'priority': '4',
            'subscription': '/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>',
            'JMS_AMQP_NATIVE': 'false',
            'message-id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-'
            '35748-1505981049344-2:327116:0:0:1',
            'type': 'errata.ccat.reschedule_test',
            'subject': 'errata.ccat.reschedule_test'
        }
    }


class TestErrataBuildsAdded(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    You'll see a message like this one when someone **adds a build** to
    an advisory.
    """
    expected_title = 'errata.builds.added'
    expected_subti = 'ajackson added libpciaccess-0.13.4-3.1.el7_4 to RHEL advisory 31169'
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/31169'
    expected_packages = set(['libpciaccess'])
    expected_usernames = set(['ajackson'])
    expected_agent = 'ajackson'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "i": 0,
        "timestamp": 1509028483.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-43669-1508744086399-2:216012:0:0:1",
        "topic": "/topic/VirtualTopic.eng.errata.builds.added",
        "headers": {
            "product": "RHEL",
            "expires": "0",
            "errata_id": "31169",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.builds.added",
            "subject": "errata.builds.added",
            "persistent": "true",
            "who": "ajackson@redhat.com",
            "priority": "4",
            "when": "2017-10-26 14:34:37 UTC",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-43669-1508744086399-"
            "2:216012:0:0:1",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "errata.builds.added",
            "brew_build": "libpciaccess-0.13.4-3.1.el7_4"
        },
        "msg": {
            "when": "2017-10-26 14:34:37 UTC",
            "product": "RHEL",
            "who": "ajackson@redhat.com",
            "errata_id": 31169,
            "brew_build": "libpciaccess-0.13.4-3.1.el7_4"
        }
    }


class TestErrataBuildsRemoved(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    You'll see a message like this one when someone **removes a build** from
    an advisory.
    """
    expected_title = 'errata.builds.removed'
    expected_subti = 'sradco removed ovirt-engine-dwh-4.2.1-0.0.master.20171025112108.el7ev from RHV advisory 29571'
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/29571'
    expected_packages = set(['ovirt-engine-dwh'])
    expected_usernames = set(['sradco'])
    expected_agent = 'sradco'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "i": 0,
        "timestamp": 1509028264.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-43669-1508744086399-2:215849:0:0:1",
        "topic": "/topic/VirtualTopic.eng.errata.builds.removed",
        "headers": {
            "product": "RHV",
            "expires": "0",
            "errata_id": "29571",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.builds.removed",
            "subject": "errata.builds.removed",
            "persistent": "true",
            "who": "sradco@redhat.com",
            "priority": "4",
            "when": "2017-10-26 14:31:03 UTC",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-43669-1508744086399-"
            "2:215849:0:0:1",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "errata.builds.removed",
            "brew_build": "ovirt-engine-dwh-4.2.1-0.0.master.20171025112108.el7ev"
        },
        "msg": {
            "when": "2017-10-26 14:31:03 UTC",
            "product": "RHV",
            "who": "sradco@redhat.com",
            "errata_id": 29571,
            "brew_build": "ovirt-engine-dwh-4.2.1-0.0.master.20171025112108.el7ev"
        }
    }


class TestErrataTextChanged(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    You'll see a message like this one when someone **changes the text** in a
    field of an advisory.
    """
    expected_title = 'errata.activity.text_changes'
    expected_subti = ('bkundal changed security_impact, synopsis, cve, topic, '
                      'description, and reference on JBEAP advisory 30821')
    expected_link = 'https://pipeline.engineering.redhat.com/advisory/30821'
    expected_packages = set([])
    expected_usernames = set(['bkundal'])
    expected_agent = 'bkundal'
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "i": 0,
        "timestamp": 1516695443.0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-"
        "42569-1516420517578-2:51216:0:0:1",
        "topic": "/topic/VirtualTopic.eng.errata.activity.text_changes",
        "headers": {
            "product": "JBEAP",
            "expires": "0",
            "errata_id": "30821",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.activity.text_changes",
            "when": "2018-01-23 08:16:46 UTC",
            "persistent": "true",
            "who": "bkundal@redhat.com",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-"
            "42569-1516420517578-2:51216:0:0:1",
            "timestamp": "0",
            "release": "RHEL-7-JBEAP-6.4",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "RHSA",
            "subject": "errata.activity.text_changes"
        },
        "msg": {
            "product": "JBEAP",
            "errata_id": 30821,
            "who": "bkundal@redhat.com",
            "when": "2018-01-23 08:16:46 UTC",
            "text_changes": [
                {
                    "to": "Important",
                    "from": "None",
                    "name": "security_impact"
                },
                {
                    "to": "Important: Red Hat JBoss Enterprise Application Platform 6.4.19 update on RHEL 7",
                    "from": "Red Hat JBoss Enterprise Application Platform 6.4.19 update on RHEL 7",
                    "name": "synopsis"
                },
                {
                    "to": "CVE-2017-12617 CVE-2018-1041 CVE-2017-12174",
                    "from": "",
                    "name": "cve"
                },
                {
                    "to": "An update is now available for Red Hat JBoss Enterprise Application Platform "
                    "6.4 for Red Hat Enterprise Linux 6.\n\nRed Hat Product Security has rated this update "
                    "as having a security impact of Important.A Common Vulnerability Scoring System (CVSS) "
                    "base score,which gives a detailed severity rating,is available for each vulnerability "
                    "from the CVE link(s) in the References section.",
                    "from": "Updated packages that provide Red Hat JBoss Enterprise Application Platform "
                    "6.4.19 and fix several bugs,and add various enhancements are now available for Red Hat "
                    "Enterprise Linux 7.",
                    "name": "topic"
                },
                {
                    "to": "Red Hat JBoss Enterprise Application Platform is a platform for Java\napplications "
                    "based on the JBoss Application Server.\n\nThis release of Red Hat JBoss Enterprise "
                    "Application Platform 6.4.19 serves as a replacement for Red Hat JBoss Enterprise "
                    "Application Platform 6.4.18,and includes bug fixes and enhancements,which are documented "
                    "in the Release Notes document linked to in the References.\n\nSecurity Fix(es):\n\n* It "
                    "was found that when Artemis and HornetQ are configure with UDP discovery and JGroups "
                    "discovery create huge byte array when receiving unexpected multicast message and may "
                    "result in heap memory exhaustion ,full GC and OutOfMemoryError. (CVE-2017-12174)\n\n* "
                    "A vulnerability was discovered in Tomcat where if a servlet context was\nconfigured with "
                    "readonly=false and HTTP PUT requests were allowed,an\nattacker could upload a JSP file to "
                    "that context and achieve code\nexecution. (CVE-2017-12617)\n\n* A vulnerability was found "
                    "in the way RemoteMessageChannel,introduced in\njboss-remoting versions "
                    "3.3.10.Final-redhat-1,reads from an empty buffer.\nAn attacker could use this flaw to cause "
                    "denial of service via high CPU\ncaused by an infinite loop. (CVE-2018-1041)\n\nThe "
                    "CVE-2017-12174 issue was discovered by Masafumi Miura (Red Hat).",
                    "from": "Red Hat JBoss Enterprise Application Platform 6 is a platform for Java\napplications "
                    "based on JBoss Application Server 7. \n\nThis release serves as a replacement for Red Hat "
                    "JBoss Enterprise Application\nPlatform 6.4.18,and includes bug fixes and enhancements. "
                    "Documentation for these\nchanges will be available shortly from the Red Hat JBoss Enterprise "
                    "Application\nPlatform 6.4.19 Release Notes,linked to in the References. \n\nAll users of Red "
                    "Hat JBoss Enterprise Application Platform 6.4 on Red Hat\nEnterprise Linux 7 are advised to "
                    "upgrade to these updated packages. The JBoss\nserver process must be restarted for the update "
                    "to take effect.",
                    "name": "description"
                },
                {
                    "to": "https://access.redhat.com/security/updates/classification/#important\n"
                    "https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/",
                    "from": "https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/"
                    "6.4/index.html",
                    "name": "reference"
                }
            ],
            "release": "RHEL-7-JBEAP-6.4",
            "type": "RHSA"
        }
    }


class TestErrataCCATResult(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    Container Content Availability Testing (CCAT) results are published to the
    UMB whenever a test completes.
    """
    expected_title = 'errata.ccat'
    expected_subti = ('CAT results for erratum 34908 on cdn-stage (automated): pass')
    expected_link = ("https://content-test-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/"
                     "job/stage_cdn_content_validation/6277/")
    expected_packages = set([
        # TODO - this would be very valuable for routing notifications
    ])
    expected_usernames = set([])
    expected_agent = None
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1532442252.0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-34769-1532431903164-21:11079:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.errata.ccat",
        "headers": {
            "BUILD_ID": "6277",
            "content-length": "199",
            "expires": "0",
            "ERRATA_ID": "34908",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "TRIGGER_TYPE": "automated",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.errata.ccat",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "message-id": ("ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com"
                           "-34769-1532431903164-21:11079:0:0:1"),
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "MESSAGE_TYPE": "pass",
            "TARGET": "cdn-stage"
        },
        "signature": None,
        "source_version": "0.9.0",
        "msg": {
            "MESSAGE": "This is a content testing message sent at 2018-07-24 14:23:31.328161",
            "BUILD_URL": ("https://content-test-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/"
                          "job/stage_cdn_content_validation/6277/")
        }
    }


add_doc(locals())

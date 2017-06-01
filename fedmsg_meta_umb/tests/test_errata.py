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


class TestErrataStatusChange(fedmsg.tests.test_meta.Base):
    """ The Errata Tool supports the release workflow for Red Hat content.

    Messages are published when an advisory **changes state**.  This is an
    example of an advisory moving from the QE state back to the NEW_FILES state
    (for modification by developers).
    """
    expected_title = 'errata.activity.status'
    expected_subti = ('fmuellne moved RHBA-2017:27087-02 from QE to NEW_FILES')
    expected_link = 'https://errata.devel.redhat.com/advisory/27087'
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
    expected_link = 'https://errata.devel.redhat.com/advisory/28816'
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
    expected_link = 'https://errata.devel.redhat.com/advisory/10000'
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
            "to": "false",
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
    expected_link = 'https://errata.devel.redhat.com/advisory/26924'
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
    expected_link = 'https://errata.devel.redhat.com/advisory/26924'
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
    expected_link = 'https://errata.devel.redhat.com/advisory/26924'
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
    expected_link = 'https://errata.devel.redhat.com/advisory/28445'
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
    expected_link = 'https://errata.devel.redhat.com/advisory/27244'
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

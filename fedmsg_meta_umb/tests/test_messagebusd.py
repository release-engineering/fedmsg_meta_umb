# Copyright (C) 2020 Red Hat, Inc.
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


class TestMessagebusdTaskRepo(fedmsg.tests.test_meta.Base):
    """ messagebusd receives a message on the Unified Message Bus, performs some action, and sends a response.

    A "task-repo" message requests the creation of a yum repo containing the output of a Brew task.
    """
    expected_title = 'messagebusd.task-repo'
    expected_subti = 'repo requested for task 33314536 by efuller@REDHAT.COM via umbproxy'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taskinfo?taskID=33314536'
    expected_icon = '_static/img/icons/umb.png'
    expected_agent = 'efuller'
    expected_usernames = set(['efuller'])

    msg = {
        'certificate': None,
        'crypto': None,
        'headers': {
            'JMSXUserID': 'msg-umbproxy',
            'JMS_AMQP_MESSAGE_FORMAT': '0',
            'JMS_AMQP_NATIVE': 'false',
            'amq6100_destination': 'queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'amq6100_originalDestination': 'topic://VirtualTopic.devops.messagebusd.task-repo',
            'correlation-id': '25f21d1c-f6a3-438c-ac82-c43d7bcf946c',
            'destination': '/topic/VirtualTopic.devops.messagebusd.task-repo',
            'expires': '0',
            'message-id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-'
            '3:433137:0:0:1',
            'original-destination': '/topic/VirtualTopic.devops.messagebusd.task-repo',
            'priority': '4',
            'reply-to': '/topic/VirtualTopic.devops.messagebusd.reply.task-repo',
            'subscription': '/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'timestamp': '0',
            'type': 'task-repo',
            'umbproxy_username': 'efuller@REDHAT.COM',
            'user': 'efuller'
        },
        'i': 0,
        'msg': {'requesttime': 1606951330.391472, 'task_id': 33314536},
        'msg_id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-3:433137:0:0:1',
        'signature': None,
        'source_name': 'datanommer',
        'source_version': '0.9.1',
        'timestamp': 1606951331.0,
        'topic': '/topic/VirtualTopic.devops.messagebusd.task-repo',
        'username': None
    }


class TestMessagebusdReplyTaskRepo(fedmsg.tests.test_meta.Base):
    """ messagebusd receives a message on the Unified Message Bus, performs some action, and sends a response.

    A "reply.task-repo" message provides the result of a previous "task-repo" message.
    """
    expected_title = 'messagebusd.reply.task-repo'
    expected_subti = 'Successfully ran "flock /var/tmp/task-33314536.lock /usr/bin/brew-task-repo 33314536"'
    expected_link = None
    expected_icon = '_static/img/icons/umb.png'
    expected_agent = None
    expected_usernames = set()

    msg = {
        'certificate': None,
        'crypto': None,
        'headers': {
            'JMSXUserID': 'msg-client-messagebusd',
            'JMS_AMQP_FirstAcquirer': 'false',
            'JMS_AMQP_MESSAGE_FORMAT': '0',
            'JMS_AMQP_NATIVE': 'false',
            'amq6100_destination': 'queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'amq6100_originalDestination': 'topic://VirtualTopic.devops.messagebusd.reply.task-repo',
            'content-length': '1024',
            'correlation-id': '25f21d1c-f6a3-438c-ac82-c43d7bcf946c',
            'destination': '/topic/VirtualTopic.devops.messagebusd.reply.task-repo',
            'expires': '0',
            'message-id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-'
            '3:1534:0:15:1',
            'original-destination': '/topic/VirtualTopic.devops.messagebusd.reply.task-repo',
            'priority': '4',
            'subscription': '/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'timestamp': '0'
        },
        'i': 0,
        'msg': {
            'command_output': [
                'Creating x86_64 repo under '
                '/mnt/redhat/devel/task-repos/official/kernel/4.18.0/255.el8/x86_64\n'
                'Creating ppc64le repo under '
                '/mnt/redhat/devel/task-repos/official/kernel/4.18.0/255.el8/ppc64le\n'
                'Creating aarch64 repo under '
                '/mnt/redhat/devel/task-repos/official/kernel/4.18.0/255.el8/aarch64\n'
                'Creating i686 repo under '
                '/mnt/redhat/devel/task-repos/official/kernel/4.18.0/255.el8/i686\n'
                'Creating s390x repo under '
                '/mnt/redhat/devel/task-repos/official/kernel/4.18.0/255.el8/s390x\n'
                'Creating noarch repo under '
                '/mnt/redhat/devel/task-repos/official/kernel/4.18.0/255.el8/noarch\n'
                'Repos for task 33314536 created under '
                '/mnt/redhat/devel/task-repos/official/kernel/4.18.0/255.el8\n'
            ],
            'commands': [
                [
                    'flock',
                    '/var/tmp/task-33314536.lock',
                    '/usr/bin/brew-task-repo',
                    '33314536'
                ]
            ],
            'endtime': 1606951534.726212,
            'message': 'Successfully ran "flock /var/tmp/task-33314536.lock '
            '/usr/bin/brew-task-repo 33314536"',
            'requesttime': 1606951330.391472,
            'returncode': 0,
            'starttime': 1606951331.458769,
            'status': 'success'
        },
        'msg_id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-3:1534:0:15:1',
        'signature': None,
        'source_name': 'datanommer',
        'source_version': '0.9.1',
        'timestamp': 1606951534.0,
        'topic': '/topic/VirtualTopic.devops.messagebusd.reply.task-repo',
        'username': None
    }


class TestMessagebusdTaskRepoAnon(fedmsg.tests.test_meta.Base):
    """ messagebusd receives a message on the Unified Message Bus, performs some action, and sends a response.

    A "task-repo" message requests the creation of a yum repo containing the output of a Brew task.
    This message is artifically constructed to have no identifying information.
    """
    expected_title = 'messagebusd.task-repo'
    expected_subti = 'repo requested for task 33437766'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taskinfo?taskID=33437766'
    expected_icon = '_static/img/icons/umb.png'
    expected_agent = None
    expected_usernames = set()

    msg = {
        'certificate': None,
        'crypto': None,
        'headers': {
            'JMS_AMQP_MESSAGE_FORMAT': '0',
            'JMS_AMQP_NATIVE': 'false',
            'amq6100_destination': 'queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'amq6100_originalDestination': 'topic://VirtualTopic.devops.messagebusd.task-repo',
            'correlation-id': '12c84ec2-3b04-4fb9-8871-97e1e58938bb',
            'destination': '/topic/VirtualTopic.devops.messagebusd.task-repo',
            'expires': '0',
            'message-id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-'
            '3:347650:0:0:1',
            'original-destination': '/topic/VirtualTopic.devops.messagebusd.task-repo',
            'priority': '4',
            'reply-to': '/topic/VirtualTopic.devops.messagebusd.reply.task-repo',
            'subscription': '/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'timestamp': '0',
            'type': 'task-repo',
        },
        'i': 0,
        'msg': {'requesttime': 1606916274.8746986, 'task_id': 33437766},
        'msg_id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-3:347650:0:0:1',
        'signature': None,
        'source_name': 'datanommer',
        'source_version': '0.9.1',
        'timestamp': 1606916279.0,
        'topic': '/topic/VirtualTopic.devops.messagebusd.task-repo',
        'username': None
    }


class TestMessagebusdStaticRepoRegen(fedmsg.tests.test_meta.Base):
    """ messagebusd receives a message on the Unified Message Bus, performs some action, and sends a response.

    A "static-repo-regen" message requests the regeneration of a yum repo based on the content of a Brew tag.
    """
    expected_title = 'messagebusd.static-repo-regen'
    expected_subti = 'static repo regen requested for tag eng-fedora-33 by mikeb@IPA.REDHAT.COM via umbproxy'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taginfo?tagID=eng-fedora-33'
    expected_icon = '_static/img/icons/umb.png'
    expected_agent = 'mikeb'
    expected_usernames = set(['mikeb'])

    msg = {
        'certificate': None,
        'crypto': None,
        'headers': {
            'JMSXUserID': 'msg-umbproxy',
            'JMS_AMQP_MESSAGE_FORMAT': '0',
            'JMS_AMQP_NATIVE': 'false',
            'amq6100_destination': 'queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'amq6100_originalDestination': 'topic://VirtualTopic.devops.messagebusd.static-repo-regen',
            'correlation-id': '3e67b394-eeb6-436c-875c-a9de5501358a',
            'destination': '/topic/VirtualTopic.devops.messagebusd.static-repo-regen',
            'expires': '0',
            'message-id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-'
            '3:439154:0:0:1',
            'original-destination': '/topic/VirtualTopic.devops.messagebusd.static-repo-regen',
            'priority': '4',
            'reply-to': '/topic/VirtualTopic.devops.messagebusd.umbproxy.reply',
            'subscription': '/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'timestamp': '0',
            'type': 'regen-static-repo',
            'umbproxy_username': 'mikeb@IPA.REDHAT.COM',
            'user': 'umbproxy-web'
        },
        'i': 0,
        'msg': {'requesttime': 1606957014.913, 'tag': 'eng-fedora-33'},
        'msg_id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-3:439154:0:0:1',
        'signature': None,
        'source_name': 'datanommer',
        'source_version': '0.9.1',
        'timestamp': 1606957019.0,
        'topic': '/topic/VirtualTopic.devops.messagebusd.static-repo-regen',
        'username': None
    }


class TestMessagebusdUmbroxyReply(fedmsg.tests.test_meta.Base):
    """ messagebusd receives a message on the Unified Message Bus, performs some action, and sends a response.

    A "umbproxy.reply" message provides the result of a previous request submitted via umbproxy.
    """
    expected_title = 'messagebusd.umbproxy.reply'
    expected_subti = 'Successfully ran "flock /var/tmp/eng-fedora-33.lock /usr/bin/brew-repo-wrapper ' \
        '--basedir /mnt/redhat/rel-eng/repos --taggedfile /mnt/redhat/rel-eng/repos/eng-fedora-33/tagged ' \
        'eng-fedora-33 --unsigned"'
    expected_link = 'https://umbproxy.engineering.redhat.com/'
    expected_icon = '_static/img/icons/umb.png'
    expected_agent = None
    expected_usernames = set()

    msg = {
        'certificate': None,
        'crypto': None,
        'headers': {
            'JMSXUserID': 'msg-client-messagebusd',
            'JMS_AMQP_FirstAcquirer': 'false',
            'JMS_AMQP_MESSAGE_FORMAT': '0',
            'JMS_AMQP_NATIVE': 'false',
            'amq6100_destination': 'queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'amq6100_originalDestination': 'topic://VirtualTopic.devops.messagebusd.umbproxy.reply',
            'content-length': '603',
            'correlation-id': '3e67b394-eeb6-436c-875c-a9de5501358a',
            'destination': '/topic/VirtualTopic.devops.messagebusd.umbproxy.reply',
            'expires': '0',
            'message-id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-'
            '3:1534:0:18:1',
            'original-destination': '/topic/VirtualTopic.devops.messagebusd.umbproxy.reply',
            'priority': '4',
            'subscription': '/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'timestamp': '0'
        },
        'i': 0,
        'msg': {
            'command_output': [''],
            'commands': [
                [
                    'flock',
                    '/var/tmp/eng-fedora-33.lock',
                    '/usr/bin/brew-repo-wrapper',
                    '--basedir',
                    '/mnt/redhat/rel-eng/repos',
                    '--taggedfile',
                    '/mnt/redhat/rel-eng/repos/eng-fedora-33/tagged',
                    'eng-fedora-33',
                    '--unsigned'
                ]
            ],
            'endtime': 1606957024.853463,
            'message': 'Successfully ran "flock /var/tmp/eng-fedora-33.lock '
            '/usr/bin/brew-repo-wrapper --basedir '
            '/mnt/redhat/rel-eng/repos --taggedfile '
            '/mnt/redhat/rel-eng/repos/eng-fedora-33/tagged '
            'eng-fedora-33 --unsigned"',
            'requesttime': 1606957014.913,
            'returncode': 0,
            'starttime': 1606957019.837216,
            'status': 'success'
        },
        'msg_id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-3:1534:0:18:1',
        'signature': None,
        'source_name': 'datanommer',
        'source_version': '0.9.1',
        'timestamp': 1606957024.0,
        'topic': '/topic/VirtualTopic.devops.messagebusd.umbproxy.reply',
        'username': None
    }


class TestMessagebusdStaticRepoRegenJenkins(fedmsg.tests.test_meta.Base):
    """ messagebusd receives a message on the Unified Message Bus, performs some action, and sends a response.

    A "static-repo-regen" message requests the regeneration of a yum repo based on the content of a Brew tag.
    This example was requested by a Jenkins job.
    """
    expected_title = 'messagebusd.static-repo-regen'
    expected_subti = 'static repo regen requested for tag eng-rhel-7-candidate by client msg-rh-jenkins-ci-plugin'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taginfo?tagID=eng-rhel-7-candidate'
    expected_icon = '_static/img/icons/umb.png'
    expected_agent = None
    expected_usernames = set()

    msg = {
        'certificate': None,
        'crypto': None,
        'headers': {
            'CI_NAME': 'revolutionary_engagement',
            'CI_TYPE': 'custom',
            'JMSXUserID': 'msg-rh-jenkins-ci-plugin',
            'amq6100_destination': 'queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'amq6100_originalDestination': 'topic://VirtualTopic.devops.messagebusd.static-repo-regen',
            'correlation-id': 'ff46fa99-617f-459e-8146-e66981f112be',
            'destination': '/topic/VirtualTopic.devops.messagebusd.static-repo-regen',
            'expires': '1606744458723',
            'message-id': 'ID:rhos-d-rhel7-7134-37774-1606658056028-3:1:1:1:1',
            'original-destination': '/topic/VirtualTopic.devops.messagebusd.static-repo-regen',
            'persistent': 'true',
            'priority': '4',
            'reply-to': '/topic/VirtualTopic.qe.ci.static-repo-regen',
            'subscription': '/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'timestamp': '1606658058723',
            'type': 'application/json'
        },
        'i': 0,
        'msg': {'requesttime': 1606658057, 'tag': 'eng-rhel-7-candidate'},
        'msg_id': 'ID:rhos-d-rhel7-7134-37774-1606658056028-3:1:1:1:1',
        'signature': None,
        'source_name': 'datanommer',
        'source_version': '0.9.1',
        'timestamp': 1606658058.0,
        'topic': '/topic/VirtualTopic.devops.messagebusd.static-repo-regen',
        'username': None
    }


class TestMessagebusdStageMwRelease(fedmsg.tests.test_meta.Base):
    """ messagebusd receives a message on the Unified Message Bus, performs some action, and sends a response.

    A "stage-mw-release" message requests the staging of Middleware content to /mnt/redhat in preparation for release.
    """
    expected_title = 'messagebusd.stage-mw-release'
    expected_subti = 'staging requested for release AMQ-BROKER-ON-OPENSHIFT-7.8.0.CR4 by hgao'
    expected_link = None
    expected_icon = '_static/img/icons/umb.png'
    expected_agent = 'hgao'
    expected_usernames = set(['hgao'])

    msg = {
        'certificate': None,
        'crypto': None,
        'headers': {
            'JMSXUserID': 'msg-umbproxy',
            'JMS_AMQP_MESSAGE_FORMAT': '0',
            'JMS_AMQP_NATIVE': 'false',
            'amq6100_destination': 'queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'amq6100_originalDestination': 'topic://VirtualTopic.devops.messagebusd.stage-mw-release',
            'correlation-id': '34f6e9ac-03f8-40fd-b022-024a069a4720',
            'destination': '/topic/VirtualTopic.devops.messagebusd.stage-mw-release',
            'expires': '0',
            'message-id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-'
            '3:220534:0:0:1',
            'original-destination': '/topic/VirtualTopic.devops.messagebusd.stage-mw-release',
            'priority': '4',
            'reply-to': '/topic/VirtualTopic.devops.messagebusd.reply.stage-mw-release',
            'subscription': '/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'timestamp': '0',
            'type': 'stage-mw-release',
            'user': 'hgao'
        },
        'i': 0,
        'msg': {
            'release': 'AMQ-BROKER-ON-OPENSHIFT-7.8.0.CR4',
            'requesttime': 1606833708.849003
        },
        'msg_id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-3:220534:0:0:1',
        'signature': None,
        'source_name': 'datanommer',
        'source_version': '0.9.1',
        'timestamp': 1606833709.0,
        'topic': '/topic/VirtualTopic.devops.messagebusd.stage-mw-release',
        'username': None
    }


class TestMessagebusdBrewTaskRepoReply(fedmsg.tests.test_meta.Base):
    """ messagebusd receives a message on the Unified Message Bus, performs some action, and sends a response.

    A "reply.brew-task-repo" message provides the result of a repo generation triggered by completion of a Brew
    build task.
    """
    expected_title = 'messagebusd.reply.brew-task-repo'
    expected_subti = 'Successfully ran "flock /var/tmp/task-33455032.lock /usr/local/bin/gen-task-repo 33455032"'
    expected_link = None
    expected_icon = '_static/img/icons/umb.png'
    expected_agent = None
    expected_usernames = set()

    msg = {
        'certificate': None,
        'crypto': None,
        'headers': {
            'JMSXUserID': 'msg-client-messagebusd',
            'JMS_AMQP_MESSAGE_FORMAT': '0',
            'JMS_AMQP_NATIVE': 'false',
            'amq6100_destination': 'queue://Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'amq6100_originalDestination': 'topic://VirtualTopic.devops.messagebusd.reply.brew-task-repo',
            'content-length': '802',
            'correlation-id': 'e94a18a3-ea07-4d6e-9ca1-a7f389ec98db',
            'destination': '/topic/VirtualTopic.devops.messagebusd.reply.brew-task-repo',
            'expires': '0',
            'message-id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-'
            '3:62:0:1293:1',
            'original-destination': '/topic/VirtualTopic.devops.messagebusd.reply.brew-task-repo',
            'priority': '4',
            'subscription': '/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.devops.>',
            'timestamp': '0'
        },
        'i': 0,
        'msg': {
            'command_output': [
                'Creating x86_64 repo under '
                '/srv/repos/scratch/istio-build/servicemesh-operator/1.1.10/1.el8/x86_64\n'
                'Repos for task 33455032 created under '
                '/srv/repos/scratch/istio-build/servicemesh-operator/1.1.10/1.el8\n'
                'Wrote repo file to '
                '/srv/repos/scratch/istio-build/servicemesh-operator/1.1.10/1.el8/servicemesh-operator-'
                '1.1.10-1.el8-scratch.repo\n'
                'Sent email to '
                'istio-build/istio-jenkins.rhev-ci-vms.eng.rdu2.redhat.com@redhat.com\n'
            ],
            'commands': [
                [
                    'flock',
                    '/var/tmp/task-33455032.lock',
                    '/usr/local/bin/gen-task-repo',
                    '33455032'
                ]
            ],
            'emails': 'mikeb@redhat.com',
            'endtime': 1606959262.517975,
            'message': 'Successfully ran "flock /var/tmp/task-33455032.lock '
            '/usr/local/bin/gen-task-repo 33455032"',
            'requesttime': None,
            'returncode': 0,
            'starttime': 1606959252.793886,
            'status': 'success'
        },
        'msg_id': 'ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-40384-1606738019242-3:62:0:1293:1',
        'signature': None,
        'source_name': 'datanommer',
        'source_version': '0.9.1',
        'timestamp': 1606959263.0,
        'topic': '/topic/VirtualTopic.devops.messagebusd.reply.brew-task-repo',
        'username': None
    }


add_doc(locals())

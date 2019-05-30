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
# Authors:  Stanislav Ochotnicky <sochotnicky@redhat.com>

import fedmsg.tests.test_meta
from .common import add_doc

class TestMetaXORcontainerImageInsert(fedmsg.tests.test_meta.Base):
    """ The MetaXOR service provides images to lightblue database

    Messages (like the example given here) are published when information about
    new image gets stored in Lightblue
    """
    expected_title = 'metaxor.events.lightblue.containerImage.insert'
    expected_subti = ('New containerImage entity for unpublished container image '
                      'aos3-installation-docker-v3.3.1.46.37-1 has been created.')
    expected_link = ('https://brewweb.engineering.redhat.com/brew/search?'
                     'terms=aos3-installation-docker-v3.3.1.46.37-1&'
                     'type=build&match=exact')
    expected_packages = set(['aos3-installation-docker'])
    expected_icon = '_static/img/icons/metaxor.png'

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1516924184.0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com"
        "-42569-1516420517578-2:230301:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.metaxor.events.lightblue.containerImage.insert",
        "headers": {
            "content-length": "187",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "overridden": "false",
            "full_refresh": "false",
            "force_refresh": "false",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.metaxor.events.lightblue."
            "containerImage.insert",
            "schema_version": "1.0.4",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod."
            "VirtualTopic.eng.>",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2."
            "redhat.com-42569-1516420517578-2:230301:0:0:1",
            "timestamp": "0",
            "published": "false",
            "JMS_AMQP_FirstAcquirer": "false",
            "changes": "[]",
            "brew_build": "aos3-installation-docker-v3.3.1.46.37-1"
        },
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "overridden": False,
            "force_refresh": False,
            "full_refresh": False,
            "schema_version": "1.0.4",
            "published": False,
            "changes": [],
            "brew_build": "aos3-installation-docker-v3.3.1.46.37-1"
        }
    }


class TestMetaXORcontainerImageUpdate(fedmsg.tests.test_meta.Base):
    """ The MetaXOR service provides images to lightblue database

    Messages (like the example given here) are published when the existing image
    in lightblue gets updated
    """
    expected_title = 'metaxor.events.lightblue.containerImage.update'
    expected_subti = ('Existing containerImage entity for published container '
                      'image etcd-docker-3.2.11-2 has been updated.')
    expected_link = ('https://brewweb.engineering.redhat.com/brew/search?'
                     'terms=etcd-docker-3.2.11-2&type=build&match=exact')
    expected_packages = set(['etcd-docker'])
    expected_icon = '_static/img/icons/metaxor.png'

    msg = {
        'username': None,
        'source_name': 'datanommer',
        'certificate': None,
        'i': 0,
        'timestamp': 1517059491.0,
        'msg_id': 'ID:messaging-devops-broker02.web.prod.ext.phx2.redhat'
        '.com-42569-1516420517578-2:283330:0:0:1',
        'crypto': None,
        'topic': '/topic/VirtualTopic.eng.metaxor.events.lightblue.'
        'containerImage.update',
        'headers': {
            'content-length': '206',
            'full_refresh': 'false',
            'JMS_AMQP_MESSAGE_FORMAT': '0',
            'overridden': 'false',
            'force_refresh': 'true',
            'JMS_AMQP_NATIVE': 'false',
            'expires': '0',
            'published': 'true',
            'schema_version': '1.0.4',
            'priority': '4',
            'JMS_AMQP_FirstAcquirer': 'false',
            'timestamp': '0',
            'destination': '/topic/VirtualTopic.eng.metaxor.events.'
            'lightblue.containerImage.update',
            'message-id': 'ID:messaging-devops-broker02.web.prod.ext.'
            'phx2.redhat.com-42569-1516420517578-2:283330:0:0:1',
            'changes': '[brew, lastUpdateDate, repositories]',
            'brew_build': 'etcd-docker-3.2.11-2',
            'subscription': '/queue/Consumer.client-datanommer.'
            'openpaas-prod.VirtualTopic.eng.>'
        },
        'signature': None,
        'source_version': '0.8.2',
        'msg': {
            'overridden': False,
            'force_refresh': True,
            'full_refresh': False,
            'schema_version': '1.0.4',
            'published': True,
            'changes': [
                'brew',
                'lastUpdateDate',
                'repositories'
            ],
            'brew_build': 'etcd-docker-3.2.11-2'
        }
    }

class TestMetaXORRefreshEvent(fedmsg.tests.test_meta.Base):
    """ The MetaXOR service provides images to lightblue database

    Messages (like the example given here) are published when MetaXOR finishes
    refreshing metadata about whole repository
    """
    expected_title = 'metaxor.events.refresh'
    expected_subti = ('Container repository openshift3/registry-console '
                      'has been refreshed in Lightblue.')
    expected_link = ('https://access.redhat.com/containers/#/'
                     'registry.access.redhat.com/openshift3/registry-console')
    expected_packages = set([])
    expected_icon = '_static/img/icons/metaxor.png'

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1517069378.0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2."
        "redhat.com-42569-1516420517578-2:285156:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.metaxor.events.refresh",
        "headers": {
            "repository_filter": "null",
            "content-length": "95",
            "destination": "/topic/VirtualTopic.eng.metaxor.events.refresh",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "repository": "openshift3/registry-console",
            "full_refresh": "false",
            "JMS_AMQP_NATIVE": "false",
            "expires": "0",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2"
            ".redhat.com-42569-1516420517578-2:285156:0:0:1",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod."
            "VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "repository_filter": None,
            "full_refresh": False,
            "repository": "openshift3/registry-console"
        }
    }


class TestMetaXORStrMessage(fedmsg.tests.test_meta.Base):
    """ The MetaXOR service provides images to lightblue database

    Messages (like the example given here) are published when we issue command
    to MetaXOR using strings
    """
    expected_title = 'metaxor.internal.refresh'
    expected_subti = ('Non dictionary message')
    expected_link = None
    expected_packages = set([])
    expected_icon = '_static/img/icons/metaxor.png'

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1517069378.0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2."
        "redhat.com-42569-1516420517578-2:285156:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.metaxor.internal.refresh",
        "headers": {
            "repository_filter": "null",
            "content-length": "95",
            "destination": "/topic/VirtualTopic.eng.metaxor.internal.refresh",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "repository": "openshift3/registry-console",
            "full_refresh": "false",
            "JMS_AMQP_NATIVE": "false",
            "expires": "0",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2"
            ".redhat.com-42569-1516420517578-2:285156:0:0:1",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod."
            "VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.8.2",
        "msg": "Non dictionary message"
    }


class TestMetaXORBadMessage(fedmsg.tests.test_meta.Base):
    """ The MetaXOR service provides images to lightblue database

    Messages (like the example given here) are published when we send non-string
    messages to metaxor. These likely can't be simply displayed so let's just
    put a placeholder for them'
    """
    expected_title = 'metaxor.internal.refresh'
    expected_subti = ('Unknown message format')
    expected_link = None
    expected_packages = set()
    expected_objects = set()
    expected_icon = '_static/img/icons/metaxor.png'

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1517069378.0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2."
        "redhat.com-42569-1516420517578-2:285156:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.metaxor.internal.refresh",
        "headers": {
            "repository_filter": "null",
            "content-length": "95",
            "destination": "/topic/VirtualTopic.eng.metaxor.internal.refresh",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "repository": "openshift3/registry-console",
            "full_refresh": "false",
            "JMS_AMQP_NATIVE": "false",
            "expires": "0",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2"
            ".redhat.com-42569-1516420517578-2:285156:0:0:1",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod."
            "VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.8.2",
        "msg": 123
    }


class TestMetaXORcontainerRepositoryInsert(fedmsg.tests.test_meta.Base):
    """ The MetaXOR service provides repositories to lightblue database

    Messages (like the example given here) are published when the new
    repository is created in Lightblue
    """
    expected_title = 'metaxor.events.lightblue.containerRepository.insert'
    expected_subti = ('New published container repository rhel7/rhel has '
                      'been created.')
    expected_link = ('https://access.redhat.com/containers/#/'
                     'registry.access.redhat.com/rhel7/rhel')
    expected_objects = {'rhel7/rhel'}
    expected_icon = '_static/img/icons/metaxor.png'

    msg = {
        'username': None,
        'source_name': 'datanommer',
        'certificate': None,
        'i': 0,
        'timestamp': 1517059491.0,
        'msg_id': 'ID:messaging-devops-broker02.web.prod.ext.phx2.redhat'
        '.com-42569-1516420517578-2:283330:0:0:1',
        'crypto': None,
        'topic': '/topic/VirtualTopic.eng.metaxor.events.lightblue'
                 '.containerRepository.insert',
        'headers': {
            'content-length': '206',
            'full_refresh': 'false',
            'JMS_AMQP_MESSAGE_FORMAT': '0',
            'overridden': 'false',
            'force_refresh': 'true',
            'JMS_AMQP_NATIVE': 'false',
            'expires': '0',
            'published': 'true',
            'schema_version': '1.0.0',
            'priority': '4',
            'JMS_AMQP_FirstAcquirer': 'false',
            'timestamp': '0',
            'destination': '/topic/VirtualTopic.eng.metaxor.events.'
            'lightblue.containerRepository.insert',
            'message-id': 'ID:messaging-devops-broker02.web.prod.ext.'
            'phx2.redhat.com-42569-1516420517578-2:283330:0:0:1',
            'changes': '[lastUpdateDate]',
            'brew_build': 'etcd-docker-3.2.11-2',
            'subscription': '/queue/Consumer.client-datanommer.'
            'openpaas-prod.VirtualTopic.eng.>'
        },
        'signature': None,
        'source_version': '0.8.2',
        'msg': {
            'published': True,
            'repository': 'rhel7/rhel',
            'registry': 'registry.access.redhat.com',
            'full_refresh': False,
            'force_refresh': False,
            'schema_version': '1.0.0',
            'changes': [
                'lastUpdateDate'
            ]
        }
    }


class TestMetaXORcontainerRepositoryUpdate(fedmsg.tests.test_meta.Base):
    """ The MetaXOR service provides repositories to lightblue database

    Messages (like the example given here) are published when the existing
    repository is updated in Lightblue
    """
    expected_title = 'metaxor.events.lightblue.containerRepository.update'
    expected_subti = ('Existing published container repository rhel7/rhel has '
                      'been updated.')
    expected_link = ('https://access.redhat.com/containers/#/'
                     'registry.access.redhat.com/rhel7/rhel')
    expected_objects = {'rhel7/rhel'}
    expected_icon = '_static/img/icons/metaxor.png'

    msg = {
        'username': None,
        'source_name': 'datanommer',
        'certificate': None,
        'i': 0,
        'timestamp': 1517059491.0,
        'msg_id': 'ID:messaging-devops-broker02.web.prod.ext.phx2.redhat'
        '.com-42569-1516420517578-2:283330:0:0:1',
        'crypto': None,
        'topic': '/topic/VirtualTopic.eng.metaxor.events.lightblue'
                 '.containerRepository.update',
        'headers': {
            'content-length': '206',
            'full_refresh': 'false',
            'JMS_AMQP_MESSAGE_FORMAT': '0',
            'overridden': 'false',
            'force_refresh': 'true',
            'JMS_AMQP_NATIVE': 'false',
            'expires': '0',
            'published': 'true',
            'schema_version': '1.0.0',
            'priority': '4',
            'JMS_AMQP_FirstAcquirer': 'false',
            'timestamp': '0',
            'destination': '/topic/VirtualTopic.eng.metaxor.events.'
            'lightblue.containerRepository.update',
            'message-id': 'ID:messaging-devops-broker02.web.prod.ext.'
            'phx2.redhat.com-42569-1516420517578-2:283330:0:0:1',
            'changes': '[lastUpdateDate]',
            'brew_build': 'etcd-docker-3.2.11-2',
            'subscription': '/queue/Consumer.client-datanommer.'
            'openpaas-prod.VirtualTopic.eng.>'
        },
        'signature': None,
        'source_version': '0.8.2',
        'msg': {
            'published': True,
            'repository': 'rhel7/rhel',
            'registry': 'registry.access.redhat.com',
            'full_refresh': False,
            'force_refresh': False,
            'schema_version': '1.0.0',
            'changes': [
                'lastUpdateDate'
            ]
        }
    }

class TestMetaXORnternalRefreshRepo(fedmsg.tests.test_meta.Base):
    """ The MetaXOR service provides images to lightblue database

    Messages (like the example given here) are published when user/service
    requests repository update done by workers
    """
    expected_title = 'metaxor.internal.refresh.repository'
    expected_subti = ('Repository update (2) requested by metaxor - '
                      'jboss-datagrid-7/datagrid72-openshift')
    expected_objects = set(['jboss-datagrid-7/datagrid72-openshift'])
    expected_icon = '_static/img/icons/metaxor.png'
    expected_usernames = {'metaxor'}

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1537794802.0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-38086-1536885036904-4:664804:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.metaxor.internal.refresh.repository",
        "headers": {
            "content-length": "130",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "full_refresh": "false",
            "force_refresh": "false",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.metaxor.internal.refresh.repository",
            "persistent": "true",
            "priority": "2",
            "subscription": "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>",
            "user": "metaxor",
            "timestamp": "0",
            "message-id":
                "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-38086-1536885036904-4:664804:0:0:1",
            "name": "jboss-datagrid-7/datagrid72-openshift"
        },
        "signature": None,
        "source_version": "0.9.1",
        "msg": {
            "force_refresh": False,
            "priority": 2,
            "full_refresh": False,
            "name": "jboss-datagrid-7/datagrid72-openshift",
            "user": "metaxor"
        }
    }


add_doc(locals())

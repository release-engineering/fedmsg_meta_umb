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
# Authors: Gowrishankar Rajaiyan <grajaiya@redhat.com>

import fedmsg.tests.test_meta


class TestLegacyTestMessage(fedmsg.tests.test_meta.Base):
    """ shanks once sent a test message like this one... """
    expected_title = 'cips'
    expected_link = None
    expected_subti = None
    expected_packages = set([])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "i": 0,
        "timestamp": 1509120145.0,
        "msg_id": "ID:somebroker01-43669-1508744086399-2:286434:0:0:2",
        "topic": "/topic/VirtualTopic.eng.cips",
        "headers": {
            "content-length": "38",
            "destination": "/topic/VirtualTopic.eng.cips",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "msgnum": "1",
            "expires": "0",
            "priority": "4",
            "message-id": "ID:somebroker01-43669-1508744086399-2:286434:0:0:2",
            "msgtype": "test",
            "timestamp": "2017-10-27 16:02:12.643878",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "msg": {
            "message": "This is test message 1."
        }
    }


class TestCIPSStart(fedmsg.tests.test_meta.Base):
    """ `CIPS <https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-package-sanity-documentation/
    lastSuccessfulBuild/artifact/cips/docs/builddir/index.html>`_ performs basic package sanity testing of rpms.

    Messages (like the example given here) are published when an **CIPS**
    job is **starting**. (A CIPS job performs basic sanity testing for the given brew build).
    """
    expected_title = 'cips.start'
    expected_link = ('https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/'
                     'ci-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/1915/')
    expected_subti = ('continuous integration package sanity testing started for component: setup-2.8.71-7.el7_4 '
                      'with brew task_id: 14393825')
    expected_packages = set(['setup'])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1509104627.0,
        "msg_id": "ID:somebroker-43669-1508744086399-2:275322:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.cips.start",
        "headers": {
            "ci_type": "ci-cips",
            "content-length": "43",
            "expires": "0",
            "id": "14393825",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.cips.starting",
            "component": "setup-2.8.71-7.el7_4",
            "priority": "4",
            "message-id": "ID:somebroker-43669-1508744086399-2:275322:0:0:1",
            "jenkins_build_url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
                                 "ci-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/1915/",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "start_time": "2017-10-27T11:43:51+00:00"
        }
    }


class TestCIPSEnd(fedmsg.tests.test_meta.Base):
    """ `CIPS <https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-package-sanity-documentation/
    lastSuccessfulBuild/artifact/cips/docs/builddir/index.html>`_ performs basic package sanity testing of rpms.

    Messages (like the example given here) are published when an **CIPS**
    job is **completed**. (A CIPS job performs basic sanity testing for the given brew build).
    """
    expected_title = 'cips.end'
    expected_link = ('https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/'
                     'ci-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/1915/')
    expected_subti = ('continuous integration package sanity testing completed for component: setup-2.8.71-7.el7_4 '
                      'with brew task_id: 14393825')
    expected_packages = set(['setup'])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1509104805.0,
        "msg_id": "ID:somebroker-43669-1508744086399-2:275325:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.cips.end",
        "headers": {
            "ci_type": "ci-cips",
            "content-length": "41",
            "expires": "0",
            "id": "14393825",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.cips.completed",
            "component": "setup-2.8.71-7.el7_4",
            "priority": "4",
            "message-id": "ID:somebroker-43669-1508744086399-2:275325:0:0:1",
            "jenkins_build_url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
                                 "ci-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/1915/",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "end_time": "2017-10-27T11:47:02+00:00"
        }
    }


class TestCIPSComplete(fedmsg.tests.test_meta.Base):
    """ `CIPS <https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-package-sanity-documentation/
    lastSuccessfulBuild/artifact/cips/docs/builddir/index.html>`_ performs basic package sanity testing of rpms.

    Messages (like the example given here) are published when an **CIPS**
    job is **completed**. (A CIPS job performs basic sanity testing for the given brew build).
    """
    expected_title = 'cips.complete'
    expected_link = ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-package-sanity-development/"
                     "label=ose-slave-tps,provision_arch=x86_64/1858/")
    expected_subti = ('continuous integration package sanity testing PASSED for '
                      'component: setup-2.8.71-7.el7_4 with brew task_id: 15485779')
    expected_packages = set(['setup'])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "username": "null",
        "source_name": "datanommer",
        "certificate": "null",
        "i": 0,
        "timestamp": 1520336954.0,
        "msg_id": "ID:somebroker-37288-1518002445552-2:1414297:0:0:1",
        "crypto": "null",
        "topic": "/topic/VirtualTopic.eng.cips.complete",
        "headers": {
            "content-length": "1102",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "timestamp": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.cips.complete",
            "component": "setup-2.8.71-7.el7_4",
            "nvr": "setup-2.8.71-7.el7_4",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "message-id": "ID:somebroker-37288-1518002445552-2:1414297:0:0:1",
            "scratch": "true",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "brew-build",
            "id": "15485779",
            "issuer": "jenkins/some-jenkins"
        },
        "signature": "null",
        "source_version": "0.8.2",
        "msg": {
            "category": "sanity",
            "status": "PASSED",
            "ci": {
                "name": "RPM Factory",
                "url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com",
                "environment": "production",
                "team": "rpm-factory",
                "irc": "#rpm-factory",
                "email": "nobody@redhat.com"
            },
            "run": {
                "url": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-package-sanity-development/"
                        "label=ose-slave-tps,provision_arch=x86_64/1858/"),
                "rebuild": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-package-sanity-"
                            "development/label=ose-slave-tps,provision_arch=x86_64/1858//rebuild/parametrized"),
                "log": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-package-sanity-development/"
                        "label=ose-slave-tps,provision_arch=x86_64/1858//console")
            },
            "name": "tier0",
            "recipients": [],
            "system": [
                {
                    "os": "rhel-7.4-server-x86_64-updated",
                    "provider": "openstack"
                }
            ],
            "artifact": {
                "nvr": "setup-2.8.71-7.el7_4",
                "scratch": "true",
                "component": "setup-2.8.71-7.el7_4",
                "type": "brew-build",
                "id": 15485779,
                "issuer": "jenkins/some-jenkins"
            },
            "thread_id": "",
            "xunit": ""
        }
    }

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


class TestTPSStart(fedmsg.tests.test_meta.Base):
    """ `TPS-next <https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/test-package-sanity-documentation/
    lastSuccessfulBuild/artifact/docs/index.html>`_ performs basic package sanity testing of rpms.

    Messages (like the example given here) are published when an **TPS**
    job is **starting**. (A TPS job performs basic sanity testing for the given brew build).
    """
    expected_title = 'tps.starting'
    expected_link = ('https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/'
                     'test-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/1915/')
    expected_subti = 'package sanity testing started for component: setup-2.8.71-7.el7_4 with brew task_id: 14393825'
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
        "topic": "/topic/VirtualTopic.eng.tps.starting",
        "headers": {
            "ci_type": "ci-tps",
            "content-length": "43",
            "expires": "0",
            "brew_task_id": "14393825",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.tps.starting",
            "component": "setup-2.8.71-7.el7_4",
            "priority": "4",
            "message-id": "ID:somebroker-43669-1508744086399-2:275322:0:0:1",
            "jenkins_build_url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
                                 "test-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/1915/",
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


class TestTPSCompleted(fedmsg.tests.test_meta.Base):
    """ `TPS-next <https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/test-package-sanity-documentation/
    lastSuccessfulBuild/artifact/docs/index.html>`_ performs basic package sanity testing of rpms.

    Messages (like the example given here) are published when an **TPS**
    job is **completed**. (A TPS job performs basic sanity testing for the given brew build).
    """
    expected_title = 'tps.completed'
    expected_link = ('https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/'
                     'test-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/1915/')
    expected_subti = 'package sanity testing completed for component: setup-2.8.71-7.el7_4 with brew task_id: 14393825'
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
        "topic": "/topic/VirtualTopic.eng.tps.completed",
        "headers": {
            "ci_type": "ci-tps",
            "content-length": "41",
            "expires": "0",
            "brew_task_id": "14393825",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.tps.completed",
            "component": "setup-2.8.71-7.el7_4",
            "priority": "4",
            "message-id": "ID:somebroker-43669-1508744086399-2:275325:0:0:1",
            "jenkins_build_url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
                                 "test-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/1915/",
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


class TestTPSResults(fedmsg.tests.test_meta.Base):
    """ `TPS-next <https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/test-package-sanity-documentation/
    lastSuccessfulBuild/artifact/docs/index.html>`_ performs basic package sanity testing of rpms.

    Messages (like the example given here) are published when an **TPS**
    job is **performed**. (A TPS job performs basic sanity testing for the given brew build).
    """
    expected_title = 'tps'
    expected_link = ('https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/'
                     'test-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/1915/')
    expected_subti = 'package sanity testing results for component: setup-2.8.71-7.el7_4 with brew task_id: 14393825'
    expected_packages = set(['setup'])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1509104808.0,
        "msg_id": "ID:somebroker-43669-1508744086399-2:275326:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.tps",
        "headers": {
            "ci_type": "ci-tps",
            "content-length": "931",
            "expires": "0",
            "brew_task_id": "14393825",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.tps",
            "component": "setup-2.8.71-7.el7_4",
            "priority": "4",
            "message-id": "ID:somebroker-43669-1508744086399-2:275326:0:0:1",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "environment": {
                "resource_group_type": "openstack",
                "resource_base_image": "rhel-7.4-server-x86_64-updated",
                "arch": "x86_64",
                "brew_tag": "rhel-7.4-z-candidate",
                "build_type": "scratch"
            },
            "tests": {
                "remove": "SKIPPED",
                "install": "PASSED",
                "update": "PASSED"
            },
            "infrastructure": {
                "jenkins_job_url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
                                   "test-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/",
                "jenkins_build_url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
                                     "test-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/1915/"
            },
            "results": {
                "start_time": "2017-10-27T11:43:51+00:00",
                "end_time": "2017-10-27T11:47:02+00:00",
                "tps_report": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
                              "test-package-sanity-development/label=ose-slave-tps,provision_arch=x86_64/734/"
                              "/artifact/tps-next/reports/results.html",
                "tps_status": "PASSED"
            }
        }
    }

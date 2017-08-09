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


class TestRHCHISanityFinish(fedmsg.tests.test_meta.Base):
    """ The RHCHI pipeline validates containers.

    Messages (like the example given here) are published when the **sanity**
    phase of the pipeline **completes**.
    """
    expected_title = 'rhchi.sanity.finished'
    expected_subti = ('The sanity phase of the RHCHI pipeline passed for '
                      'openshift3/metrics-hawkular-metrics')
    expected_link = ('https://chi-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/'
                     'job/sanity-prod/324/')
    expected_packages = set(['metrics-hawkular-metrics-docker'])
    expected_icon = ('https://chi-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/'
                     'static/0e416130/images/headshot.png')

    msg = {
        "i": 0,
        "timestamp": 1500320889.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat."
        "com-36770-1500288178994-2:18523:0:0:1",
        "topic": "/topic/VirtualTopic.eng.rhchi.sanity.finished",
        "headers": {
            "status": "passed",
            "priority": "4",
            "content-length": "881",
            "destination": "/topic/VirtualTopic.eng.rhchi.sanity.finished",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "timestamp": "0",
            "url": "https://chi-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
            "sanity-prod/324/",
            "JMS_AMQP_NATIVE": "False",
            "address": "topic://VirtualTopic.eng.rhchi.sanity.finished",
            "rhchi_stage": "sanity",
            "expires": "0",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-36770-1500288178994-2:18523:0:0:1",
            "finished": "1.500320888567753E9",
            "container_nvr": "metrics-hawkular-metrics-docker-3.4.1-29",
            "container_name": "openshift3/metrics-hawkular-metrics",
            "JMS_AMQP_FirstAcquirer": "False",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "msg": {
            "triggered_by": {
                "status": "passed",
                "triggered_by": None,
                "original_topic": "topic://VirtualTopic.eng.rhchi.build.finished",
                "JMS_AMQP_MESSAGE_FORMAT": 0,
                "url": "https://brew.engineering.redhat.com/brew/buildinfo?buildID=574451",
                "JMS_AMQP_NATIVE": False,
                "address": "topic://VirtualTopic.eng.rhchi.build.finished",
                "rhchi_stage": "build",
                "finished": 1500320505.0,
                "container_nvr": "metrics-hawkular-metrics-docker-3.4.1-29",
                "container_name": "openshift3/metrics-hawkular-metrics",
                "JMS_AMQP_FirstAcquirer": False,
                "type": "rhchi"
            },
            "container_validation_data": {
                "container_img": {
                    "container_registry_url": "brew-pulp-docker01.web.prod.ext.phx2"
                    ".redhat.com:8888/openshift3/metrics-hawkular-metrics:3.4.1-29"
                },
                "dist_git_hash": "19881dfcf68522e4915cf7a5f0ea35fb95376f1c",
                "dist_git_branch": "rhaos-3.4-rhel-7",
                "container_validation_id": "7a99050d-34c2-432d-a051-f55c3799db41"
            }
        }
    }


class TestRHCHISanityStarted(fedmsg.tests.test_meta.Base):
    """ The RHCHI pipeline validates containers.

    Messages (like the example given here) are published when the **sanity**
    phase of the pipeline **starts**.
    """
    expected_title = 'rhchi.sanity.started'
    expected_subti = ('The sanity phase of the RHCHI pipeline started for '
                      'chi-smoke-test')
    expected_link = ('https://chi-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/'
                     'job/sanity-prod/1085/')
    expected_packages = set(['chi-smoke-test-af3ab946-bf36-484e'])
    expected_icon = ('https://chi-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/'
                     'static/0e416130/images/headshot.png')

    msg = {
        "i": 0,
        "timestamp": 1502234849.0,
        "msg_id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat."
        "com-37191-1501276833669-2:264280:0:0:1",
        "topic": "/topic/VirtualTopic.eng.rhchi.sanity.started",
        "headers": {
            "priority": "4",
            "content-length": "1105",
            "destination": "/topic/VirtualTopic.eng.rhchi.sanity.started",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "timestamp": "0",
            "started": "1.502234821027946E9",
            "JMS_AMQP_NATIVE": "false",
            "address": "topic://VirtualTopic.eng.rhchi.sanity.started",
            "container_validation_id": "af3ab946-bf36-484e-94b4-af00a16ddfd7",
            "expires": "0",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat."
            "com-37191-1501276833669-2:264280:0:0:1",
            "container_chidata_url": "http://git.app.eng.bos.redhat.com/git/rhchi.git/"
            "plain/tests/e2e/CHIData.yaml",
            "container_nvr": "chi-smoke-test-af3ab946-bf36-484e-94b4-af00a16ddfd7",
            "url": "https://chi-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/sanity-prod/1085/",
            "container_name": "chi-smoke-test",
            "rhchi_stage": "sanity",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "msg": {
            "triggered_by": {
                "status": "passed",
                "triggered_by": {
                    "container_chidata_url": "http://git.app.eng.bos.redhat.com/git/rhchi.git/"
                    "plain/tests/e2e/CHIData.yaml",
                    "triggered_by": None,
                    "container_nvr": "chi-smoke-test-af3ab946-bf36-484e-94b4-af00a16ddfd7",
                    "container_validation_id": "af3ab946-bf36-484e-94b4-af00a16ddfd7",
                    "container_name": "chi-smoke-test"
                },
                "original_topic": "topic://VirtualTopic.eng.rhchi.build.finished",
                "JMS_AMQP_MESSAGE_FORMAT": 0,
                "url": "https://chi-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/e2e-smoke-test/7/",
                "JMS_AMQP_NATIVE": False,
                "address": "topic://VirtualTopic.eng.rhchi.build.finished",
                "container_validation_id": "af3ab946-bf36-484e-94b4-af00a16ddfd7",
                "container_chidata_url": "http://git.app.eng.bos.redhat.com/git/rhchi.git/"
                "plain/tests/e2e/CHIData.yaml",
                "finished": 1502234823.80292,
                "container_nvr": "chi-smoke-test-af3ab946-bf36-484e-94b4-af00a16ddfd7",
                "container_name": "chi-smoke-test",
                "rhchi_stage": "build",
                "JMS_AMQP_FirstAcquirer": False,
                "type": "rhchi"
            },
            "container_validation_data": {
                "container_img": "",
                "dist_git_hash": "",
                "dist_git_branch": ""
            }
        }
    }

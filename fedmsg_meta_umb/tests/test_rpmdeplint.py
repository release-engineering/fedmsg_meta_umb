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


class TestRPMDEPLINTStart(fedmsg.tests.test_meta.Base):
    """ `rpmdeplint <https://pagure.io/rpmdeplint>`_ tool finds errors in RPM packages in the context
    of their dependency graph.

    Messages (like the example given here) are published when an **rpmdeplint**
    job is **starting**.
    """
    expected_title = 'rpmdeplint.start'
    expected_link = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/946/'
    expected_subti = ('rpmdeplint testing started for '
                      'component: sip-4.19.7-3.el8+7 with brew task_id: 16868906')
    expected_packages = set(['sip'])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1530007015.0,
        "msg_id": "ID:some-broker01.com-41274-1529619027429-2:208825:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.rpmdeplint.start",
        "headers": {
            "ci_type": "ci-rpmdeplint",
            "content-length": "43",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.rpmdeplint.start",
            "component": "sip",
            "nvr": "sip-4.19.7-3.el8+7",
            "priority": "4",
            "message-id": "ID:some-broker01.com-41274-1529619027429-2:208825:0:0:1",
            "jenkins_build_url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/946/",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "id": "16868906",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.9.0",
        "msg": {
            "start_time": "2018-06-26T09:56:42+00:00"
        }
    }


class TestRPMDEPLINTEnd(fedmsg.tests.test_meta.Base):
    """ `rpmdeplint <https://pagure.io/rpmdeplint>`_ tool finds errors in RPM packages in the context
    of their dependency graph.

    Messages (like the example given here) are published when an **rpmdeplint**
    job is **ending**.
    """
    expected_title = 'rpmdeplint.end'
    expected_link = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/946/'
    expected_subti = ('rpmdeplint testing ended for '
                      'component: sip-4.19.7-3.el8+7 with brew task_id: 16868906')
    expected_packages = set(['sip'])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1530007113.0,
        "msg_id": "ID:some-broker01.com-41274-1529619027429-2:208939:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.rpmdeplint.end",
        "headers": {
            "ci_type": "ci-rpmdeplint",
            "content-length": "41",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.rpmdeplint.end",
            "component": "sip",
            "nvr": "sip-4.19.7-3.el8+7",
            "priority": "4",
            "message-id": "ID:some-broker01.com-41274-1529619027429-2:208939:0:0:1",
            "jenkins_build_url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/946/",
            "timestamp": "0",
            "JMS_AMQP_FirstAcquirer": "false",
            "id": "16868906",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.9.0",
        "msg": {
            "end_time": "2018-06-26T09:58:25+00:00"
        }
    }


class TestRPMDEPLINTComplete(fedmsg.tests.test_meta.Base):
    """ `rpmdeplint <https://pagure.io/rpmdeplint>`_ tool finds errors in RPM packages in the context
    of their dependency graph.

    Messages (like the example given here) are published when an **rpmdeplint**
    job is **complete**.
    """
    expected_title = 'rpmdeplint.complete'
    expected_link = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/'
    expected_subti = ('rpmdeplint testing FAILED for '
                      'component: sip-4.19.7-3.el8+7 with brew task_id: 16869293')
    expected_packages = set(['sip'])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1530068522.0,
        "msg_id": "ID:some-broker01.com-41274-1529619027429-2:276135:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.rpmdeplint.complete",
        "headers": {
            "content-length": "1561",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "timestamp": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.rpmdeplint.complete",
            "component": "sip",
            "nvr": "sip-4.19.7-3.el8+7",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "message-id": "ID:some-broker01.com-41274-1529619027429-2:276135:0:0:1",
            "scratch": "true",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "brew-build",
            "id": "16869293",
            "issuer": "lbalhar"
        },
        "signature": None,
        "source_version": "0.9.0",
        "msg": {
            "category": "sanity",
            "status": "FAILED",
            "ci": {
                "name": "RPM Factory",
                "url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com",
                "environment": "production",
                "team": "rpm-factory",
                "irc": "#rpm-factory",
                "email": "nobody@redhat.com"
            },
            "run": {
                "url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/",
                "rebuild": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/"
                            "/rebuild/parametrized"),
                "log": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066//console"
            },
            "name": "tier0",
            "recipients": [],
            "system": [
                {
                    "os": "",
                    "provider": ""
                }
            ],
            "artifact": {
                "nvr": "sip-4.19.7-3.el8+7",
                "scratch": "true",
                "component": "sip",
                "type": "brew-build",
                "id": 16869293,
                "issuer": "lbalhar"
            },
            "label": "",
            "note": [
                {
                    "check-conflicts": ("PASSED https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
                                        "ci-rpmdeplint/1066//artifact/rpmdeplint/logs/debug/x86_64/"
                                        "check-conflicts.out/*view*"),
                    "check-sat": ("PASSED https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
                                  "ci-rpmdeplint/1066//artifact/rpmdeplint/logs/debug/x86_64/check-sat.out/*view*"),
                    "check-upgrade": ("PASSED https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
                                      "ci-rpmdeplint/1066//artifact/rpmdeplint/logs/debug/x86_64/"
                                      "check-upgrade.out/*view*"),
                    "check-repoclosure": ("FAILED https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/"
                                          "ci-rpmdeplint/1066//artifact/rpmdeplint/logs/debug/x86_64/"
                                          "check-repoclosure.out/*view*")
                }
            ],
            "thread_id": "",
            "xunit": ""
        }
    }


class TestRPMDEPLINTCompleteChecksat(fedmsg.tests.test_meta.Base):
    """ `rpmdeplint <https://pagure.io/rpmdeplint>`_ tool finds errors in RPM packages in the context
    of their dependency graph.

    Messages (like the example given here) are published when an **rpmdeplint check-sat**
    task is **complete**.
    """
    expected_title = 'rpmdeplint.complete.check-sat'
    expected_link = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/'
    expected_subti = ('rpmdeplint check-sat PASSED for '
                      'component: sip-4.19.7-3.el8+7 with brew task_id: 16869293')
    expected_packages = set(['sip'])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1530068429.0,
        "msg_id": "ID:some-broker.com-41274-1529619027429-2:276082:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.rpmdeplint.complete.check-sat",
        "headers": {
            "content-length": "909",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "timestamp": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.rpmdeplint.complete.check-sat",
            "component": "sip",
            "nvr": "sip-4.19.7-3.el8+7",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "message-id": "ID:some-broker.com-41274-1529619027429-2:276082:0:0:1",
            "scratch": "true",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "brew-build",
            "id": "16869293",
            "issuer": "lbalhar"
        },
        "signature": None,
        "source_version": "0.9.0",
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
                "url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/",
                "rebuild": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/"
                            "/rebuild/parametrized"),
                "log": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/"
                        "/artifact/rpmdeplint/logs/debug/x86_64/check-sat.out/*view*")
            },
            "name": "tier0",
            "recipients": [],
            "system": [
                {
                    "os": "",
                    "provider": ""
                }
            ],
            "artifact": {
                "nvr": "sip-4.19.7-3.el8+7",
                "scratch": "true",
                "component": "sip",
                "type": "brew-build",
                "id": 16869293,
                "issuer": "lbalhar"
            },
            "label": "check-sat",
            "thread_id": "",
            "xunit": ""
        }
    }


class TestRPMDEPLINTCompleteCheckconflicts(fedmsg.tests.test_meta.Base):
    """ `rpmdeplint <https://pagure.io/rpmdeplint>`_ tool finds errors in RPM packages in the context
    of their dependency graph.

    Messages (like the example given here) are published when an **rpmdeplint check-conflicts**
    task is **complete**.
    """
    expected_title = 'rpmdeplint.complete.check-conflicts'
    expected_link = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/'
    expected_subti = ('rpmdeplint check-conflicts PASSED for '
                      'component: sip-4.19.7-3.el8+7 with brew task_id: 16869293')
    expected_packages = set(['sip'])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1530068429.0,
        "msg_id": "ID:some-broker.com-41274-1529619027429-2:276082:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.rpmdeplint.complete.check-conflicts",
        "headers": {
            "content-length": "909",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "timestamp": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.rpmdeplint.complete.check-conflicts",
            "component": "sip",
            "nvr": "sip-4.19.7-3.el8+7",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "message-id": "ID:some-broker.com-41274-1529619027429-2:276082:0:0:1",
            "scratch": "true",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "brew-build",
            "id": "16869293",
            "issuer": "lbalhar"
        },
        "signature": None,
        "source_version": "0.9.0",
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
                "url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/",
                "rebuild": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/"
                            "/rebuild/parametrized"),
                "log": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/"
                        "/artifact/rpmdeplint/logs/debug/x86_64/check-conflicts.out/*view*")
            },
            "name": "tier0",
            "recipients": [],
            "system": [
                {
                    "os": "",
                    "provider": ""
                }
            ],
            "artifact": {
                "nvr": "sip-4.19.7-3.el8+7",
                "scratch": "true",
                "component": "sip",
                "type": "brew-build",
                "id": 16869293,
                "issuer": "lbalhar"
            },
            "label": "check-conflicts",
            "thread_id": "",
            "xunit": ""
        }
    }


class TestRPMDEPLINTCompleteCheckrepoclosure(fedmsg.tests.test_meta.Base):
    """ `rpmdeplint <https://pagure.io/rpmdeplint>`_ tool finds errors in RPM packages in the context
    of their dependency graph.

    Messages (like the example given here) are published when an **rpmdeplint check-repoclosure**
    task is **complete**.
    """
    expected_title = 'rpmdeplint.complete.check-repoclosure'
    expected_link = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/'
    expected_subti = ('rpmdeplint check-repoclosure FAILED for '
                      'component: sip-4.19.7-3.el8+7 with brew task_id: 16869293')
    expected_packages = set(['sip'])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1530068429.0,
        "msg_id": "ID:some-broker.com-41274-1529619027429-2:276082:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.rpmdeplint.complete.check-repoclosure",
        "headers": {
            "content-length": "909",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "timestamp": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.rpmdeplint.complete.check-repoclosure",
            "component": "sip",
            "nvr": "sip-4.19.7-3.el8+7",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "message-id": "ID:some-broker.com-41274-1529619027429-2:276082:0:0:1",
            "scratch": "true",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "brew-build",
            "id": "16869293",
            "issuer": "lbalhar"
        },
        "signature": None,
        "source_version": "0.9.0",
        "msg": {
            "category": "sanity",
            "status": "FAILED",
            "ci": {
                "name": "RPM Factory",
                "url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com",
                "environment": "production",
                "team": "rpm-factory",
                "irc": "#rpm-factory",
                "email": "nobody@redhat.com"
            },
            "run": {
                "url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/",
                "rebuild": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/"
                            "/rebuild/parametrized"),
                "log": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/"
                        "/artifact/rpmdeplint/logs/debug/x86_64/check-repoclosure.out/*view*")
            },
            "name": "tier0",
            "recipients": [],
            "system": [
                {
                    "os": "",
                    "provider": ""
                }
            ],
            "artifact": {
                "nvr": "sip-4.19.7-3.el8+7",
                "scratch": "true",
                "component": "sip",
                "type": "brew-build",
                "id": 16869293,
                "issuer": "lbalhar"
            },
            "label": "check-repoclosure",
            "thread_id": "",
            "xunit": ""
        }
    }


class TestRPMDEPLINTCompleteCheckupgrades(fedmsg.tests.test_meta.Base):
    """ `rpmdeplint <https://pagure.io/rpmdeplint>`_ tool finds errors in RPM packages in the context
    of their dependency graph.

    Messages (like the example given here) are published when an **rpmdeplint check-upgrades**
    task is **complete**.
    """
    expected_title = 'rpmdeplint.complete.check-upgrades'
    expected_link = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/'
    expected_subti = ('rpmdeplint check-upgrades PASSED for '
                      'component: sip-4.19.7-3.el8+7 with brew task_id: 16869293')
    expected_packages = set(['sip'])
    expected_icon = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'
    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1530068429.0,
        "msg_id": "ID:some-broker.com-41274-1529619027429-2:276082:0:0:1",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.rpmdeplint.complete.check-upgrades",
        "headers": {
            "content-length": "909",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "timestamp": "0",
            "JMS_AMQP_NATIVE": "false",
            "destination": "/topic/VirtualTopic.eng.rpmdeplint.complete.check-upgrades",
            "component": "sip",
            "nvr": "sip-4.19.7-3.el8+7",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "message-id": "ID:some-broker.com-41274-1529619027429-2:276082:0:0:1",
            "scratch": "true",
            "JMS_AMQP_FirstAcquirer": "false",
            "type": "brew-build",
            "id": "16869293",
            "issuer": "lbalhar"
        },
        "signature": None,
        "source_version": "0.9.0",
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
                "url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/",
                "rebuild": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/"
                            "/rebuild/parametrized"),
                "log": ("https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-rpmdeplint/1066/"
                        "/artifact/rpmdeplint/logs/debug/x86_64/check-upgrades.out/*view*")
            },
            "name": "tier0",
            "recipients": [],
            "system": [
                {
                    "os": "",
                    "provider": ""
                }
            ],
            "artifact": {
                "nvr": "sip-4.19.7-3.el8+7",
                "scratch": "true",
                "component": "sip",
                "type": "brew-build",
                "id": 16869293,
                "issuer": "lbalhar"
            },
            "label": "check-upgrades",
            "thread_id": "",
            "xunit": ""
        }
    }

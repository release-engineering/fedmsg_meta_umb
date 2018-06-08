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
# Authors:  Giulia Naponiello <gnaponie@redhat.com>


import fedmsg.tests.test_meta
from .common import add_doc


class TestGreenwaveDecisionUpdateErrataNewFiles(fedmsg.tests.test_meta.Base):
    """ Greenwave is a service to decide whether a software artifact can
    pass certain gating points in a software delivery pipeline, based on test
    results stored in ResultsDB and waivers stored in WaiverDB.

    Greenwave publishes a message when a new result/waiver causes the
    decision to change.

    This decision is for Erratum moving to New Files state.
    """
    expected_title = 'greenwave.decision.update'
    expected_subti = ('greenwave is a GO on libXdmcp-1.1.2-9.el8 for '
                      '"errata_newfile_to_qe" (rhel-7)')
    expected_link = ('https://resultsdb.engineering.redhat.com/'
                     'results?item=libXdmcp-1.1.2-9.el8&type=koji_build')
    expected_packages = set(['libXdmcp'])
    expected_icon = (
        'https://datagrepper-prod-datanommer.int.open.paas.redhat.com/'
        'umb/_static/img/icons/greenwave.png')

    msg = {
        "i": 0,
        "username": "upshift",
        "timestamp": 1526649161.0,
        "msg_id": "2018-c50ff499-7573-4d7b-97de-45536096dfba",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.greenwave.decision.update",
        "headers": {
            "expires": "1527253961866",
            "timestamp": "1526649161866",
            "destination": "/topic/VirtualTopic.eng.greenwave.decision.update",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com"
                          "-36970-1526482715012-2:55604:-1:1:1267",
            "content-type": "text/plain",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.8.2",
        "msg": {
            "policies_satisfied": True,
            "decision_context": "errata_newfile_to_qe",
            "product_version": "rhel-7",
            "applicable_policies": [
                "1"
            ],
            "unsatisfied_requirements": [],
            "subject": [
                {
                    "item": "libXdmcp-1.1.2-9.el8",
                    "type": "koji_build"
                }
            ],
            "summary": "all required tests passed",
            "previous": {
                "policies_satisfied": False,
                "summary": "1 of 30 required test results missing",
                "unsatisfied_requirements": [
                    {
                        "testcase": "dist.rpmdiff.analysis.xml_validity",
                        "item": {
                            "item": "libXdmcp-1.1.2-9.el8",
                            "type": "koji_build"
                        },
                        "type": "test-result-missing",
                        "scenario": None
                    }
                ],
                "applicable_policies": [
                    "1"
                ]
            }
        }
    }


class TestGreenwaveDecisionUpdateComposeGate(fedmsg.tests.test_meta.Base):
    """ Greenwave is a service to decide whether a software artifact can
    pass certain gating points in a software delivery pipeline, based on test
    results stored in ResultsDB and waivers stored in WaiverDB.

    Greenwave publishes a message when a new result/waiver causes the
    decision to change.

    This decision is for compose gating.
    """
    expected_title = 'greenwave.decision.update'
    expected_subti = ('greenwave says NO-GO on libsemanage-2.8-2.el8+7 for '
                      '"osci_compose_gate" (rhel-8)')
    expected_link = ('https://resultsdb.engineering.redhat.com/'
                     'results?item=libsemanage-2.8-2.el8%2B7&type=brew-build')
    expected_packages = set(['libsemanage'])
    expected_icon = (
        'https://datagrepper-prod-datanommer.int.open.paas.redhat.com/'
        'umb/_static/img/icons/greenwave.png')

    msg = {
        "username": "upshift",
        "source_name": "datanommer",
        "certificate": None,
        "i": 39446,
        "timestamp": 1528403467.0,
        "msg_id": "2018-3337fe81-2e0b-4048-a963-068b34405205",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.greenwave.decision.update",
        "headers": {
            "expires": "1529008267689",
            "timestamp": "1528403467689",
            "destination": "/topic/VirtualTopic.eng.greenwave.decision.update",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com"
                          "-42045-1527890187852-2:112143:-1:1:1",
            "content-type": "text/plain",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.9.0",
        "msg": {
            "policies_satisfied": False,
            "decision_context": "osci_compose_gate",
            "product_version": "rhel-8",
            "applicable_policies": [
                "osci_compose"
            ],
            "unsatisfied_requirements": [
                {
                    "testcase": "osci.brew-build.tier0.functional",
                    "item": {
                        "item": "libsemanage-2.8-2.el8+7",
                        "type": "brew-build"
                    },
                    "result_id": 5036102,
                    "scenario": None,
                    "type": "test-result-failed"
                }
            ],
            "previous": {
                "summary": "1 of 1 required tests failed",
                "policies_satisfied": False,
                "unsatisfied_requirements": [
                    {
                        "testcase": "osci.brew-build.tier0.functional",
                        "item": {
                            "item": "libsemanage-2.8-2.el8+7",
                            "type": "brew-build"
                        },
                        "result_id": 5016237,
                        "scenario": None,
                        "type": "test-result-failed"
                    }
                ],
                "applicable_policies": [
                    "osci_compose"
                ]
            },
            "summary": "1 of 1 required tests failed",
            "subject": [
                {
                    "item": "libsemanage-2.8-2.el8+7",
                    "type": "brew-build"
                }
            ]
        }
    }


add_doc(locals())

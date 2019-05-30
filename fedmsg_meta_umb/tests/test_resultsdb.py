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
# Authors:  Ralph Bean <rbean@redhat.com>

import fedmsg.tests.test_meta
from .common import add_doc


class TestResultsDBNewGoodResult(fedmsg.tests.test_meta.Base):
    """ ResultsDB is a database for test results.

    This message gets published whenever resultsdb ingests a new result.
    """
    expected_title = 'resultsdb.result.new'
    expected_subti = ('resultsdb saw baseos-ci.brew-build.covscan.static-analysis PASSED for '
                      'foo-4.11.3-3400.el7')
    expected_link = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.com/job/ci-covscan/63806/'
    expected_agent = None
    expected_usernames = set([])
    expected_packages = set(['foo'])
    expected_icon = '_static/img/icons/resultsdb.png'

    msg = {
        "timestamp": 1529352189.0,
        "msg_id": "ID:messaging-devops-broker01.com-42045-1527890187852-2:346021:-1:1:1",
        "topic": "/topic/VirtualTopic.eng.resultsdb.result.new",
        "headers": {
            "expires": "1529956989165",
            "timestamp": "1529352189165",
            "destination": "/topic/VirtualTopic.eng.resultsdb.result.new",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2.com-...",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>"
        },
        "msg": {
            "testcase": {
                "ref_url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.com",
                "href": "https://resultsdb-api.engineering.com/api/v2.0/testcases/"
                "baseos-ci.brew-build.covscan.static-analysis",
                "name": "baseos-ci.brew-build.covscan.static-analysis"
            },
            "ref_url": "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.com/"
            "job/ci-covscan/63806/",
            "note": "",
            "href": "https://resultsdb-api.engineering.com/api/v2.0/results/5231886",
            "groups": ["d24e5ea3-7e88-4474-b0ad-360a0a26cf21"],
            "submit_time": "2018-06-18T20:03:08.233992",
            "outcome": "PASSED",
            "id": 5231886,
            "data": {
                "category": ["static-analysis"],
                "ci_team": ["Platform QE"],
                "brew_task_id": ["16769734"],
                "ci_environment": ["None"],
                "scratch": ["True"],
                "component": ["rpm"],
                "ci_email": ["platform-ci@com"],
                "ci_name": ["Platform CI"],
                "item": ["foo-4.11.3-3400.el7"],
                "system_provider": ["None"],
                "ci_irc": ["#baseosci"],
                "type": ["brew-build"],
                "system_os": ["None"],
                "issuer": ["pmoravco"],
                "ci_url": ["https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.com"],
                "log": [
                    "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.com/job/ci-covscan/63806/console"
                ],
                "rebuild": [
                    "https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.com/job/ci-covscan/63806/rebuild/parameterized"
                ],
            },
        }
    }


class TestLegacyResultsDBNewGoodResult(fedmsg.tests.test_meta.Base):
    """ ResultsDB is a database for test results.

    This message gets published whenever resultsdb ingests a new result.
    """
    expected_title = 'resultsdb.result.new'
    expected_subti = (
        'resultsdb saw dist.rpmdiff.analysis.patches FAILED for '
        'qpid-dispatch-1.0.0-5.el6')
    expected_link = 'https://rpmdiff.engineering.redhat.com/run/185690/17'
    expected_agent = None
    expected_usernames = set([])
    expected_packages = set(['qpid-dispatch'])
    expected_icon = '_static/img/icons/resultsdb.png'

    msg = {
        "headers": {
            "destination": "/topic/VirtualTopic.eng.resultsdb.result.new",
            "message-id": "ID:messaging-devops-broker01.dev1.ext.devlab."
            "redhat.com-44807-1512072391381-3:1811626:-1:1:1",
            "priority": "4",
            "timestamp": "1514930340914"
        },
        "i": 0,
        "msg": {
            "result": {
                "id": 2854980,
                "log_url": "https://rpmdiff.engineering.redhat.com/"
                "run/185690/17",
                "outcome": "FAILED",
                "prev_outcome": None,
                "submit_time": "2018-01-02 21:58:58 UTC"
            },
            "task": {
                "item": "qpid-dispatch-1.0.0-5.el6",
                "name": "dist.rpmdiff.analysis.patches",
                "type": "koji_build"
            }
        },
        "msg_id": "ID:messaging-devops-broker01.dev1.ext.devlab.redhat."
        "com-44807-1512072391381-3:1811626:-1:1:1",
        "signature": None,
        "source_name": "datanommer",
        "source_version": "0.8.2",
        "timestamp": 1514930340.0,
        "topic": "/topic/VirtualTopic.eng.resultsdb.result.new",
        "username": None
    }


class TestLegacyResultsDBNewMalformedResult(fedmsg.tests.test_meta.Base):
    """ Test handling an oddly formed result. """
    nodoc = True  # Don't include this one in the docs.

    expected_title = 'resultsdb.result.new'
    expected_subti = ('resultsdb saw dist.rpmdiff.analysis.patches FAILED for '
                      'something')
    expected_link = ('https://resultsdb-api.engineering.redhat.com/api/v2.0/'
                     'results/2854980')
    expected_agent = None
    expected_usernames = set([])
    expected_packages = set([])
    expected_icon = '_static/img/icons/resultsdb.png'

    msg = {
        "headers": {
            "destination": "/topic/VirtualTopic.eng.resultsdb.result.new",
            "message-id": "ID:messaging-devops-broker01.dev1.ext.devlab."
            "redhat.com-44807-1512072391381-3:1811626:-1:1:1",
            "priority": "4",
            "timestamp": "1514930340914"
        },
        "i": 0,
        "msg": {
            "result": {
                "id": 2854980,
                "outcome": "FAILED",
                "prev_outcome": None,
                "submit_time": "2018-01-02 21:58:58 UTC"
            },
            "task": {
                "name": "dist.rpmdiff.analysis.patches",
            }
        },
        "msg_id": "ID:messaging-devops-broker01.dev1.ext.devlab.redhat."
        "com-44807-1512072391381-3:1811626:-1:1:1",
        "signature": None,
        "source_name": "datanommer",
        "source_version": "0.8.2",
        "timestamp": 1514930340.0,
        "topic": "/topic/VirtualTopic.eng.resultsdb.result.new",
        "username": None
    }


add_doc(locals())

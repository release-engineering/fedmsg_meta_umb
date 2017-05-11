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

class TestRPMDiffComparisonStart(fedmsg.tests.test_meta.Base):
    """ The RPMDiff system performs analyses of rpms.

    Messages (like the example given here) are published when an **comparison**
    job is **starting**.  (A comparison job compares one rpm against a baseline
    rpm).
    """
    expected_title = 'rpmdiff.job.starting'
    expected_subti = ('rpmdiff comparison of openshift-ansible is starting '
                      '(3.6.65.2-1.git.0.1a149c1.el7 against '
                      '3.6.65.1-1.git.0.1f50797.el7)')
    expected_link = 'https://rpmdiff.engineering.redhat.com/run/94269/'
    expected_packages = set(['openshift-ansible'])
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "i": 0,
        "msg": {
            "baseline": "openshift-ansible-3.6.65.1-1.git.0.1f50797.el7",
            "errata_id": None,
            "nvr": "openshift-ansible-3.6.65.2-1.git.0.1a149c1.el7",
            "overall_score": None,
            "package_name": "openshift-ansible",
            "run_id": 94269,
            "source": "RPMDIFF",
            "type": "COMPARISON",
        },
        "msg_id": "ID\\csomebroker-32888-1493960489068-4\\c151703\\c0\\c0\\c1",
        "source_name": "datanommer",
        "source_version": "0.7.0",
        "timestamp": 1494464909.0,
        "topic": "/topic/VirtualTopic.eng.rpmdiff.job.starting",
        "username": None,
    }


class TestRPMDiffAnalysisCompleted(fedmsg.tests.test_meta.Base):
    """ The RPMDiff system performs analyses of rpms.

    Messages (like the example given here) are published when an **analysis**
    job is **completed**.  (An analysis job operates on a single rpm).
    """

    expected_title = 'rpmdiff.job.completed'
    expected_subti = ('rpmdiff analysis of openshift-ansible-3.6.65.2-1'
                      '.git.0.1a149c1.el7 is completed')
    expected_link = 'https://rpmdiff.engineering.redhat.com/run/94268/'
    expected_packages = set(['openshift-ansible'])
    expected_icon = ('https://errata.devel.redhat.com/assets/'
                     'images/erratatool18.png')
    msg = {
        "username": None,
        "i": 0,
        "timestamp": 1494464973.0,
        "msg_id": "ID\\cbrokerbroker-32888-1493960489068-4\\c151704\\c0\\c0\\c1",
        "topic": "/topic/VirtualTopic.eng.rpmdiff.job.completed",
        "msg": {
            "errata_id": None,
            "baseline": None,
            "package_name": "openshift-ansible",
            "run_id": 94268,
            "source": "RPMDIFF",
            "type": "ANALYSIS",
            "overall_score": "Needs inspection",
            "nvr": "openshift-ansible-3.6.65.2-1.git.0.1a149c1.el7"
        }
    }

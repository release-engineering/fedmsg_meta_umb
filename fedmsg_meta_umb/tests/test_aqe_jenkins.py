# Copyright (C) 2019 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Wai Cheang <wcheang@redhat.com>

import fedmsg.tests.test_meta
from .common import add_doc


class TestAqeJenkins(fedmsg.tests.test_meta.Base):
    """ Retrobob is a service that runs another tool, retrodep, to generate
    source manifest from dist-git content. It publishes retrodep run results
    to UMB.
    """
    expected_title = "aqe-jenkins.retrobob.result"
    expected_subti = (
        "retrodep run on build osbs-test-sandwich-container was met with "
        "success")
    expected_icon = "_static/img/icons/jenkins.png"
    msg = {
        "i": 0,
        "msg_id": "ID:pnt-devops-rad-stage-jenkins.rhev-ci-vms.eng.rdu2.redhat.com-44328-1560142882813-1701:1:1:1:1",
        "topic": "/topic/VirtualTopic.eng.aqe-jenkins.retrobob.result",
        "timestamp": 1560399981.0,
        "msg": {
            "build_id": 1719121,
            "manifest_path": "rh-manifest.txt",
            "name": "osbs-test-sandwich-container",
            "nvr": "osbs-test-sandwich-container-1.0.go.module.metadata-198",
            "result": "success",
            "source": "git://dist-git.host.stage.eng.bos.redhat.com/containers/osbs-test-sandwich#test-sources",
            "source_tag": "osbs-test-sandwich-container-1.0.go.module.metadata-198-sources",
            "version": "1.0.go.module.metadata"
        },
        "headers": {
            "CI_NAME": "retrobob-dev",
            "CI_TYPE": "custom",
            "JMSXUserID": "msg-aqe-jenkins",
            "amq6100_destination": "queue://Consumer.client-datanommer.upshift-stage.VirtualTopic.eng.>",
            "amq6100_originalDestination": "topic://VirtualTopic.eng.aqe-jenkins.retrobob.result",
            "correlation-id": "ee691c02-0e29-44e3-be42-314f7ea2a60a",
            "destination": "/topic/VirtualTopic.eng.aqe-jenkins.retrobob.result",
            "expires": "1560486381829",
            "message-id": "ID:pnt-devops-rad-stage-jenkins.rhev-ci-vms.eng.rdu2.redhat.com-44328",
            "original-destination": "/topic/VirtualTopic.eng.aqe-jenkins.retrobob.result",
            "persistent": "true",
            "priority": "4",
            "service": "RetroBob",
            "subscription": "/queue/Consumer.client-datanommer.upshift-stage.VirtualTopic.eng.>",
            "timestamp": "1560399981829",
            "type": "application/json"
        },
    }


add_doc(locals())

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
# Authors: Yukin Chan <yuqchen@redhat.com>

import fedmsg.tests.test_meta

class TestCIComplete(fedmsg.tests.test_meta.Base):
    """ `Engineering CI Automation System performs tests to ensure the quality
    of virtualization packages automatically.

    Messages (like the example given here) are published when an **CI**
    job is **completed**.
    """
    msg = {
        "username": "null",
        "source_name": "datanommer",
        "certificate": "null",
        "i": 0,
        "timestamp": 1530670930,
        "msg_id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-41274-1529619027429-3:231921:-1:1:1",
        "crypto": "null",
        "topic": "/topic/VirtualTopic.eng.ci.brew-build.test.complete",
        "headers": {
            "content-length": "918",
            "expires": "1531275730696",
            "nvr": "libvirt-4.5.0-1.el7",
            "scratch": "False",
            "destination": "/topic/VirtualTopic.eng.ci.brew-build.test.complete",
            "component": "libvirt",
            "priority": "4",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-prod.VirtualTopic.eng.>",
            "timestamp": "1530670930696",
            "message-id": "ID:messaging-devops-broker01.web.prod.ext.phx2.redhat.com-41274-1529619027429-3:231921:-1:1:1",
            "type": "brew-build",
            "id": "16976169",
            "issuer": "jdenemar"
        },
        "signature": "null",
        "source_version": "0.9.0",
        "msg": {
            "category": "functional",
            "status": "failed",
            "ci": {
                "url": "https://libvirt-jenkins.rhev-ci-vms.eng.rdu2.redhat.com",
                "team": "Libvirt QE",
                "irc": "#libvirt-auto",
                "email": "gsun@redhat.com",
                "name": "Libvirt CI"
            },
            "run": {
                "url": "https://libvirt-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/libvirt-RHEL-7.6-runtest-x86_64-function-migration/9/#rhev",
                "log": "http://qed.lab.eng.pek2.redhat.com/test-results/testresult/e23871e8-7f30-11e8-b238-0a580a8101fd"
            },
            "namespace": "libvirt-ci",
            "system": {
                "os": "RHEL7.6",
                "provider": "beaker"
            },
            "artifact": {
                "nvr": "libvirt-4.5.0-1.el7",
                "scratch": "false",
                "component": "libvirt",
                "type": "brew-build",
                "id": "16976169",
                "issuer": "jdenemar"
            },
            "note": "Submit by Metadash",
            "type": "official"
        }
    }
    expected_title = 'CI Test Job complete'
    expected_link = ('https://libvirt-jenkins.rhev-ci-vms.eng.rdu2.redhat.com'
                     '/job/libvirt-RHEL-7.6-runtest-x86_64-function-migration'
                     '/9/#rhev')
    expected_subti = 'Test job for \"libvirt-4.5.0-1.el7\" complete'
    expected_packages = set(['libvirt'])
    expected_icon = None

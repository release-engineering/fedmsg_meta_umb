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
# Authors:  Mike Bonnet <mikeb@redhat.com>

import fedmsg.tests.test_meta
from .common import add_doc


class TestDistGit(fedmsg.tests.test_meta.Base):
    """ The Dist-Git system manages collections of git repositories.

    Messages are published every time one or more commits are pushed to a repo.
    """
    expected_title = 'distgit.commit'
    expected_subti = '42bcbca2 was committed on the rhel-7.4 branch of the rpcbind rpm repo by steved'
    expected_link = ('https://pkgs.devel.redhat.com/cgit/rpms/rpcbind/commit/'
                     '?h=rhel-7.4&id=42bcbca202b35ae663bdbca9e10b64d4a5dfbf5a')
    expected_packages = set(['rpcbind'])
    expected_icon = 'https://git-scm.com/images/logos/downloads/Git-Icon-Black.png'
    expected_usernames = set(['steved'])
    expected_agent = 'steved'

    msg = {
        "i": 0,
        "timestamp": 1494525626.0,
        "msg_id": ("ID\\cmessaging-devops-broker01.web.prod.ext.phx2.redhat.com-32888-"
                   "1493960489068-4\\c171881\\c0\\c0\\c1"),
        "topic": "/topic/VirtualTopic.eng.distgit.commit",
        "headers": {
            "username": "steved",
            "repo": "rpcbind",
            "content-length": "666",
            "expires": "0",
            "rev": "42bcbca202b35ae663bdbca9e10b64d4a5dfbf5a",
            "destination": "/topic/VirtualTopic.eng.distgit.commit",
            "namespace": "rpms",
            "agent": "steved",
            "subscription": "/queue/Consumer.datanommer-dev-mikeb.VirtualTopic.eng.>",
            "message-id": ("ID\\cmessaging-devops-broker01.web.prod.ext.phx2.redhat.com-32888-"
                           "1493960489068-4\\c171881\\c0\\c0\\c1"),
            "timestamp": "0",
            "branch": "rhel-7.4",
            "seen": "false",
            "path": "/srv/git/rpms/rpcbind.git",
            "email": "steved@redhat.com",
            "name": "Steve Dickson"
        },
        "msg": {
            "username": "steved",
            "stats": {
                "files": {
                    "rpcbind-0.2.0-memleaks.patch": {
                        "deletions": 0,
                        "additions": 177,
                        "lines": 177
                    },
                    "rpcbind.spec": {
                        "deletions": 2,
                        "additions": 8,
                        "lines": 10
                    }
                },
                "total": {
                    "deletions": 2,
                    "files": 2,
                    "additions": 185,
                    "lines": 187
                }
            },
            "name": "Steve Dickson",
            "rev": "42bcbca202b35ae663bdbca9e10b64d4a5dfbf5a",
            "namespace": "rpms",
            "agent": "steved",
            "summary": "Fixed memory leaks (bz 1449456)",
            "repo": "rpcbind",
            "branch": "rhel-7.4",
            "seen": False,
            "path": "/srv/git/rpms/rpcbind.git",
            "message": ("Fixed memory leaks (bz 1449456)\n\nSigned-off-by: Steve Dickson <steved@redhat.com>\n"
                        "Resolves: bz1449456\n"),
            "email": "steved@redhat.com"
        }
    }


add_doc(locals())

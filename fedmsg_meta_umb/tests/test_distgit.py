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


class TestDistGitCommit(fedmsg.tests.test_meta.Base):
    """ The Dist-Git system manages collections of git repositories.

    A commit message is published for every commit that is pushed to a repo.
    """
    expected_title = 'distgit.commit'
    expected_subti = '42bcbca2 was committed on the rhel-7.4 branch of the rpcbind rpm repo by steved'
    expected_link = ('https://pipeline.engineering.redhat.com/distgitcommit/'
                     '42bcbca202b35ae663bdbca9e10b64d4a5dfbf5a')
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


class TestDistGitPushSingle(fedmsg.tests.test_meta.Base):
    """ The Dist-Git system manages collections of git repositories.

    A push message is published for every branch updated by a "git push".
    This is a message representing a push which updates a branch with a single commit.
    """
    expected_title = 'distgit.push'
    expected_subti = '1 commit was pushed to the rhel-8.0 branch of the httpd rpm repo by mikeb'
    expected_link = 'https://pkgs.devel.redhat.com/cgit/rpms/httpd/log/?h=rhel-8.0'
    expected_packages = set(['httpd'])
    expected_icon = 'https://git-scm.com/images/logos/downloads/Git-Icon-Black.png'
    expected_usernames = set(['mikeb'])
    expected_agent = 'mikeb'

    msg = {
        "i": 0,
        "timestamp": 1521512774.0,
        "msg_id": "ID:messaging-devops-broker01.web.stage.ext.phx2.redhat.com-34380-1520940284355-18:52484:0:0:1",
        "topic": "/topic/VirtualTopic.eng.distgit.push",
        "headers": {
            "oldrev": "0000000000000000000000000000000000000000",
            "repo": "httpd",
            "content-length": "312",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "username": "mikeb",
            "destination": "/topic/VirtualTopic.eng.distgit.push",
            "namespace": "rpms",
            "newrev": "9d3d09ed37b4450bbff8c45527a7d75297626633",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker01.web.stage.ext.phx2.redhat.com-"
            "34380-1520940284355-18:52484:0:0:1",
            "numcommits": "1",
            "branch": "rhel-8.0",
            "timestamp": "0",
            "path": "/srv/git/rpms/httpd.git",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-stage.VirtualTopic.eng.>"
        },
        "msg": {
            "oldrev": "0000000000000000000000000000000000000000",
            "username": "mikeb",
            "newrev": "9d3d09ed37b4450bbff8c45527a7d75297626633",
            "commits": [
                "9d3d09ed37b4450bbff8c45527a7d75297626633"
            ],
            "namespace": "rpms",
            "repo": "httpd",
            "numcommits": 1,
            "branch": "rhel-8.0",
            "path": "/srv/git/rpms/httpd.git"
        }
    }


class TestDistGitPushMultiple(fedmsg.tests.test_meta.Base):
    """ The Dist-Git system manages collections of git repositories.

    A push message is published for every branch updated by a "git push".
    This is a message representing a push which updates a branch with multiple commits.
    """
    expected_title = 'distgit.push'
    expected_subti = '3 commits were pushed to the rhel-7.5 branch of the ntp rpm repo by mikeb'
    expected_link = 'https://pkgs.devel.redhat.com/cgit/rpms/ntp/log/?h=rhel-7.5'
    expected_packages = set(['ntp'])
    expected_icon = 'https://git-scm.com/images/logos/downloads/Git-Icon-Black.png'
    expected_usernames = set(['mikeb'])
    expected_agent = 'mikeb'

    msg = {
        "i": 0,
        "timestamp": 1521513184.0,
        "msg_id": "ID:messaging-devops-broker01.web.stage.ext.phx2.redhat.com-34380-1520940284355-18:52505:0:0:1",
        "topic": "/topic/VirtualTopic.eng.distgit.push",
        "headers": {
            "oldrev": "9d3d09ed37b4450bbff8c45527a7d75297626633",
            "repo": "ntp",
            "content-length": "356",
            "expires": "0",
            "JMS_AMQP_MESSAGE_FORMAT": "0",
            "JMS_AMQP_NATIVE": "false",
            "username": "mikeb",
            "destination": "/topic/VirtualTopic.eng.distgit.push",
            "namespace": "rpms",
            "newrev": "b904064468acb97fe0a7a00165979d19a462ec0b",
            "priority": "4",
            "message-id": "ID:messaging-devops-broker01.web.stage.ext.phx2.redhat.com-"
            "34380-1520940284355-18:52505:0:0:1",
            "numcommits": "3",
            "branch": "rhel-7.5",
            "timestamp": "0",
            "path": "/srv/git/rpms/ntp.git",
            "JMS_AMQP_FirstAcquirer": "false",
            "subscription": "/queue/Consumer.client-datanommer.openpaas-stage.VirtualTopic.eng.>"
        },
        "msg": {
            "oldrev": "9d3d09ed37b4450bbff8c45527a7d75297626633",
            "username": "mikeb",
            "newrev": "b904064468acb97fe0a7a00165979d19a462ec0b",
            "commits": [
                "b426cb95170fc4308828f640a75975410771c7af",
                "a0f167a36048c77f84c57507873995614ce07bc8",
                "b904064468acb97fe0a7a00165979d19a462ec0b"
            ],
            "namespace": "rpms",
            "repo": "ntp",
            "numcommits": 3,
            "branch": "rhel-7.5",
            "path": "/srv/git/rpms/ntp.git"
        }
    }


add_doc(locals())

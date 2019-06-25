# Copyright (C) 2019 Red Hat, Inc.
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
# Authors:  Tomas Kopecek <tkopecek@redhat.com>

from . import test_brew
from .common import add_doc

class TestBrewKojiraExpired(test_brew.BrewBase):
    expected_state = 'open'
    expected_subti = 'tag rhos-16.0-rhel-8-trunk-image-build was expired for 30 seconds'
    expected_link = 'https://brewweb.engineering.redhat.com/brew/taskinfo?taskID=22335794'
    msg = {
        "i": 0,
        "msg_id": "47f15511-549c-4fc1-b6cd-738d4e1995bc",
        "topic": "/topic/VirtualTopic.eng.brew.kojira.expired",
        "msg": {
            "seconds": 30,
            "tag": "rhos-16.0-rhel-8-trunk-image-build",
            "tag_id": 21700,
            "task_id": 22335794,
            "type": "RepoExpired"
        },
    }


add_doc(locals())

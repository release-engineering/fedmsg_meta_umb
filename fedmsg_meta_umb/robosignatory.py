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

from fedmsg.meta.base import BaseProcessor


class RobosignatoryProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = "robosignatory"
    __description__ = "RAD Auto-Signing Service"
    __link__ = "https://mojo.redhat.com/docs/DOC-1131189"
    __docs__ = "https://mojo.redhat.com/docs/DOC-1131189"
    __obj__ = "Signing Events"

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        if msg['topic'].endswith('robosignatory.container.sign'):
            tmpl = self._("robosignatory's attempt to sign the {repo} "
                          "container with {sig_key_id} was met "
                          "with {signing_status}")
            return tmpl.format(**msg['msg'])

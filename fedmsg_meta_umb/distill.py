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


class DistillProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = "distill"
    __description__ = "The Compose Tool"
    __link__ = "https://pagure.io/pungi"
    __docs__ = "https://pagure.io/pungi"
    __obj__ = "Composes"

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        compose = msg['msg']['compose-id']
        if msg['topic'].endswith('distill.compose-finished'):
            statuses = {
                'FINISHED': self._('just finished'),
                'DOOMED': self._('failed in a horrible fire'),
            }
            status = msg['msg']['compose-state']
            status = statuses.get(status) or status
            tmpl = self._("distill compose of {compose} {status}")
            return tmpl.format(compose=compose, status=status)
        elif msg['topic'].endswith('distill.compose-started'):
            tmpl = self._("distill compose of {compose} started")
            return tmpl.format(compose=compose)

    def link(self, msg, **config):
        if 'compose-path' in msg['msg']:
            location = msg['msg']['compose-path'].rstrip('/').rstrip('/compose')
            if not location.startswith('http'):
                base = 'http://download.lab.bos.redhat.com'
                prefix = '/mnt/redhat'
                return base + location[len(prefix):]
            return location

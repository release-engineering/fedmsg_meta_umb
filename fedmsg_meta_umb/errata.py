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


class ErrataProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'errata'
    __description__ = 'the Errata Tool'
    __link__ = 'https://errata.devel.redhat.com/'
    __docs__ = 'https://errata.devel.redhat.com/user-guide/'
    __obj__ = 'errata events'
    __icon__ = ('https://errata.devel.redhat.com/assets/'
                'images/erratatool18.png')

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        headers = msg['headers']
        title = self.title(msg, **config)
        if title.endswith('activity.status'):
            template = self._("{agent} moved {fulladvisory} "
                              "from {from} "
                              "to {to}")
            return template.format(agent=self.agent(msg, **config), **headers)

    def agent(self, msg, **config):
        return msg['headers']['who'].split('@')[0]

    def usernames(self, msg, **config):
        return set([self.agent(msg, **config)])

    def link(self, msg, **config):
        template = 'https://errata.devel.redhat.com/advisory/{errata_id}'
        return template.format(**msg['headers'])

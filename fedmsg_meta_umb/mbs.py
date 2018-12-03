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


class MBSProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'mbs'
    __description__ = 'the Module Build Service'
    __link__ = 'https://mbs.engineering.redhat.com'
    __docs__ = 'https://gitlab.cee.redhat.com/rhel-appstream/module-maintainer-guide'
    __obj__ = 'Module Builds'
    __icon__ = '/umb/_static/img/icons/mbs.png'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        tmpl = self._('{owner}\'s build of {name}-{stream} transitioned '
                      'to the "{state_name}" state.')
        return tmpl.format(**msg['msg'])

    def link(self, msg, **config):
        idx = msg['msg']['id']
        return 'http://mbsweb.engineering.redhat.com/module/%i' % idx

    def usernames(self, msg, **config):
        return set([msg['msg']['owner']])

    def packages(self, msg, **config):
        return set([msg['msg']['name']])

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
# Authors:  Mike Bonnet <mikeb@redhat.com>

from fedmsg.meta.base import BaseProcessor


class RepotrackerProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'repotracker'
    __description__ = 'repotracker'
    __link__ = 'https://github.com/release-engineering/repotracker'
    __docs__ = 'https://github.com/release-engineering/repotracker'
    __obj__ = 'repotracker'
    __icon__ = '_static/img/icons/repotracker.png'

    subtitle_templates = {
        'repotracker.container.tag.added':
        '{tag} tag was added to the {reponame} container repository',
        'repotracker.container.tag.updated':
        '{tag} tag was updated in the {reponame} container repository',
        'repotracker.container.tag.removed':
        '{tag} tag was removed from the {reponame} container repository',
    }

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        tmpl = self.subtitle_templates.get(self.title(msg, **config))
        if tmpl:
            return tmpl.format(**msg['headers'])

    def link(self, msg, **config):
        return 'https://' + msg['headers']['repo']

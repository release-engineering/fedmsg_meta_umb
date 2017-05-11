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


class RPMDiffProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'rpmdiff'
    __description__ = 'the rpmdiff analysis system'
    __link__ = 'https://rpmdiff.engineering.redhat.com'
    __docs__ = 'https://mojo.redhat.com/docs/DOC-1085683'
    __obj__ = 'RPMDiff Analysis System'
    __icon__ = ('https://errata.devel.redhat.com/assets/'
                'images/erratatool18.png')

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        action = self.title(msg, **config).split('.')[-1]
        if msg['msg']['type'] == 'COMPARISON':
            kwargs = dict(
                action=action,
                package=msg['msg']['package_name'],
                baseline='-'.join(msg['msg']['baseline'].rsplit('-', 2)[1:]),
                target='-'.join(msg['msg']['nvr'].rsplit('-', 2)[1:]),
            )
            template = ('rpmdiff comparison of {package} is {action} '
                        '({target} against {baseline})')
            return template.format(**kwargs)
        elif msg['msg']['type'] == 'ANALYSIS':
            kwargs = dict(action=action, nvr=msg['msg']['nvr'])
            template = 'rpmdiff analysis of {nvr} is {action}'
            return template.format(**kwargs)

    def packages(self, msg, **config):
        return set([msg['msg']['package_name']])

    def link(self, msg, **config):
        template = 'https://rpmdiff.engineering.redhat.com/run/{run_id}/'
        return template.format(**msg['msg'])

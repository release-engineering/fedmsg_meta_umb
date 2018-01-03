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

from fedmsg.meta.base import BaseProcessor, BaseConglomerator


class PubProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'pub'
    __description__ = 'the software publication system'
    __link__ = 'https://pub.devel.redhat.com'
    __docs__ = 'https://pub.devel.redhat.com/pub/docs/index.html'
    __obj__ = 'Publish Events'
    __icon__ = ('https://errata.devel.redhat.com/assets/'
                'images/erratatool18.png')

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        if self.title(msg, **config) == 'pub.container.sign':
            template = self._("image {0} "
                              "was signed with key {1} in {2}")
            return template.format(msg['msg']['image_name'],
                                   msg['msg']['sig_key_id'].lower(),
                                   msg['headers'].get('target', '"unspecified"'))
        template = self._("{agent}'s {source} push to {target} "
                          "of {files} {status}")
        items = [item.split('/')[-1] for item in msg['msg']['file_list']]
        files = BaseConglomerator.list_to_series(items)
        status_lookup = {
            'OPEN': self._('just started'),
            'CLOSED': self._('completed successfully'),
            'FAILED': self._('failed'),
        }
        unhandled_status = self._('entered an unknown state')
        status = status_lookup.get(msg['msg']['state'], unhandled_status)
        agent = self.agent(msg, **config) or self._('unknown')
        return template.format(
            files=files,
            status=status,
            agent=agent,
            **msg['msg'])

    def link(self, msg, **config):
        if self.title(msg, **config) == 'pub.container.sign':
            template = 'http://pub.devel.redhat.com/pub/task/{0}/'
            return template.format(msg['msg']['pub_task_id'])
        return msg['msg']['push_url']

    def usernames(self, msg, **config):
        users = set()
        if msg['msg'].get('pushed_by'):
            users.add(msg['msg']['pushed_by'].split('@')[0])
        if msg['msg'].get('owner'):
            users.add(msg['msg']['owner'].split('@')[0])
        return users

    def agent(self, msg, **config):
        if msg['msg'].get('pushed_by'):
            return msg['msg']['pushed_by'].split('@')[0]
        if msg['msg'].get('owner'):
            return msg['msg']['owner'].split('@')[0]

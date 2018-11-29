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


class ODCSProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'odcs'
    __description__ = 'the On-Demand Compose Service'
    __link__ = 'https://odcs.engineering.redhat.com'
    __docs__ = 'https://pagure.io/odcs'
    __icon__ = '/umb/_static/img/icons/odcs.png'
    __obj__ = 'ODCS composes'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        topic = msg['topic']

        if topic.endswith('odcs.state.change'):
            usernames = self.usernames(msg, **config)
            agent = next(iter(usernames)) if usernames else None

            template = self._('{agent}\'s compose of {source} '
                              'transitioned to {state_name}.')
            return template.format(agent=agent, **msg['msg']['compose'])
        else:
            return 'Unknown message.'

    def link(self, msg, **config):
        if 'compose' in msg['msg']:
            if 'result_repofile' in msg['msg']['compose']:
                return msg['msg']['compose']['result_repofile']

    def usernames(self, msg, **config):
        usernames = set()
        if 'compose' in msg['msg']:
            if 'owner' in msg['msg']['compose']:
                owner = self._format_username(msg['msg']['compose']['owner'])
                usernames.add(owner)
        return usernames

    @staticmethod
    def _format_username(username):
        # For ldap-format strings
        username = username.split(',')[0]
        if username.startswith('UID='):
            username = username[4:]
        # For krb service principals
        username = username.split('/')[0]
        return username

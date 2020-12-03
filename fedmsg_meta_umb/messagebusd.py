# Copyright (C) 2020 Red Hat, Inc.
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


class MessagebusdProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.devops'

    __name__ = 'messagebusd'
    __description__ = 'Daemon for executing arbitrary code based on messages received' \
        ' from the Unified Message Bus'
    __link__ = 'https://gitlab.cee.redhat.com/devops/messagebusd'
    __docs__ = 'https://docs.engineering.redhat.com/display/EXD/messagebusd'
    __obj__ = 'messagebusd events'
    __icon__ = '_static/img/icons/umb.png'

    subtitle_templates = {
        'messagebusd.task-repo': 'repo requested for task {task_id}',
        'messagebusd.static-repo-regen': 'static repo regen requested for tag {tag}',
        'messagebusd.stage-mw-release': 'staging requested for release {release}',
    }

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def _suffix(self, text, headers):
        if headers.get('umbproxy_username'):
            return '{} by {} via umbproxy'.format(text, headers['umbproxy_username'])
        elif headers.get('user') and headers['user'] != 'null':
            return '{} by {}'.format(text, headers['user'])
        elif headers.get('JMSXUserID'):
            return '{} by client {}'.format(text, headers['JMSXUserID'])
        else:
            return text

    def subtitle(self, msg, **config):
        headers = msg['headers']
        body = msg['msg']
        tmpl = self.subtitle_templates.get(self.title(msg, **config))
        if tmpl:
            return self._suffix(tmpl.format(**body), headers)
        elif 'message' in body:
            return body['message']
        else:
            return None

    def link(self, msg, **config):
        body = msg['msg']
        if 'task_id' in body:
            return 'https://brewweb.engineering.redhat.com/brew/taskinfo?taskID={}'.format(body['task_id'])
        elif 'tag' in body:
            return 'https://brewweb.engineering.redhat.com/brew/taginfo?tagID={}'.format(body['tag'])
        elif '.umbproxy.' in msg['topic']:
            return 'https://umbproxy.engineering.redhat.com/'
        else:
            return None

    def agent(self, msg, **config):
        headers = msg['headers']
        if headers.get('umbproxy_username'):
            return headers['umbproxy_username'].split('@')[0].split('/')[0]
        elif headers.get('user') and headers['user'] != 'null':
            return headers['user']
        else:
            return None

    def usernames(self, msg, **config):
        persons = set()
        agent = self.agent(msg, **config)
        if agent:
            persons.add(agent)
        return persons

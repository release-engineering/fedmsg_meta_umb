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
# Authors:  Ralph Bean <rbean@redhat.com>

from fedmsg.meta.base import BaseProcessor


class ResultsDBProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'resultsdb'
    __description__ = 'ResultsDB'
    __link__ = 'https://resultsdb.engineering.redhat.com'
    __docs__ = 'https://mojo.redhat.com/docs/DOC-1131637'
    __obj__ = 'Results'
    __icon__ = '/umb/_static/img/icons/resultsdb.png'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        # New format
        if msg['topic'].endswith('resultsdb.result.new') and 'data' in msg['msg']:
            name = msg['msg'].get('testcase', {}).get('name', 'unknown')
            status = msg['msg'].get('outcome', 'unknown')
            item = msg['msg'].get('data', {}).get('item')
            item = item[0] if item else 'something'
            tmpl = self._('resultsdb saw {name} {status} for {item}')
            return tmpl.format(name=name, status=status, item=item)
        # Old format
        if msg['topic'].endswith('resultsdb.result.new') and 'task' in msg['msg']:
            name = msg['msg'].get('task', {}).get('name', 'unknown')
            status = msg['msg'].get('result', {}).get('outcome', 'unknown')
            item = msg['msg'].get('task', {}).get('item', 'something')
            tmpl = self._('resultsdb saw {name} {status} for {item}')
            return tmpl.format(name=name, status=status, item=item)

    def link(self, msg, **config):
        try:
            return msg['msg']['ref_url']
        except KeyError:
            pass

        # Old format
        try:
            return msg['msg']['result']['log_url']
        except KeyError:
            pass

        try:
            tmpl = (
                'https://resultsdb-api.engineering.redhat.com/'
                'api/v2.0/results/%s')
            idx = msg['msg']['result']['id']
            return tmpl % idx
        except KeyError:
            pass

    def packages(self, msg, **config):
        # New format
        kind = msg['msg'].get('data', {}).get('type')
        kind = kind[0] if kind else kind
        if kind == 'koji_build' or kind == 'brew-build':
            item = msg['msg'].get('data', {}).get('item')
            item = item[0] if item else item
            if item:
                return set([item.rsplit('-', 2)[0]])

        # Old format
        kind = msg['msg'].get('task', {}).get('type', '')
        if kind == 'koji_build':
            item = msg['msg'].get('task', {}).get('item')
            if item:
                return set([item.rsplit('-', 2)[0]])
        return set()

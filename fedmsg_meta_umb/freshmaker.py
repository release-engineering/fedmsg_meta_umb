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
# Authors:  Chenxiong Qi <cqi@redhat.com>

from fedmsg.meta.base import BaseProcessor


class FreshmakerProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'freshmaker'
    __description__ = 'a service scheduling rebuilds of artifacts as new content becomes available'
    __link__ = 'https://freshmaker.engineering.redhat.com'
    __docs__ = 'https://mojo.redhat.com/docs/DOC-1155261'
    __icon__ = '_static/img/icons/freshmaker.png'
    __obj__ = 'Artifact rebuild scheduler'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        inner_msg = msg['msg']
        topic = msg['topic']

        if topic.endswith('manual.rebuild'):
            template = self._('Manual rebuild is triggered for Errata advisory {errata_id}.')
        elif topic.endswith('build.state.changed'):
            if inner_msg['state_name'] == 'DONE':
                template = self._('{type_name} {name} is successfully rebuilt '
                                  'from original build {original_nvr} to new '
                                  'build {rebuilt_nvr}.')
            else:
                template = self._('{type_name} build state is switched to {state_name}: '
                                  '"{state_reason}"')
        elif topic.endswith('event.state.changed') or topic.endswith('event.state.changed.min'):
            template = self._('Event state is switched to {state_name}: "{state_reason}"')
        else:
            template = 'Unknown message.'

        return template.format(**inner_msg)

    def link(self, msg, **config):
        topic = msg['topic']

        pipeline_url = 'https://pipeline.engineering.redhat.com'
        if topic.endswith('build.state.changed'):
            return '{0}/freshmakerevent/{1}'.format(pipeline_url, msg['msg']['event_id'])
        elif topic.endswith('event.state.changed') or topic.endswith('event.state.changed.min'):
            return '{0}/freshmakerevent/{1}'.format(pipeline_url, msg['msg']['id'])
        elif topic.endswith('manual.rebuild'):
            return '{0}/advisory/{1}'.format(pipeline_url, msg['msg']['errata_id'])
        else:
            # For any other new kind of message that is not known yet
            return None

    def packages(self, msg, **config):
        if msg['topic'].endswith('event.state.changed'):
            try:
                return set([build['name'] for build in msg['msg']['builds']])
            except TypeError:
                return set([nvr.rsplit('-', 2)[0] for nvr in msg['msg']['builds']])
        else:
            return set([])

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
# Authors:  Stanislav Ochotnicky <sochotnicky@redhat.com>

from fedmsg.meta.base import BaseProcessor


class MetaXORProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'metaxor'
    __description__ = 'a service storing information about container images ' \
                      'in Lightblue'
    __link__ = 'https://docs.engineering.redhat.com/x/MxSPAg'
    __docs__ = 'https://docs.engineering.redhat.com/x/MxSPAg'
    __icon__ = ('https://datagrepper-prod-datanommer.int.open.paas.redhat.com/'
                'umb/_static/img/icons/metaxor.png')
    __obj__ = 'Metaxor'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        inner_msg = msg['msg']
        topic = msg['topic']

        if isinstance(inner_msg, str):
            return inner_msg

        if not isinstance(inner_msg, dict):
            return "Unknown message format"

        publish = 'published' if inner_msg.get('published') else 'unpublished'

        if topic.endswith('containerImage.update'):
            template = self._('Existing containerImage entity for {publish} '
                              'container image {brew_build} has been updated.')
        elif topic.endswith('containerImage.insert'):
            template = self._('New containerImage entity for {publish} '
                              'container image {brew_build} has been created.')
        elif topic.endswith('containerRepository.insert'):
            template = self._('New {publish} container repository '
                              '{repository} has been created.')
        elif topic.endswith('containerRepository.update'):
            template = self._('Existing {publish} container repository '
                              '{repository} has been updated.')
        elif topic.endswith('events.refresh'):
            template = self._('Container repository {repository} has been '
                              'refreshed in Lightblue.')
        elif topic.endswith('internal.refresh.repository'):
            template = self._('Repository update ({priority}) requested by {user} - '
                              '{name}')
        else:
            template = 'Unknown message.'

        return template.format(publish=publish, **inner_msg)

    def link(self, msg, **config):
        inner_msg = msg['msg']
        topic = msg['topic']
        if (topic.endswith('events.refresh') or
                topic.endswith('containerRepository.insert') or
                topic.endswith('containerRepository.update')):
            template = ('https://access.redhat.com/containers/#/'
                        'registry.access.redhat.com/{repository}')
            return template.format(**inner_msg)
        elif (topic.endswith('containerImage.update') or
              topic.endswith('containerImage.insert')):
            template = ('https://brewweb.engineering.redhat.com/brew/search?'
                        'terms={brew_build}&type=build&match=exact')
            return template.format(**inner_msg)
        return None

    def packages(self, msg, **config):
        if msg['topic'].endswith('containerImage.update') or \
           msg['topic'].endswith('containerImage.insert'):
            return set([msg['msg']['brew_build'].rsplit('-', 2)[0]])
        else:
            return set([])

    def objects(self, msg, **config):
        if msg['topic'].endswith('containerRepository.update') or \
           msg['topic'].endswith('containerRepository.insert'):
            return {msg['msg']['repository']}
        elif msg['topic'].endswith('internal.refresh.repository'):
            return {msg['msg']['name']}
        else:
            return set()

    def usernames(self, msg, **config):
        if msg['topic'].endswith('internal.refresh.repository'):
            return {msg['msg']['user']}
        return set()

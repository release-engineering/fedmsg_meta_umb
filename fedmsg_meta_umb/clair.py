# Copyright (C) 2019 Red Hat, Inc.
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
# Authors:  Ales Raszka <araszka@redhat.com>

from fedmsg.meta.base import BaseProcessor


class ClairProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'clair'
    __description__ = 'a service responsible for container grading'
    __link__ = 'http://clair-clair-prod.cloud.paas.psi.redhat.com'
    __docs__ = 'https://docs.engineering.redhat.com/x/OhbhB'
    __icon__ = '_static/img/icons/clair.png'
    __obj__ = 'Clair'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        inner_msg = msg['msg']
        topic = msg['topic']

        if not isinstance(inner_msg, dict):
            return "Unknown message format"

        template = 'Unknown message'

        if topic.endswith('clair.notification'):
            if inner_msg.get('affected_images'):
                inner_msg['affected_images_len'] = len(inner_msg['affected_images'])
                template = self._(
                    'New notification batch {vulnerability_name} with {affected_images_len} image(s)'
                )
            else:
                template = self._('New notification {Notification[Name]}')
        elif topic.endswith('clair.scan'):
            template = self._('New image scanned: {nvr}.{arch} ({grades[0][grade]})')
        elif topic.endswith('clair.scan.isv'):
            template = self._('New image scanned: {image_id} ({grades[0][grade]})')
        elif topic.endswith('clair.command'):
            if inner_msg.get('brew_build'):
                template = self._('Scan request: {brew_build}.{architecture}')
            elif inner_msg.get('imageDigest'):
                template = self._('Scan request: {imageDigest}')

        return template.format(**inner_msg)

    def link(self, msg, **config):
        inner_msg = msg['msg']
        topic = msg['topic']
        if topic.endswith('clair.notification'):
            return "{}/notifications/{}?limit=10".format(
                self.__link__, inner_msg['Notification']['Name']
            )
        if topic.endswith('clair.scan'):
            return "{}/ancestry/{}.{}".format(
                self.__link__, inner_msg['nvr'], inner_msg['arch']
            )
        if topic.endswith('clair.scan.isv'):
            return "{}/ancestry/{}".format(
                self.__link__, inner_msg['image_id'].replace(':', '-')
            )
        elif topic.endswith('clair.command'):
            if inner_msg.get('brew_build'):
                return (
                    'https://brewweb.engineering.redhat.com/brew/search?'
                    'terms={brew_build}&type=build&match=glob'.format(**inner_msg)
                )

        return None

    def packages(self, msg, **config):
        inner_msg = msg['msg']
        if msg['topic'].endswith('clair.scan'):
            return set([inner_msg['nvr'].rsplit('-', 2)[0]])
        elif msg['topic'].endswith('clair.command'):
            if inner_msg.get('brew_build'):
                return set([inner_msg['brew_build'].rsplit('-', 2)[0]])

        return set()

    def usernames(self, msg, **config):
        if msg['topic'].endswith('clair.command'):
            return {msg['msg']['user']}
        return set()

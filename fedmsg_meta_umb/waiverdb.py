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


class WaiverDBProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'waiverdb'
    __description__ = 'WaiverDB'
    __link__ = 'https://waiverdb.engineering.redhat.com'
    __docs__ = 'https://pagure.io/docs/waiverdb/'
    __obj__ = 'Waivers'
    __icon__ = '_static/img/icons/waiverdb.png'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        if msg['topic'].endswith('waiverdb.waiver.new'):
            if msg['msg']['waived']:
                action = 'waived'
            else:
                action = 'unwaived'
            return '{username} {action} {testcase} on {subject_identifier} ({product_version})'.format(action=action,
                                                                                                       **msg['msg'])

    def link(self, msg, **config):
        return 'https://waiverdb.engineering.redhat.com/api/v1.0/waivers/{}'.format(msg['msg']['id'])

    def packages(self, msg, **config):
        if msg['msg']['subject_type'] == 'koji_build':
            return set([msg['msg']['subject_identifier'].rsplit('-', 2)[0]])
        return set()

    def usernames(self, msg, **config):
        return set([msg['msg']['username']])

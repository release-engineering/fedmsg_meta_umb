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


class ProjectNewCastleProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'pnc'
    __description__ = 'Project Newcastle'
    __link__ = 'http://orch.cloud.pnc.engineering.redhat.com/'
    __docs__ = 'https://docs.engineering.redhat.com/display/JP/Project+Newcastle'
    __obj__ = 'Middleware Builds'
    __icon__ = '_static/img/icons/newcastle.png'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        tmpl = self._('The {attribute} of pnc {name} build #{buildRecordId} '
                      'changed from {oldStatus} to {newStatus}')
        return tmpl.format(buildRecordId=msg['msg']['buildRecordId'], **msg['headers'])

    def link(self, msg, **config):
        tmpl = 'http://orch.cloud.pnc.engineering.redhat.com/pnc-web/#/build-records/{idx}'
        return tmpl.format(idx=msg['msg']['buildRecordId'])

    def usernames(self, msg, **config):
        return set()

    def packages(self, msg, **config):
        return set()

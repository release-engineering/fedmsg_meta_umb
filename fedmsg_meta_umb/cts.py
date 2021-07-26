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
# Authors:  Lubomír Sedlář <lsedlar@redhat.com>

import logging

from fedmsg.meta.base import BaseProcessor


log = logging.getLogger(__name__)


class CTSProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = "cts"
    __description__ = "The Compose Tracking service"
    __link__ = "https://pagure.io/cts"
    __docs__ = "https://docs.pagure.org/cts/"
    __obj__ = "cts"

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        try:
            compose = msg['msg']['compose']['compose_info']['payload']['compose']['id']
            tag = msg['msg'].get('tag')
            templates = {
                'compose-tagged': self._("Compose {compose} was tagged with {tag}"),
                'compose-untagged': self._("Compose {compose} was untagged with {tag}"),
                'compose-created': self._("Compose {compose} was created"),
                'compose-changed': self._("Compose {compose} was changed"),
            }
            tmpl = templates[msg['msg']['event']]
            return tmpl.format(compose=compose, tag=tag)
        except KeyError:
            log.exception()
            return None

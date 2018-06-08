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
# Authors:  Giulia Naponiello <gnaponie@redhat.com>

from six.moves.urllib.parse import urlencode
from fedmsg.meta.base import BaseProcessor


class GreenwaveProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'greenwave'
    __description__ = 'Greenwave Gating Service'
    __link__ = 'https://greenwave.engineering.redhat.com/api/v1.0/policies'
    __obj__ = 'Gating Decisions'
    __docs__ = 'https://mojo.redhat.com/docs/DOC-1171796'
    __icon__ = ('https://datagrepper-prod-datanommer.int.open.paas.redhat.com/'
                'umb/_static/img/icons/greenwave.png')

    @staticmethod
    def satisfied(msg):
        return msg['msg']['policies_satisfied']

    def link(self, msg, **config):
        subject = msg['msg']['subject']
        if subject:
            base = "https://resultsdb.engineering.redhat.com/results"
            # we want to be sure that we always have the same parameter order
            query = urlencode(sorted(
                [(k, v) for k, v in msg['msg']['subject'][0].items()],
                key=lambda tup: tup[0]
            ))
            return base + "?" + query

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        if self.satisfied(msg):
            decision = self._("is a GO")
        else:
            decision = self._("says NO-GO")

        tmpl = self._(
            "greenwave {decision} on {item} for "
            "\"{decision_context}\" ({product_version})"
        )
        subject = msg['msg']['subject']
        items = [entry.get('item') for entry in subject if entry.get('item')]
        item = items[0] if items else "\"something\""
        return tmpl.format(decision=decision, item=item, **msg['msg'])

    def packages(self, msg, **config):
        subject = msg['msg']['subject']
        items = [
            entry.get('item') for entry in subject
            if entry.get('item') and entry.get('type') in ['brew-build', 'koji_build']
        ]
        return set([item.rsplit('-', 2)[0] for item in items])

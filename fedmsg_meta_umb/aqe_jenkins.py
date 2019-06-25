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
# Authors:  Wai Cheang <wcheang@redhat.com>

from fedmsg.meta.base import BaseProcessor


class AqeJenkinsProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = "aqe-jenkins"
    __description__ = "generates source manifest from dist-git content"
    __link__ = "https://docs.engineering.redhat.com/display/PDT/RetroBob"
    __docs__ = "https://docs.engineering.redhat.com/display/PDT/RetroBob"
    __obj__ = "Container First builds (Retrobob)"
    __icon__ = "_static/img/icons/jenkins.png"

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        if msg['topic'].endswith('aqe-jenkins.retrobob.result'):
            tmpl = self._("retrodep run on build {name} was met with {result}")
            return tmpl.format(**msg['msg'])

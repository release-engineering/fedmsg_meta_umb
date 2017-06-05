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
# Authors:  Ralph Bean <rbean@redhat.com>

from fedmsg.meta.base import BaseProcessor


class PungiProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = "pungi"
    __description__ = "The Compose Tool"
    __link__ = "https://pagure.io/pungi"
    __docs__ = "https://pagure.io/pungi"
    __obj__ = "Composes"

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        compose = msg['msg']['compose_id']
        if msg['topic'].endswith('pungi.status-change'):
            statuses = {
                'STARTED': self._('started'),
                'FINISHED': self._('just finished'),
                'DOOMED': self._('failed in a horrible fire'),
            }
            status = statuses.get(msg['msg']['status'], msg['msg']['status'])
            tmpl = self._("pungi compose of {compose} {status}")
            return tmpl.format(compose=compose, status=status)
        elif msg['topic'].endswith('pungi.phase-start'):
            phase = msg['msg']['phase_name']
            tmpl = self._("pungi started the {phase} phase "
                          "of the {compose} compose")
            return tmpl.format(compose=compose, phase=phase)
        elif msg['topic'].endswith('pungi.phase-stop'):
            phase = msg['msg']['phase_name']
            tmpl = self._("pungi finished the {phase} phase "
                          "of the {compose} compose")
            return tmpl.format(compose=compose, phase=phase)
        elif msg['topic'].endswith('pungi.createiso-imagedone'):
            image = msg['msg']['file'].split('compose/')[-1]
            tmpl = self._("pungi finished createiso for {image}")
            return tmpl.format(image=image)
        elif msg['topic'].endswith('pungi.createiso-imagefail'):
            image = msg['msg']['file'].split('compose/')[-1]
            tmpl = self._("pungi createiso for {image} failed!")
            return tmpl.format(image=image)
        elif msg['topic'].endswith('pungi.createiso-targets'):
            N = len(msg['msg']['deliverables'])
            tmpl = self._("pungi assigned {N} createiso targets for {compose}")
            return tmpl.format(N=N, compose=compose)
        elif msg['topic'].endswith('pungi.ostree'):
            ref = msg['msg']['ref']
            arch = msg['msg']['arch']
            commitid = msg['msg']['commitid']
            tmpl = self._('pungi ostree compose {compose} produced '
                          'ostree commit {commitid} for {arch} {ref}')
            return tmpl.format(compose=compose, arch=arch, commitid=commitid,
                               ref=ref)

    def link(self, msg, **config):
        if 'location' in msg['msg']:
            location = msg['msg']['location'].rstrip('/').rstrip('/compose')
            if not location.startswith('http'):
                base = 'http://download.lab.bos.redhat.com'
                prefix = '/mnt/redhat'
                return base + location[len(prefix):]
            return location

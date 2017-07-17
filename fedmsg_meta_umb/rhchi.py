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


class RHCHIProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'rhchi'
    __description__ = 'the RHCHI Container Validation Pipeline'
    __link__ = 'https://chi-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/'
    __docs__ = 'https://docs.engineering.redhat.com/display/RHAPPINFRA/Container+E2E+QE+-+Full+Workflow'
    __obj__ = 'pipeline progress'
    __icon__ = ('https://chi-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/'
                '0e416130/images/headshot.png')

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        template = self._("The {rhchi_stage} phase of the RHCHI "
                          "pipeline {status} for {container_name}")
        return template.format(**msg['headers'])

    def link(self, msg, **config):
        return msg['headers']['url']

    def packages(self, msg, **config):
        return set([msg['headers']['container_nvr'].rsplit('-', 2)[0]])

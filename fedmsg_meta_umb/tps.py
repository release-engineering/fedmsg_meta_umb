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
# Authors: Gowrishankar Rajaiyan <grajaiya@redhat.com>

from fedmsg.meta.base import BaseProcessor


class TPSProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'tps'
    __description__ = 'package sanity testing of brew builds'
    __obj__ = 'Test Package Sanity'
    __docs__ = ('https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/'
                'test-package-sanity-documentation/lastSuccessfulBuild/artifact/docs/index.html')
    __link__ = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/test-package-sanity-development'
    __icon__ = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def packages(self, msg, **config):
        return set([msg['headers']['component'].rsplit('-', 2)[0]])

    def subtitle(self, msg, **config):
        if msg['topic'].endswith('.starting'):
            template = self._("package sanity testing started for "
                              "component: {component} with brew task_id: {brew_task_id}")
        elif msg['topic'].endswith('.completed'):
            template = self._("package sanity testing completed for "
                              "component: {component} with brew task_id: {brew_task_id}")
        else:
            template = self._("package sanity testing results for "
                              "component: {component} with brew task_id: {brew_task_id}")

        return template.format(**msg['headers'])

    def link(self, msg, **config):
        if msg['topic'].endswith('.starting') or msg['topic'].endswith('.completed'):
            return msg['headers']['jenkins_build_url']
        else:
            return msg['msg']['infrastructure']['jenkins_build_url']

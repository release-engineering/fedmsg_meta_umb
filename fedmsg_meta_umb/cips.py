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

import logging

from fedmsg.meta.base import BaseProcessor


log = logging.getLogger(__name__)


class CIPSProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'cips'
    __description__ = 'continuous integration package sanity testing of brew builds'
    __obj__ = 'Continuous Integration Package Sanity'
    __docs__ = ('https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/'
                'ci-package-sanity-documentation/lastSuccessfulBuild/artifact/cips/docs/builddir/index.html')
    __link__ = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/job/ci-package-sanity-development'
    __icon__ = 'https://rpm-factory-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/static/0e416130/images/headshot.png'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def packages(self, msg, **config):
        if 'component' in msg.get('headers', {}):
            return set([msg['headers']['component'].rsplit('-', 2)[0]])
        return set()

    def subtitle(self, msg, **config):
        required = set(['component', 'id'])
        if not required.issubset(set(msg.get('headers', {}).keys())):
            log.warn("%r missing from %r" % (required, msg.get('headers')))
            return None
        if msg['topic'].endswith('.start'):
            template = self._("continuous integration package sanity testing started for "
                              "component: {component} with brew task_id: {id}")
        elif msg['topic'].endswith('.end'):
            template = self._("continuous integration package sanity testing ended for "
                              "component: {component} with brew task_id: {id}")
        elif msg['topic'].endswith('.running'):
            template = self._("continuous integration package sanity testing in progress for "
                              "component: {component} with brew task_id: {id}")
        else:
            if 'status' not in msg['msg']:
                log.warn("No 'status' found in %r" % msg['msg'])
                return None
            template = self._("continuous integration package sanity testing %s for "
                              "component: {component} with brew task_id: {id}"
                              % msg['msg']['status'])

        return template.format(**msg['headers'])

    def link(self, msg, **config):
        if msg['topic'].endswith('.complete') or msg['topic'].endswith('running'):
            msg = msg.get('msg', {})
            return msg.get('run').get('url')
        elif msg['topic'].endswith('.start') or msg['topic'].endswith('.end'):
            return msg['headers']['jenkins_build_url']

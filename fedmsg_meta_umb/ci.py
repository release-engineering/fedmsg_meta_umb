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
# Authors:  Yukin Chan <yuqchen@redhat.com>

from fedmsg.meta.base import BaseProcessor

class CIProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'ci'
    __description__ = 'Engineering CI Automation System'
    __link__ = 'https://libvirt-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/'
    __docs__ = 'https://libvirt-jenkins.rhev-ci-vms.eng.rdu2.redhat.com/view'
                '/Utils/job/libvirt-jobs-updater/lastSuccessfulBuild/artifact'
                '/libvirt-ci/docs/build/html/intro.html'
    __obj__ = 'Engineering CI Automation'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        return 'CI Test Job' + msg['topic'].split('.')[-1]

    def packages(self, msg, **config):
        return set([msg['header']['component']])

    def usernames(self, msg, **config):
        return set([msg['msg']['ci']['name'],
                    msg['msg']['artifact']['issuer']])

    def link(self, msg, **config):
        return msg['msg']['run']['url']

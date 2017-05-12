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
# Authors:  Mike Bonnet <mikeb@redhat.com>

from fedmsg.meta.base import BaseProcessor


class DistGitProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'distgit'
    __description__ = 'the dist-git repository management system'
    __link__ = 'https://pkgs.devel.redhat.com'
    __docs__ = 'https://mojo.redhat.com/docs/DOC-1045187'
    __obj__ = 'Dist-Git Repository Management System'
    __icon__ = 'https://git-scm.com/images/logos/downloads/Git-Icon-Black.png'
    link_template = ('https://pkgs.devel.redhat.com/cgit/rpms/{repo}/'
                     'commit/?h={branch}&id={rev}')
    subtitle_template = ('{shortrev} was committed on the {branch} branch '
                         'of the {repo} {repotype} repo by {username}')

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        return self.subtitle_template.format(repotype=msg['msg']['namespace'][:-1],
                                             shortrev=msg['msg']['rev'][:8],
                                             **msg['msg'])

    def packages(self, msg, **config):
        return set([msg['msg']['repo']])

    def usernames(self, msg, **config):
        return set([msg['msg']['username']])

    def link(self, msg, **config):
        return self.link_template.format(**msg['msg'])

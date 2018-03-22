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
    commit_link_template = ('https://pkgs.devel.redhat.com/cgit/rpms/{repo}/'
                            'commit/?h={branch}&id={rev}')
    push_link_template = 'https://pkgs.devel.redhat.com/cgit/rpms/{repo}/log/?h={branch}'
    commit_subtitle_template = ('{shortrev} was committed on the {branch} branch '
                                'of the {repo} {repotype} repo by {username}')
    push_subtitle_template = ('{numcommits} {commits_str} {were_str} pushed to the {branch} '
                              'branch of the {repo} {repotype} repo by {username}')

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        if msg['topic'].endswith('.commit'):
            return self.commit_subtitle_template.format(repotype=msg['msg']['namespace'][:-1],
                                                        shortrev=msg['msg']['rev'][:8],
                                                        **msg['msg'])
        elif msg['topic'].endswith('.push'):
            if msg['msg']['numcommits'] == 1:
                commits_str = 'commit'
                were_str = 'was'
            else:
                commits_str = 'commits'
                were_str = 'were'
            return self.push_subtitle_template.format(commits_str=commits_str,
                                                      were_str=were_str,
                                                      repotype=msg['msg']['namespace'][:-1],
                                                      **msg['msg'])

    def packages(self, msg, **config):
        return set([msg['msg']['repo']])

    def usernames(self, msg, **config):
        return set([msg['msg']['username']])

    def link(self, msg, **config):
        if msg['topic'].endswith('.commit'):
            return self.commit_link_template.format(**msg['msg'])
        elif msg['topic'].endswith('.push'):
            return self.push_link_template.format(**msg['msg'])

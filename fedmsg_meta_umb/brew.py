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

class BrewProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'brew'
    __description__ = 'the Brew build system'
    __link__ = 'https://brewweb.engineering.redhat.com/brew/'
    __docs__ = 'https://mojo.redhat.com/docs/DOC-1024827'
    __obj__ = 'Brew Build System'
    __icon__ = ('https://brewweb.engineering.redhat.com/'
                'koji-static/themes/brew/images/brew_small.png')

    def __init__(self, *args, **kw):
        super(BrewProcessor, self).__init__(*args, **kw)
        self.subtitle_templates = {
            'task': {
                'free': self._('{info[method]} task {info[id]} has been created'),
                'open': self._('{info[method]} task {info[id]} has started'),
                'closed': self._('{info[method]} task {info[id]} has completed'),
                'canceled': self._('{info[method]} task {info[id]} has been canceled'),
                'assigned': self._('{info[method]} task {info[id]} has been assigned'),
                'failed': self._('{info[method]} task {info[id]} has failed'),
            },
            'repo': {
                'init': self._('repo {repo_id} for {tag[name]} is being created'),
                'done': self._('repo {repo[id]} for {repo[tag_name]} has been created'),
            },
            'package': {
                'add': self._('package {package[name]} was added to tag {tag[name]}'),
                'update': self._('package {package[name]} was updated in tag {tag[name]}'),
                'block': self._('package {package[name]} was blocked in tag {tag[name]}'),
                'unblock': self._('package {package[name]} was unblocked in tag {tag[name]}'),
                'remove': self._('package {package[name]} was removed from tag {tag[name]}'),
            },
            'build': {
                'building': self._('{info[name]}-{info[version]}-{info[release]} is building'),
                'complete': self._('{info[nvr]} has been built successfully'),
                'deleted': self._('{info[nvr]} has been deleted'),
                'failed': self._('build of {info[nvr]} has failed'),
                'canceled': self._('build of {info[nvr]} has been canceled'),
                'tag': self._('{build[nvr]} tagged into {tag[name]}'),
                'untag': self._('{build[nvr]} untagged from {tag[name]}'),
            },
            'import': {
                'build': self._('{build[nvr]} has been imported'),
                'rpm': self._('{rpm[name]}-{rpm[version]}-{rpm[release]}.{rpm[arch]}.rpm has been imported'),
                'archive': self._('{archive[filename]} from {build[nvr]} has been imported'),
                'image': self._('{image[arch]} image from {build[nvr]} has been imported'),
                'cg': self._('{build[nvr]} has been imported by a Content Generator'),
            },
            'sign': {
                'rpm': self._('{rpm[name]}-{rpm[version]}-{rpm[release]}.{rpm[arch]}.rpm has been signed '
                              'with key {sigkey}'),
            },
        }

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        tokens = msg['topic'].split('.')
        if len(tokens) < 3:
            return None
        if tokens[-2] not in self.subtitle_templates:
            return None
        tmpl = self.subtitle_templates[tokens[-2]].get(tokens[-1])
        if tmpl:
            return tmpl.format(**msg['msg'])
        return None

    def packages(self, msg, **config):
        tokens = msg['topic'].split('.')
        if len(tokens) < 3:
            return set()
        if tokens[-2] == 'package':
            return set([msg['msg']['package']['name']])
        elif tokens[-2] == 'build':
            if tokens[-1] in ['tag', 'untag']:
                return set([msg['msg']['build']['name']])
            else:
                return set([msg['msg']['info']['name']])
        elif tokens[-2] == 'import':
            return set([msg['msg']['build']['name']])
        elif tokens[-2] == 'sign':
            return set([msg['msg']['build']['name']])
        return set()

    def usernames(self, msg, **config):
        tokens = msg['topic'].split('.')
        if len(tokens) < 3:
            return set()
        if tokens[-2] == 'build':
            if tokens[-1] in ['tag', 'untag']:
                return set([msg['msg']['user']['name'],
                            msg['msg']['build']['owner_name']])
            else:
                return set([msg['msg']['info']['owner_name']])
        elif tokens[-2] == 'import':
            return set([msg['msg']['build']['owner_name']])
        elif tokens[-2] == 'sign':
            return set([msg['msg']['build']['owner_name']])
        return set()

    def link(self, msg, **config):
        tokens = msg['topic'].split('.')
        if len(tokens) < 3:
            return self.__link__
        if tokens[-2] == 'task':
            return self.__link__ + 'taskinfo?taskID=' + \
                str(msg['msg']['info']['id'])
        elif tokens[-2] == 'package':
            return self.__link__ + 'packageinfo?packageID=' + \
                str(msg['msg']['package']['id'])
        elif tokens[-2] == 'build':
            if tokens[-1] in ['tag', 'untag']:
                build_id = msg['msg']['build']['id']
            else:
                build_id = msg['msg']['info']['id']
            return self.__link__ + 'buildinfo?buildID=' + str(build_id)
        elif tokens[-2] == 'repo':
            if tokens[-1] == 'init':
                tag_id = msg['msg']['tag']['id']
            else:
                tag_id = msg['msg']['repo']['tag_id']
            return self.__link__ + 'taginfo?tagID=' + str(tag_id)
        return self.__link__

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
# Authors:  Stanislav Ochotnicky <sochotnicky@redhat.com>

from fedmsg.meta.base import BaseProcessor


class JIRAProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'jira'
    __description__ = 'an issue tracking system from Atlassian'
    __link__ = 'https://projects.engineering.redhat.com'
    __docs__ = 'https://docs.engineering.redhat.com/x/pa7FAw'
    __icon__ = 'https://projects.engineering.redhat.com/favicon.ico'
    __obj__ = 'JIRA issue tracking system'

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        inner_msg = msg['msg']
        data = {}
        try:
            # these will only be available on issue create/update but not
            # comment added/edited messages
            data['key'] = inner_msg['issue']['key']
            data['issue_type'] = inner_msg['issue']['fields']['issuetype']['name']
            data['summary'] = inner_msg['issue']['fields']['summary']
        except KeyError:
            return None
        topic = msg['topic']

        if topic.endswith('jira.issue.created'):
            data['author'] = inner_msg['user']['displayName']
            template = self._('{issue_type} {key} has been created by '
                              '{author}.')
        elif topic.endswith('jira.issue.updated'):
            data['author'] = inner_msg['user']['displayName']
            template = self._('{issue_type} {key} has been updated by '
                              '{author}.')
        elif topic.endswith("jira.comment.added"):
            data['author'] = inner_msg['comment']['author']['displayName']
            data['issue_type'] = data['issue_type'].lower()
            template = self._('Comment has been added by {author} in {issue_type} '
                              '{key}.')
        elif topic.endswith("jira.comment.updated"):
            data['author'] = inner_msg['comment']['updateAuthor']['displayName']
            data['issue_type'] = data['issue_type'].lower()
            template = self._('Comment has been edited by {author} in {issue_type} '
                              '{key}.')
        else:
            template = 'Unknown message.'

        return template.format(**data)

    def link(self, msg, **config):
        inner_msg = msg['msg']
        topic = msg['topic']
        comment_id = None
        template = self.__link__ + "/browse/{key}"
        if (topic.endswith('jira.comment.added') or
                topic.endswith('jira.comment.updated')):
            comment_id = inner_msg['comment']['id']
            template = template + "?focusedCommentId={comment_id}"
        try:
            return template.format(key=inner_msg['issue']['key'],
                                   comment_id=comment_id)
        except KeyError:
            return None

    def usernames(self, msg, **config):
        names = set()
        inner_msg = msg['msg']

        # this is relatively readable at least. Various pieces can exist in
        # different situations so let's just handle by ignoring missing places
        try:
            names.add(inner_msg['issue']['fields']['creator']['name'])
        except KeyError:
            pass
        try:
            names.add(inner_msg['issue']['fields']['assignee']['name'])
        except KeyError:
            pass
        try:
            names.add(inner_msg['issue']['fields']['reporter']['name'])
        except KeyError:
            pass
        try:
            names.add(inner_msg['comment']['author']['name'])
        except KeyError:
            pass
        try:
            names.add(inner_msg['comment']['updateAuthor']['name'])
        except KeyError:
            pass
        try:
            names.add(inner_msg['user']['name'])
        except KeyError:
            pass
        return names

    def agent(self, msg, **config):
        try:
            return msg['msg']['user']['name']
        except KeyError:
            return None

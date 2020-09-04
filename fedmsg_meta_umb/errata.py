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

import copy

from fedmsg.meta.base import BaseProcessor


class ErrataProcessor(BaseProcessor):
    topic_prefix_re = r'/topic/VirtualTopic\.eng'

    __name__ = 'errata'
    __description__ = 'the Errata Tool'
    __link__ = 'https://errata.devel.redhat.com/'
    __docs__ = 'https://errata.devel.redhat.com/user-guide/'
    __obj__ = 'errata events'
    __icon__ = ('https://errata.devel.redhat.com/assets/'
                'images/erratatool18.png')

    def __init__(self, *args, **kwargs):
        super(ErrataProcessor, self).__init__(*args, **kwargs)
        self.simple_subtitle_templates = {
            'errata.activity.status': self._(
                '{agent} moved {fulladvisory} from {from} to {to}'),
            'errata.activity.created': self._(
                '{agent} filed a new {type} advisory for {release}'),
            'errata.activity.signing': self._(
                '{agent} reported signing {to} for {fulladvisory}'),
            'errata.bugs.changed': self._(
                '{agent} changed bugs on an advisory'),
            'errata.builds.changed': self._(
                '{agent} changed builds on an advisory'),
            'errata.builds.added': self._(
                '{agent} added {brew_build} to {product} advisory {errata_id}'),
            'errata.builds.removed': self._(
                '{agent} removed {brew_build} from {product} advisory {errata_id}'),
            'errata.ccat.reschedule_test': self._(
                'CCAT for erratum {ERRATA_ID} in {TARGET} was rescheduled'),
            'errata.ccat': self._(
                'CAT results for erratum {ERRATA_ID} on {TARGET} ({TRIGGER_TYPE}): {MESSAGE_TYPE}'),
        }

    def title(self, msg, **config):
        return msg['topic'].split('.', 2)[-1]

    def subtitle(self, msg, **config):
        headers = copy.deepcopy(msg['headers'])
        title = self.title(msg, **config)
        agent = self.agent(msg, **config)

        # First, handle the simple cases...
        template = self.simple_subtitle_templates.get(title)
        if template:
            return template.format(agent=agent, **headers)

        # Then, handle these more complex cases if that failed.
        if title == 'errata.activity.security_approved':
            if headers['to'] == '1':
                template = self._('{agent} approved the security '
                                  'request on {fulladvisory}')
            elif headers['to'] == 'null':
                template = self._('{agent} unset the security '
                                  'flag on {fulladvisory}')
            elif headers['to'] == '0':
                # Two very different senses of "false"
                if headers['from'] == 'null':
                    template = self._('{agent} requested security '
                                      'approval on {fulladvisory}')
                else:
                    template = self._('{agent} denied the security '
                                      'request on {fulladvisory}')

            return template.format(agent=agent, **headers)

        elif title == 'errata.activity.batch':
            if headers['to'] != 'null':
                template = self._('{agent} added {fulladvisory} '
                                  'to the {to} advisory batch')
            else:
                template = self._('{agent} removed {fulladvisory} '
                                  'from the {from} advisory batch')
            return template.format(agent=agent, **headers)
        elif title == 'errata.activity.docs_approval':
            if headers['to'] == 'docs_approved':
                template = self._('{agent} approved the docs '
                                  'on {fulladvisory}')
            else:
                template = self._('{agent} changed the docs flag '
                                  'on {fulladvisory} to {to}')
            return template.format(agent=agent, **headers)
        elif title == 'errata.activity.assigned_to':
            if headers['to'] == 'null':
                template = self._('{agent} unassigned {fulladvisory}')
            else:
                headers['to'] = self.scrub_username(headers['to'])
                template = self._('{agent} assigned {to} to {fulladvisory}')
            return template.format(agent=agent, **headers)
        elif title == 'errata.activity.text_changes':
            body = msg['msg']
            field_list = [t['name'] for t in body['text_changes']]
            fields = ', '.join(field_list)
            if len(field_list) == 2:
                fields = fields.replace(', ', ' and ')
            elif len(field_list) > 2:
                # Oxford comma
                fields = '{0}, and {2}'.format(*fields.rpartition(', '))
            template = '{0} changed {1} on {2} advisory {3}'
            return template.format(agent, fields, body['product'], body['errata_id'])

    @staticmethod
    def scrub_username(username):
        return username.split('@')[0].split('/')[0]

    def agent(self, msg, **config):
        who = msg['headers'].get('who')
        if who:
            return self.scrub_username(who)
        else:
            return None

    def usernames(self, msg, **config):
        # Every message returns the agent in the set...
        persons = set()
        agent = self.agent(msg, **config)
        if agent:
            persons.add(agent)

        # But a select few messages have additional persons associated
        title = self.title(msg, **config)
        if title == 'errata.activity.assigned_to':
            for key in ('from', 'to',):
                if msg['headers'][key] != 'null':
                    persons.add(self.scrub_username(msg['headers'][key]))

        return persons

    def link(self, msg, **config):
        title = self.title(msg, **config)
        if title == 'errata.ccat.reschedule_test':
            template = 'https://pipeline.engineering.redhat.com/advisory/{ERRATA_ID}'
        elif title == 'errata.ccat':
            template = msg['msg'].get('BUILD_URL', '')
        else:
            template = 'https://pipeline.engineering.redhat.com/advisory/{errata_id}'
        return template.format(**msg['headers'])

    def packages(self, msg, **config):
        nvr = msg['headers'].get('brew_build')
        if nvr:
            return set([nvr.rsplit('-', 2)[0]])
        return set()

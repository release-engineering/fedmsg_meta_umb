# Copyright (C) 2019 Red Hat, Inc.
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
# Authors:  Ales Raszka <araszka@redhat.com>

from fedmsg.meta.base import BaseProcessor


class ClairProcessor(BaseProcessor):
    topic_prefix_re = r"/topic/VirtualTopic\.eng"

    __name__ = "clair"
    __description__ = "a service responsible for container grading"
    __link__ = "https://clair.engineering.redhat.com"
    __docs__ = "https://docs.engineering.redhat.com/x/OhbhB"
    __icon__ = "_static/img/icons/clair.png"
    __obj__ = "Clair"

    def title(self, msg, **config):
        return msg["topic"].split(".", 2)[-1]

    def subtitle(self, msg, **config):
        inner_msg = msg["msg"]
        topic = msg["topic"]

        if not isinstance(inner_msg, dict) and not isinstance(inner_msg, list):
            return "Unknown message format"

        template = "Unknown message"

        if topic.endswith("clair.v4.notification"):
            by_reason = self._split_by_reason(inner_msg)
            return "New notification - added: {}, removed: {} vulnerabilities".format(
                len(by_reason.get("added", [])), len(by_reason.get("removed", []))
            )
        elif topic.endswith("clair.scan"):
            if inner_msg.get("nvr") and inner_msg.get("arch"):
                template = self._(
                    "New image scanned: {nvr}.{arch} ({grades[0][grade]})"
                )
            elif inner_msg.get("nvra"):
                template = self._("New image scanned: {nvra} ({grades[0][grade]})")
        elif topic.endswith("clair.scan.isv"):
            template = self._("New image scanned: {image_id} ({grades[0][grade]})")
        elif topic.endswith("clair.command"):
            if inner_msg.get("brew_build"):
                template = self._("Scan request: {brew_build}.{architecture}")
            elif inner_msg.get("imageDigest"):
                template = self._("Scan request: {imageDigest}")

        return template.format(**inner_msg)

    def link(self, msg, **config):
        inner_msg = msg["msg"]
        topic = msg["topic"]
        if topic.endswith("clair.scan") or topic.endswith("clair.scan.isv"):
            if inner_msg.get("image_id"):
                return "{}/matcher/api/v1/vulnerability_report/{}".format(
                    self.__link__, inner_msg["image_id"]
                )
        elif topic.endswith("clair.command"):
            if inner_msg.get("brew_build"):
                return (
                    "https://brewweb.engineering.redhat.com/brew/search?"
                    "terms={brew_build}&type=build&match=glob".format(**inner_msg)
                )

        return None

    def packages(self, msg, **config):
        inner_msg = msg["msg"]
        if msg["topic"].endswith("clair.scan") and inner_msg.get("nvr"):
            return set([inner_msg["nvr"].rsplit("-", 2)[0]])
        if msg["topic"].endswith("clair.scan") and inner_msg.get("nvra"):
            return set([inner_msg["nvra"].rsplit("-", 2)[0]])
        elif msg["topic"].endswith("clair.command"):
            if inner_msg.get("brew_build"):
                return set([inner_msg["brew_build"].rsplit("-", 2)[0]])

        return set()

    def usernames(self, msg, **config):
        if msg["topic"].endswith("clair.command"):
            return {msg["msg"]["user"]}
        return set()

    def _split_by_reason(self, notifications):
        """
        Split notification by notification reason

        Args:
            notifications (list): Clair notifications

        Returns:
            dict: notification split by reason - reason as key
        """
        by_reason = {}
        for notification in notifications:
            reason = notification.get("reason", "")
            if reason not in by_reason:
                by_reason[reason] = []
            by_reason[reason].append(notification)
        return by_reason

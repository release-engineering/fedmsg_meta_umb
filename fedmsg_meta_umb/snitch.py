# Copyright (C) 2020 Red Hat, Inc.
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


class SnitchProcessor(BaseProcessor):
    topic_prefix_re = r"/topic/VirtualTopic\.eng"

    __name__ = "snitch"
    __description__ = "a service responsible for emiting Mongo events to UMB"
    __link__ = "https://gitlab.cee.redhat.com/rad/snitch"
    __docs__ = "https://docs.engineering.redhat.com/x/A88wBw"
    __icon__ = "_static/img/icons/snitch.png"
    __obj__ = "Snitch"

    def title(self, msg, **config):
        return msg["topic"].split(".", 2)[-1]

    def subtitle(self, msg, **config):
        inner_msg = msg["msg"]
        headers = msg["headers"]

        if not isinstance(inner_msg, dict):
            return "Unknown message format"

        obj_id = inner_msg["entityData"]["_id"]
        if isinstance(obj_id, dict) and obj_id.get("$oid"):
            obj_id = obj_id.get("$oid")
        data = {
            "entityData": inner_msg["entityData"],
            "entityName": inner_msg["entityName"],
            "operationType": headers["operationType"],
            "_id": obj_id,
        }

        template = self._("New DB event ({operationType}): {entityName} - {_id}")

        return template.format(**data)

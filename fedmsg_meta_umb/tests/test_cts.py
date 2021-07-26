# Copyright (C) 2017 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Lubomír Sedlář <lsedlar@redhat.com>

import fedmsg.tests.test_meta
from .common import add_doc


class TestCTSCreated(fedmsg.tests.test_meta.Base):
    """Compose Tracking Service (CTS) stored metadata about composes created in various services.

    Here's an example message published when a compose is created in CTS.
    """
    expected_title = "cts.compose-created"
    expected_subti = "Compose TEST-1-20210511.1 was created"
    msg = {
        "msg": {
            "event": "compose-created",
            "compose": {
                "builder": "odcs/odcs.example.com",
                "children": [],
                "parents": [],
                "respin_of": None,
                "respun_by": [],
                "tags": [],
                "compose_info": {
                    "header": {
                        "version": "1.2",
                        "type": "productmd.composeinfo",
                    },
                    "payload": {
                        "compose": {
                            "id": "TEST-1-20210511.1",
                            "date": "20210511",
                            "label": "Beta-1.0",
                            "respin": 1,
                            "type": "production",
                            "final": False,
                        },
                        "release": {
                            "short": "TEST",
                            "name": "TEST",
                            "type": "ga",
                            "version": "1",
                            "internal": False,
                        },
                        "variants": {}
                    },
                },
            },
        },
        "timestamp": 1449600728.0,
        "topic": "/topic/VirtualTopic.eng.cts.compose-created"
    }


class TestCTSChange(fedmsg.tests.test_meta.Base):
    """Compose Tracking Service (CTS) stored metadata about composes created in various services.

    Here's an example message published when a compose is changed in CTS.
    """
    expected_title = "cts.compose-changed"
    expected_subti = "Compose TEST-1-20210511.1 was changed"
    msg = {
        "msg": {
            "event": "compose-changed",
            "compose": {
                "builder": "odcs/odcs.example.com",
                "children": [],
                "parents": [],
                "respin_of": None,
                "respun_by": [],
                "tags": [],
                "compose_info": {
                    "header": {
                        "version": "1.2",
                        "type": "productmd.composeinfo",
                    },
                    "payload": {
                        "compose": {
                            "id": "TEST-1-20210511.1",
                            "date": "20210511",
                            "label": "Beta-1.0",
                            "respin": 1,
                            "type": "production",
                            "final": False,
                        },
                        "release": {
                            "short": "TEST",
                            "name": "TEST",
                            "type": "ga",
                            "version": "1",
                            "internal": False,
                        },
                        "variants": {}
                    },
                },
            },
        },
        "timestamp": 1449600728.0,
        "topic": "/topic/VirtualTopic.eng.cts.compose-changed"
    }


class TestCTSTagged(fedmsg.tests.test_meta.Base):
    """Compose Tracking Service (CTS) stored metadata about composes created in various services.

    Here's an example message published when a tag is added to a compose in CTS.
    """
    expected_title = "cts.compose-tagged"
    expected_subti = "Compose TEST-1-20210511.1 was tagged with nightly-requested"
    msg = {
        "msg": {
            "event": "compose-tagged",
            "tag": "nightly-requested",
            "compose": {
                "builder": "odcs/odcs.example.com",
                "children": [],
                "parents": [],
                "respin_of": None,
                "respun_by": [],
                "tags": ["nightly-requested"],
                "compose_info": {
                    "header": {
                        "version": "1.2",
                        "type": "productmd.composeinfo",
                    },
                    "payload": {
                        "compose": {
                            "id": "TEST-1-20210511.1",
                            "date": "20210511",
                            "label": "Beta-1.0",
                            "respin": 1,
                            "type": "production",
                            "final": False,
                        },
                        "release": {
                            "short": "TEST",
                            "name": "TEST",
                            "type": "ga",
                            "version": "1",
                            "internal": False,
                        },
                        "variants": {}
                    },
                },
            },
        },
        "timestamp": 1449600728.0,
        "topic": "/topic/VirtualTopic.eng.cts.compose-tagged"
    }


class TestCTSUntagged(fedmsg.tests.test_meta.Base):
    """Compose Tracking Service (CTS) stored metadata about composes created in
    various services.

    Here's an example message published when a tag is removed from a compose in
    CTS.
    """
    expected_title = "cts.compose-untagged"
    expected_subti = "Compose TEST-1-20210511.1 was untagged with nightly-requested"
    msg = {
        "msg": {
            "event": "compose-untagged",
            "tag": "nightly-requested",
            "compose": {
                "builder": "odcs/odcs.example.com",
                "children": [],
                "parents": [],
                "respin_of": None,
                "respun_by": [],
                "tags": [],
                "compose_info": {
                    "header": {
                        "version": "1.2",
                        "type": "productmd.composeinfo",
                    },
                    "payload": {
                        "compose": {
                            "id": "TEST-1-20210511.1",
                            "date": "20210511",
                            "label": "Beta-1.0",
                            "respin": 1,
                            "type": "production",
                            "final": False,
                        },
                        "release": {
                            "short": "TEST",
                            "name": "TEST",
                            "type": "ga",
                            "version": "1",
                            "internal": False,
                        },
                        "variants": {}
                    },
                },
            },
        },
        "timestamp": 1449600728.0,
        "topic": "/topic/VirtualTopic.eng.cts.compose-untagged"
    }


add_doc(locals())

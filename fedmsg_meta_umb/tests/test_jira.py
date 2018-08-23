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

import fedmsg.tests.test_meta

class TestJIRAIssueCreate(fedmsg.tests.test_meta.Base):
    """JIRA is issue tracking system

    Messages (like the example given here) are published when new issue is
    created
    """
    expected_title = 'jira.issue.created'
    expected_subti = 'New JIRA issue DEVOPSA-4091 has been created.'
    expected_link = ('https://projects.engineering.redhat.com/browse/'
                     'DEVOPSA-4091')
    expected_packages = set([])
    expected_icon = 'https://projects.engineering.redhat.com/favicon.ico'
    expected_usernames = set(['rbean', 'kboran'])

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1534783210.0,
        "msg_id": "ID:messaging-devops-broker01.web.prod."
        "ext.phx2.redhat.com-37550-1534679656045-2:40012:-1:1:144",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.jira.issue.created",
        "headers": {
            "priority": "4",
            "expires": "1535388010247",
            "event_type": "jira:issue_created",
            "project": "DEVOPSA",
            "timestamp": "1534783210247",
            "destination": "/topic/VirtualTopic.eng.jira.issue.created",
            "issue_key": "DEVOPSA-4091",
            "message-id": "ID:messaging-devops-broker01.web.prod."
            "ext.phx2.redhat.com-37550-1534679656045-2:40012:-1:1:144",
            "content-type": "application/json",
            "subscription": "/queue/Consumer.client-datanommer."
            "upshift-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.9.1",
        "msg": {
            "comment": {
                "updateAuthor": {},
                "author": {}
            },
            "webhookEvent": "jira:issue_created",
            "issue": {
                "fields": {
                    "status": {
                        "statusCategory": {
                            "colorName": "blue-gray",
                            "key": "new",
                            "name": "To Do"
                        },
                        "description": "This status is managed internally",
                        "name": "To Do"
                    },
                    "updated": "2018-08-20T16:40:09.644+0000",
                    "description": "Proper long description",
                    "creator": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    },
                    "created": "2018-08-20T16:40:09.644+0000",
                    "votes": {},
                    "watches": {},
                    "summary": "Add some basic summary to new issues",
                    "project": {
                        "projectCategory": {
                            "description": "Tools developed by PnT",
                            "name": "PnT Developer Operations Tools"
                        },
                        "name": "PnT DevOps Automation",
                        "key": "DEVOPSA"
                    },
                    "assignee": {
                        "displayName": "Kyle Boran",
                        "name": "kboran",
                        "emailAddress": "kboran@redhat.com",
                        "key": "kboran",
                        "active": True,
                        "timeZone": "America/New_York"
                    },
                    "issuetype": {
                        "description": "A task that needs to be done.",
                        "name": "Task"
                    },
                    "resolution": {},
                    "reporter": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    }
                },
                "key": "DEVOPSA-4091"
            },
            "user": {
                "emailAddress": "rbean@redhat.com",
                "self": "https://projects.engineering.redhat.com/rest/api/2/"
                "user?username=rbean",
                "displayName": "Ralph Bean",
                "name": "rbean",
                "timeZone": "America/Havana"
            },
            "changelog": {}
        }
    }

class TestJIRAIssueGenericUpdate(fedmsg.tests.test_meta.Base):
    """JIRA is issue tracking system

    Messages (like the example given here) are published when issue is
    updated. There are some more specific updates for comments being
    added/removed as well
    """
    expected_title = 'jira.issue.updated'
    expected_subti = 'JIRA issue FACTORY-2904 has been updated.'
    expected_link = ('https://projects.engineering.redhat.com/browse/'
                     'FACTORY-2904')
    expected_packages = set([])
    expected_icon = 'https://projects.engineering.redhat.com/favicon.ico'
    expected_usernames = set(['rbean', 'red-user'])

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1534777940.0,
        "msg_id":
        "ID:messaging-devops-broker01.web.prod.ext.phx2."
        "redhat.com-37550-1534679656045-2:40012:-1:1:132",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.jira.issue.updated",
        "headers": {
            "priority": "4",
            "expires": "1535382740838",
            "event_type": "jira:issue_updated",
            "project": "FACTORY",
            "timestamp": "1534777940838",
            "destination": "/topic/VirtualTopic.eng.jira.issue.updated",
            "issue_key": "FACTORY-2904",
            "message-id":
            "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-37550-1534679656045-2:40012:-1:1:132",
            "content-type": "application/json",
            "subscription":
            "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.9.1",
        "msg": {
            "comment": {
                "updateAuthor": {},
                "author": {}
            },
            "webhookEvent": "jira:issue_updated",
            "issue": {
                "fields": {
                    "status": {
                        "statusCategory": {
                            "colorName": "yellow",
                            "key": "indeterminate",
                            "name": "In Progress"
                        },
                        "description": "This issue is being worked on.",
                        "name": "In Progress"
                    },
                    "updated": "2018-08-20T15:12:20.474+0000",
                    "description": "Some longer description",
                    "creator": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    },
                    "created": "2018-08-14T21:12:16.681+0000",
                    "votes": {},
                    "watches": {
                        "watchCount": 5
                    },
                    "summary": "Determine MBS hang issue",
                    "project": {
                        "projectCategory": {
                            "description": "Tooling projects",
                            "name": "PnT DevOps Dev"
                        },
                        "name": "Factory 2.0",
                        "key": "FACTORY"
                    },
                    "assignee": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    },
                    "issuetype": {
                        "description": "A problem which impairs functions.",
                        "name": "Bug"
                    },
                    "resolution": {},
                    "reporter": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    }
                },
                "key": "FACTORY-2904"
            },
            "user": {
                "emailAddress": "rbean+red-user@redhat.com",
                "self":
                "https://projects.engineering.redhat.com/rest/api/2/"
                "user?username=red-user",
                "displayName": "red-user",
                "name": "red-user",
                "timeZone": "Europe/London"
            },
            "changelog": {
                "items": [
                    {
                        "field": "Product Affects Version",
                        "toString": "rhel-8.0,fedora-x",
                        "fieldtype": "custom",
                        "to": "[11704, 11626]"
                    }
                ]
            }
        }
    }

class TestJIRAIssueAddComment(fedmsg.tests.test_meta.Base):
    """JIRA is issue tracking system

    Messages (like the example given here) are published when issue is
    updated by posting a new comment.
    """
    expected_title = 'jira.comment.added'
    expected_subti = 'Bill Rainford added new comment in JIRA issue FACTORY-2904.'
    expected_link = ('https://projects.engineering.redhat.com/browse/'
                     'FACTORY-2904?focusedCommentId=973188')
    expected_packages = set([])
    expected_icon = 'https://projects.engineering.redhat.com/favicon.ico'
    expected_usernames = set(['brainfor', 'rbean', 'red-user'])

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1534777940.0,
        "msg_id":
        "ID:messaging-devops-broker01.web.prod.ext.phx2."
        "redhat.com-37550-1534679656045-2:40012:-1:1:132",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.jira.comment.added",
        "headers": {
            "priority": "4",
            "expires": "1535382740838",
            "event_type": "jira:issue_updated",
            "project": "FACTORY",
            "timestamp": "1534777940838",
            "destination": "/topic/VirtualTopic.eng.jira.comment.added",
            "issue_key": "FACTORY-2904",
            "message-id":
            "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-37550-1534679656045-2:40012:-1:1:132",
            "content-type": "application/json",
            "subscription":
            "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.9.1",
        "msg": {
            "comment": {
                "body": "Added new comment",
                "updateAuthor": {
                    "emailAddress": "brainfor@redhat.com",
                    "displayName": "Bill Rainford",
                    "name": "brainfor",
                    "key": "brainfor",
                    "timeZone": "America/Havana"
                },
                "created": "2018-08-20T18:55:36.524+0000",
                "author": {
                    "emailAddress": "brainfor@redhat.com",
                    "displayName": "Bill Rainford",
                    "name": "brainfor",
                    "key": "brainfor",
                    "timeZone": "America/Havana"
                },
                "updated": "2018-08-20T18:55:36.524+0000",
                "id": "973188"
            },
            "webhookEvent": "jira:issue_updated",
            "issue": {
                "fields": {
                    "status": {
                        "statusCategory": {
                            "colorName": "yellow",
                            "key": "indeterminate",
                            "name": "In Progress"
                        },
                        "description": "This issue is being worked on.",
                        "name": "In Progress"
                    },
                    "updated": "2018-08-20T15:12:20.474+0000",
                    "description": "Some longer description",
                    "creator": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    },
                    "created": "2018-08-14T21:12:16.681+0000",
                    "votes": {},
                    "watches": {
                        "watchCount": 5
                    },
                    "summary": "Determine MBS hang issue",
                    "project": {
                        "projectCategory": {
                            "description": "Tooling projects",
                            "name": "PnT DevOps Dev"
                        },
                        "name": "Factory 2.0",
                        "key": "FACTORY"
                    },
                    "assignee": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    },
                    "issuetype": {
                        "description": "A problem which impairs functions.",
                        "name": "Bug"
                    },
                    "resolution": {},
                    "reporter": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    }
                },
                "key": "FACTORY-2904"
            },
            "user": {
                "emailAddress": "rbean+red-user@redhat.com",
                "self":
                "https://projects.engineering.redhat.com/rest/api/2/"
                "user?username=red-user",
                "displayName": "red-user",
                "name": "red-user",
                "timeZone": "Europe/London"
            },
            "changelog": {
                "items": [
                    {
                        "field": "Product Affects Version",
                        "toString": "rhel-8.0,fedora-x",
                        "fieldtype": "custom",
                        "to": "[11704, 11626]"
                    }
                ]
            }
        }
    }

class TestJIRAIssueEditComment(fedmsg.tests.test_meta.Base):
    """JIRA is issue tracking system

    Messages (like the example given here) are published when issue is
    updated by posting a new comment.
    """
    expected_title = 'jira.comment.updated'
    expected_subti = 'Bill Rainford updated comment in JIRA issue FACTORY-2904.'
    expected_link = ('https://projects.engineering.redhat.com/browse/'
                     'FACTORY-2904?focusedCommentId=973188')
    expected_packages = set([])
    expected_icon = 'https://projects.engineering.redhat.com/favicon.ico'
    expected_usernames = set(['brainfor', 'rbean', 'red-user'])

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1534777940.0,
        "msg_id":
        "ID:messaging-devops-broker01.web.prod.ext.phx2."
        "redhat.com-37550-1534679656045-2:40012:-1:1:132",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.jira.comment.updated",
        "headers": {
            "priority": "4",
            "expires": "1535382740838",
            "event_type": "jira:issue_updated",
            "project": "FACTORY",
            "timestamp": "1534777940838",
            "destination": "/topic/VirtualTopic.eng.jira.comment.updated",
            "issue_key": "FACTORY-2904",
            "message-id":
            "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-37550-1534679656045-2:40012:-1:1:132",
            "content-type": "application/json",
            "subscription":
            "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.9.1",
        "msg": {
            "comment": {
                "body": "Edited comment",
                "updateAuthor": {
                    "emailAddress": "brainfor@redhat.com",
                    "displayName": "Bill Rainford",
                    "name": "brainfor",
                    "key": "brainfor",
                    "timeZone": "America/Havana"
                },
                "created": "2018-08-20T18:55:36.524+0000",
                "author": {
                    "emailAddress": "brainfor@redhat.com",
                    "displayName": "Bill Rainford",
                    "name": "brainfor",
                    "key": "brainfor",
                    "timeZone": "America/Havana"
                },
                "updated": "2018-08-21T18:55:36.524+0000",
                "id": "973188"
            },
            "webhookEvent": "jira:issue_updated",
            "issue": {
                "fields": {
                    "status": {
                        "statusCategory": {
                            "colorName": "yellow",
                            "key": "indeterminate",
                            "name": "In Progress"
                        },
                        "description": "This issue is being worked on.",
                        "name": "In Progress"
                    },
                    "updated": "2018-08-20T15:12:20.474+0000",
                    "description": "Some longer description",
                    "creator": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    },
                    "created": "2018-08-14T21:12:16.681+0000",
                    "votes": {},
                    "watches": {
                        "watchCount": 5
                    },
                    "summary": "Determine MBS hang issue",
                    "project": {
                        "projectCategory": {
                            "description": "Tooling projects",
                            "name": "PnT DevOps Dev"
                        },
                        "name": "Factory 2.0",
                        "key": "FACTORY"
                    },
                    "assignee": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    },
                    "issuetype": {
                        "description": "A problem which impairs functions.",
                        "name": "Bug"
                    },
                    "resolution": {},
                    "reporter": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    }
                },
                "key": "FACTORY-2904"
            },
            "user": {
                "emailAddress": "rbean+red-user@redhat.com",
                "self":
                "https://projects.engineering.redhat.com/rest/api/2/"
                "user?username=red-user",
                "displayName": "red-user",
                "name": "red-user",
                "timeZone": "Europe/London"
            },
            "changelog": {
                "items": [
                    {
                        "field": "Product Affects Version",
                        "toString": "rhel-8.0,fedora-x",
                        "fieldtype": "custom",
                        "to": "[11704, 11626]"
                    }
                ]
            }
        }
    }

class TestJIRAIssueMissingKey(fedmsg.tests.test_meta.Base):
    """JIRA is issue tracking system

    Messages (like the example given here) are published when issue is
    updated by posting a new comment.
    """
    expected_title = 'jira.issue.updated'
    expected_subti = None
    expected_link = None
    expected_packages = set([])
    expected_icon = 'https://projects.engineering.redhat.com/favicon.ico'
    expected_usernames = set(['brainfor', 'rbean', 'red-user'])

    msg = {
        "username": None,
        "source_name": "datanommer",
        "certificate": None,
        "i": 0,
        "timestamp": 1534777940.0,
        "msg_id":
        "ID:messaging-devops-broker01.web.prod.ext.phx2."
        "redhat.com-37550-1534679656045-2:40012:-1:1:132",
        "crypto": None,
        "topic": "/topic/VirtualTopic.eng.jira.issue.updated",
        "headers": {
            "priority": "4",
            "expires": "1535382740838",
            "event_type": "jira:issue_updated",
            "project": "FACTORY",
            "timestamp": "1534777940838",
            "destination": "/topic/VirtualTopic.eng.jira.issue.updated",
            "issue_key": "FACTORY-2904",
            "message-id":
            "ID:messaging-devops-broker01.web.prod.ext.phx2."
            "redhat.com-37550-1534679656045-2:40012:-1:1:132",
            "content-type": "application/json",
            "subscription":
            "/queue/Consumer.client-datanommer.upshift-prod.VirtualTopic.eng.>"
        },
        "signature": None,
        "source_version": "0.9.1",
        "msg": {
            "comment": {
                "body": "Edited comment",
                "updateAuthor": {
                    "emailAddress": "brainfor@redhat.com",
                    "displayName": "Bill Rainford",
                    "name": "brainfor",
                    "key": "brainfor",
                    "timeZone": "America/Havana"
                },
                "created": "2018-08-20T18:55:36.524+0000",
                "author": {
                    "emailAddress": "brainfor@redhat.com",
                    "displayName": "Bill Rainford",
                    "name": "brainfor",
                    "key": "brainfor",
                    "timeZone": "America/Havana"
                },
                "updated": "2018-08-21T18:55:36.524+0000",
                "id": "973188"
            },
            "webhookEvent": "jira:issue_updated",
            "issue": {
                "fields": {
                    "status": {
                        "statusCategory": {
                            "colorName": "yellow",
                            "key": "indeterminate",
                            "name": "In Progress"
                        },
                        "description": "This issue is being worked on.",
                        "name": "In Progress"
                    },
                    "updated": "2018-08-20T15:12:20.474+0000",
                    "description": "Some longer description",
                    "creator": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    },
                    "created": "2018-08-14T21:12:16.681+0000",
                    "votes": {},
                    "watches": {
                        "watchCount": 5
                    },
                    "summary": "Determine MBS hang issue",
                    "project": {
                        "projectCategory": {
                            "description": "Tooling projects",
                            "name": "PnT DevOps Dev"
                        },
                        "name": "Factory 2.0",
                        "key": "FACTORY"
                    },
                    "assignee": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    },
                    "issuetype": {
                        "description": "A problem which impairs functions.",
                        "name": "Bug"
                    },
                    "resolution": {},
                    "reporter": {
                        "displayName": "Ralph Bean",
                        "name": "rbean",
                        "emailAddress": "rbean@redhat.com",
                        "key": "rbean",
                        "active": True,
                        "timeZone": "America/Havana"
                    }
                },
            },
            "user": {
                "emailAddress": "rbean+red-user@redhat.com",
                "self":
                "https://projects.engineering.redhat.com/rest/api/2/"
                "user?username=red-user",
                "displayName": "red-user",
                "name": "red-user",
                "timeZone": "Europe/London"
            },
            "changelog": {
                "items": [
                    {
                        "field": "Product Affects Version",
                        "toString": "rhel-8.0,fedora-x",
                        "fieldtype": "custom",
                        "to": "[11704, 11626]"
                    }
                ]
            }
        }
    }

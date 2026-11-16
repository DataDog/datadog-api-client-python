# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IssueImpactViewCounts(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "accounts": (int,),
            "sessions": (int,),
            "users": (int,),
            "views": (int,),
        }

    attribute_map = {
        "accounts": "accounts",
        "sessions": "sessions",
        "users": "users",
        "views": "views",
    }

    def __init__(self_, accounts: int, sessions: int, users: int, views: int, **kwargs):
        """
        Distinct users, accounts, sessions, and view instances on a view. ``affected`` counts only those with the issue's
        errors. ``baseline`` counts all users, accounts, sessions, and view instances on the view in the time window. It
        is absent when RUM has no data for the view.

        :param accounts: Number of distinct accounts.
        :type accounts: int

        :param sessions: Number of distinct sessions.
        :type sessions: int

        :param users: Number of distinct users.
        :type users: int

        :param views: Number of distinct view instances.
        :type views: int
        """
        super().__init__(kwargs)

        self_.accounts = accounts
        self_.sessions = sessions
        self_.users = users
        self_.views = views

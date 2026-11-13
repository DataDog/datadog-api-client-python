# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue_impact_accounts import IssueImpactAccounts
    from datadog_api_client.v2.model.issue_impact_endpoints import IssueImpactEndpoints
    from datadog_api_client.v2.model.issue_impact_error_counts import IssueImpactErrorCounts
    from datadog_api_client.v2.model.issue_impact_sessions import IssueImpactSessions
    from datadog_api_client.v2.model.issue_impact_users import IssueImpactUsers
    from datadog_api_client.v2.model.issue_impact_views import IssueImpactViews


class IssueImpactAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_impact_accounts import IssueImpactAccounts
        from datadog_api_client.v2.model.issue_impact_endpoints import IssueImpactEndpoints
        from datadog_api_client.v2.model.issue_impact_error_counts import IssueImpactErrorCounts
        from datadog_api_client.v2.model.issue_impact_sessions import IssueImpactSessions
        from datadog_api_client.v2.model.issue_impact_users import IssueImpactUsers
        from datadog_api_client.v2.model.issue_impact_views import IssueImpactViews

        return {
            "accounts": (IssueImpactAccounts,),
            "endpoints": (IssueImpactEndpoints,),
            "error_counts": (IssueImpactErrorCounts,),
            "sessions": (IssueImpactSessions,),
            "users": (IssueImpactUsers,),
            "views": (IssueImpactViews,),
        }

    attribute_map = {
        "accounts": "accounts",
        "endpoints": "endpoints",
        "error_counts": "error_counts",
        "sessions": "sessions",
        "users": "users",
        "views": "views",
    }

    def __init__(
        self_,
        accounts: IssueImpactAccounts,
        endpoints: IssueImpactEndpoints,
        error_counts: IssueImpactErrorCounts,
        sessions: IssueImpactSessions,
        users: IssueImpactUsers,
        views: IssueImpactViews,
        **kwargs,
    ):
        """
        The issue's errors in the time window, and the users, sessions, accounts, views, and endpoints they affect.

        :param accounts: Accounts whose users are affected by the issue.
        :type accounts: IssueImpactAccounts

        :param endpoints: Endpoints whose traces have the issue's errors, identified by each trace's root span.
        :type endpoints: IssueImpactEndpoints

        :param error_counts: Number of errors reported by each source. Several sources can report the same error, such as an APM span and
            a log, so the counts overlap: don't add them together.
        :type error_counts: IssueImpactErrorCounts

        :param sessions: RUM sessions where the issue occurred.
        :type sessions: IssueImpactSessions

        :param users: Users affected by the issue.
        :type users: IssueImpactUsers

        :param views: RUM views where the issue occurred.
        :type views: IssueImpactViews
        """
        super().__init__(kwargs)

        self_.accounts = accounts
        self_.endpoints = endpoints
        self_.error_counts = error_counts
        self_.sessions = sessions
        self_.users = users
        self_.views = views

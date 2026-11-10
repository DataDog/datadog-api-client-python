# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue_assignee_relationship import IssueAssigneeRelationship
    from datadog_api_client.v2.model.issue_bits_investigation_relationship import IssueBitsInvestigationRelationship
    from datadog_api_client.v2.model.issue_case_relationship import IssueCaseRelationship
    from datadog_api_client.v2.model.issue_pull_requests_relationship import IssuePullRequestsRelationship
    from datadog_api_client.v2.model.issue_samples_relationship import IssueSamplesRelationship
    from datadog_api_client.v2.model.issue_team_owners_relationship import IssueTeamOwnersRelationship
    from datadog_api_client.v2.model.issue_watches_relationship import IssueWatchesRelationship


class IssueRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_assignee_relationship import IssueAssigneeRelationship
        from datadog_api_client.v2.model.issue_bits_investigation_relationship import IssueBitsInvestigationRelationship
        from datadog_api_client.v2.model.issue_case_relationship import IssueCaseRelationship
        from datadog_api_client.v2.model.issue_pull_requests_relationship import IssuePullRequestsRelationship
        from datadog_api_client.v2.model.issue_samples_relationship import IssueSamplesRelationship
        from datadog_api_client.v2.model.issue_team_owners_relationship import IssueTeamOwnersRelationship
        from datadog_api_client.v2.model.issue_watches_relationship import IssueWatchesRelationship

        return {
            "assignee": (IssueAssigneeRelationship,),
            "bits_investigation": (IssueBitsInvestigationRelationship,),
            "case": (IssueCaseRelationship,),
            "pull_requests": (IssuePullRequestsRelationship,),
            "samples": (IssueSamplesRelationship,),
            "team_owners": (IssueTeamOwnersRelationship,),
            "watches": (IssueWatchesRelationship,),
        }

    attribute_map = {
        "assignee": "assignee",
        "bits_investigation": "bits_investigation",
        "case": "case",
        "pull_requests": "pull_requests",
        "samples": "samples",
        "team_owners": "team_owners",
        "watches": "watches",
    }

    def __init__(
        self_,
        assignee: Union[IssueAssigneeRelationship, UnsetType] = unset,
        bits_investigation: Union[IssueBitsInvestigationRelationship, UnsetType] = unset,
        case: Union[IssueCaseRelationship, UnsetType] = unset,
        pull_requests: Union[IssuePullRequestsRelationship, UnsetType] = unset,
        samples: Union[IssueSamplesRelationship, UnsetType] = unset,
        team_owners: Union[IssueTeamOwnersRelationship, UnsetType] = unset,
        watches: Union[IssueWatchesRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationship between the issue and other resources, such as an assignee, case, teams, pull requests, watches, samples, or a Bits AI investigation.

        :param assignee: Relationship between the issue and assignee.
        :type assignee: IssueAssigneeRelationship, optional

        :param bits_investigation: Bits AI investigation linked to the issue, returned when ``bits_investigation`` is requested
            in the ``include`` query parameter.
        :type bits_investigation: IssueBitsInvestigationRelationship, optional

        :param case: Relationship between the issue and case.
        :type case: IssueCaseRelationship, optional

        :param pull_requests: Relationship between the issue and its linked pull requests. Returned when ``pull_requests`` is included and the issue has linked pull requests.
        :type pull_requests: IssuePullRequestsRelationship, optional

        :param samples: Relationship between the issue and its curated error samples.
        :type samples: IssueSamplesRelationship, optional

        :param team_owners: Relationship between the issue and teams.
        :type team_owners: IssueTeamOwnersRelationship, optional

        :param watches: Relationship between the issue and its active watches. Returned when ``watches`` is included and the issue has an active watch.
        :type watches: IssueWatchesRelationship, optional
        """
        if assignee is not unset:
            kwargs["assignee"] = assignee
        if bits_investigation is not unset:
            kwargs["bits_investigation"] = bits_investigation
        if case is not unset:
            kwargs["case"] = case
        if pull_requests is not unset:
            kwargs["pull_requests"] = pull_requests
        if samples is not unset:
            kwargs["samples"] = samples
        if team_owners is not unset:
            kwargs["team_owners"] = team_owners
        if watches is not unset:
            kwargs["watches"] = watches
        super().__init__(kwargs)

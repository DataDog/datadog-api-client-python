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
    from datadog_api_client.v2.model.issue_case_relationship import IssueCaseRelationship
    from datadog_api_client.v2.model.issue_samples_relationship import IssueSamplesRelationship
    from datadog_api_client.v2.model.issue_team_owners_relationship import IssueTeamOwnersRelationship


class IssueRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_assignee_relationship import IssueAssigneeRelationship
        from datadog_api_client.v2.model.issue_case_relationship import IssueCaseRelationship
        from datadog_api_client.v2.model.issue_samples_relationship import IssueSamplesRelationship
        from datadog_api_client.v2.model.issue_team_owners_relationship import IssueTeamOwnersRelationship

        return {
            "assignee": (IssueAssigneeRelationship,),
            "case": (IssueCaseRelationship,),
            "samples": (IssueSamplesRelationship,),
            "team_owners": (IssueTeamOwnersRelationship,),
        }

    attribute_map = {
        "assignee": "assignee",
        "case": "case",
        "samples": "samples",
        "team_owners": "team_owners",
    }

    def __init__(
        self_,
        assignee: Union[IssueAssigneeRelationship, UnsetType] = unset,
        case: Union[IssueCaseRelationship, UnsetType] = unset,
        samples: Union[IssueSamplesRelationship, UnsetType] = unset,
        team_owners: Union[IssueTeamOwnersRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationship between the issue and an assignee, case and/or teams.

        :param assignee: Relationship between the issue and assignee.
        :type assignee: IssueAssigneeRelationship, optional

        :param case: Relationship between the issue and case.
        :type case: IssueCaseRelationship, optional

        :param samples: Relationship between the issue and its curated error samples.
        :type samples: IssueSamplesRelationship, optional

        :param team_owners: Relationship between the issue and teams.
        :type team_owners: IssueTeamOwnersRelationship, optional
        """
        if assignee is not unset:
            kwargs["assignee"] = assignee
        if case is not unset:
            kwargs["case"] = case
        if samples is not unset:
            kwargs["samples"] = samples
        if team_owners is not unset:
            kwargs["team_owners"] = team_owners
        super().__init__(kwargs)

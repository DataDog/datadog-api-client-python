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
    from datadog_api_client.v2.model.issue_team_type import IssueTeamType


class IssueTeamReference(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_team_type import IssueTeamType

        return {
            "id": (str,),
            "type": (IssueTeamType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: IssueTeamType, **kwargs):
        """
        A team that owns the issue.

        :param id: Team identifier.
        :type id: str

        :param type: Type of the object.
        :type type: IssueTeamType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

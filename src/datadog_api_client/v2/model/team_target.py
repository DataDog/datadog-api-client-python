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
    from datadog_api_client.v2.model.team_target_type import TeamTargetType


class TeamTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_target_type import TeamTargetType

        return {
            "id": (str,),
            "type": (TeamTargetType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: TeamTargetType, **kwargs):
        """
        Represents a team target for an escalation policy step, including the team's ID and resource type.

        :param id: Specifies the unique identifier of the team resource.
        :type id: str

        :param type: Indicates that the resource is of type ``teams``.
        :type type: TeamTargetType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

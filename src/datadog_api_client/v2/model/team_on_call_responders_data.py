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
    from datadog_api_client.v2.model.team_on_call_responders_data_relationships import (
        TeamOnCallRespondersDataRelationships,
    )
    from datadog_api_client.v2.model.team_on_call_responders_data_type import TeamOnCallRespondersDataType


class TeamOnCallRespondersData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_on_call_responders_data_relationships import (
            TeamOnCallRespondersDataRelationships,
        )
        from datadog_api_client.v2.model.team_on_call_responders_data_type import TeamOnCallRespondersDataType

        return {
            "id": (str,),
            "relationships": (TeamOnCallRespondersDataRelationships,),
            "type": (TeamOnCallRespondersDataType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: TeamOnCallRespondersDataType,
        id: Union[str, UnsetType] = unset,
        relationships: Union[TeamOnCallRespondersDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``TeamOnCallRespondersData`` object.

        :param id: The ``TeamOnCallRespondersData`` ``id``.
        :type id: str, optional

        :param relationships: The definition of ``TeamOnCallRespondersDataRelationships`` object.
        :type relationships: TeamOnCallRespondersDataRelationships, optional

        :param type: Team oncall responders resource type.
        :type type: TeamOnCallRespondersDataType
        """
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type

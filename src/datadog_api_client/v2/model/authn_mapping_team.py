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
    from datadog_api_client.v2.model.authn_mapping_team_attributes import AuthNMappingTeamAttributes
    from datadog_api_client.v2.model.team_type import TeamType


class AuthNMappingTeam(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.authn_mapping_team_attributes import AuthNMappingTeamAttributes
        from datadog_api_client.v2.model.team_type import TeamType

        return {
            "attributes": (AuthNMappingTeamAttributes,),
            "id": (str,),
            "type": (TeamType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[AuthNMappingTeamAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[TeamType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Team.

        :param attributes: Team attributes.
        :type attributes: AuthNMappingTeamAttributes, optional

        :param id: The ID of the Team.
        :type id: str, optional

        :param type: Team type
        :type type: TeamType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

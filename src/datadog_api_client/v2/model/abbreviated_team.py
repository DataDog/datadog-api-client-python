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
    from datadog_api_client.v2.model.abbreviated_team_attributes import AbbreviatedTeamAttributes
    from datadog_api_client.v2.model.abbreviated_team_type import AbbreviatedTeamType


class AbbreviatedTeam(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.abbreviated_team_attributes import AbbreviatedTeamAttributes
        from datadog_api_client.v2.model.abbreviated_team_type import AbbreviatedTeamType

        return {
            "attributes": (AbbreviatedTeamAttributes,),
            "id": (str,),
            "type": (AbbreviatedTeamType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AbbreviatedTeamAttributes,
        type: AbbreviatedTeamType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``AbbreviatedTeam`` object.

        :param attributes: The definition of ``AbbreviatedTeamAttributes`` object.
        :type attributes: AbbreviatedTeamAttributes

        :param id: ID of the team
        :type id: str, optional

        :param type: The definition of ``AbbreviatedTeamType`` object.
        :type type: AbbreviatedTeamType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

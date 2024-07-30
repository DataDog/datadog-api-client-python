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
    from datadog_api_client.v2.model.team_link_attributes import TeamLinkAttributes
    from datadog_api_client.v2.model.team_link_type import TeamLinkType


class TeamLink(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_link_attributes import TeamLinkAttributes
        from datadog_api_client.v2.model.team_link_type import TeamLinkType

        return {
            "attributes": (TeamLinkAttributes,),
            "id": (str,),
            "type": (TeamLinkType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: TeamLinkAttributes, type: TeamLinkType, id: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Team link

        :param attributes: Team link attributes
        :type attributes: TeamLinkAttributes

        :param id: The team link's identifier
        :type id: str, optional

        :param type: Team link type
        :type type: TeamLinkType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type

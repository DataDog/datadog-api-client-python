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
    from datadog_api_client.v2.model.team_on_call_responders_data_relationships_responders_data_items_type import (
        TeamOnCallRespondersDataRelationshipsRespondersDataItemsType,
    )


class TeamOnCallRespondersDataRelationshipsRespondersDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_on_call_responders_data_relationships_responders_data_items_type import (
            TeamOnCallRespondersDataRelationshipsRespondersDataItemsType,
        )

        return {
            "id": (str,),
            "type": (TeamOnCallRespondersDataRelationshipsRespondersDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: TeamOnCallRespondersDataRelationshipsRespondersDataItemsType, **kwargs):
        """
        Represents a user responder associated with the on-call team.

        :param id: Unique identifier of the responder.
        :type id: str

        :param type: Identifies the resource type for individual user entities associated with on-call response.
        :type type: TeamOnCallRespondersDataRelationshipsRespondersDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

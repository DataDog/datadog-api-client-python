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
    from datadog_api_client.v2.model.team_on_call_responders_data_relationships_escalations_data_items_type import (
        TeamOnCallRespondersDataRelationshipsEscalationsDataItemsType,
    )


class TeamOnCallRespondersDataRelationshipsEscalationsDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_on_call_responders_data_relationships_escalations_data_items_type import (
            TeamOnCallRespondersDataRelationshipsEscalationsDataItemsType,
        )

        return {
            "id": (str,),
            "type": (TeamOnCallRespondersDataRelationshipsEscalationsDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: TeamOnCallRespondersDataRelationshipsEscalationsDataItemsType, **kwargs):
        """
        Represents a link to a specific escalation policy step associated with the on-call team.

        :param id: Unique identifier of the escalation step.
        :type id: str

        :param type: Identifies the resource type for escalation policy steps linked to a team's on-call configuration.
        :type type: TeamOnCallRespondersDataRelationshipsEscalationsDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

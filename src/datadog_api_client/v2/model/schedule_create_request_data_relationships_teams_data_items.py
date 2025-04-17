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
    from datadog_api_client.v2.model.schedule_create_request_data_relationships_teams_data_items_type import (
        ScheduleCreateRequestDataRelationshipsTeamsDataItemsType,
    )


class ScheduleCreateRequestDataRelationshipsTeamsDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_create_request_data_relationships_teams_data_items_type import (
            ScheduleCreateRequestDataRelationshipsTeamsDataItemsType,
        )

        return {
            "id": (str,),
            "type": (ScheduleCreateRequestDataRelationshipsTeamsDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ScheduleCreateRequestDataRelationshipsTeamsDataItemsType, **kwargs):
        """
        Holds the relationship data linking this schedule to a particular team,
        identified by ``id`` and ``type``.

        :param id: A unique identifier for the team.
        :type id: str

        :param type: Teams resource type.
        :type type: ScheduleCreateRequestDataRelationshipsTeamsDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

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
    from datadog_api_client.v2.model.schedule_data_relationships_layers_data_items_type import (
        ScheduleDataRelationshipsLayersDataItemsType,
    )


class ScheduleDataRelationshipsLayersDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_data_relationships_layers_data_items_type import (
            ScheduleDataRelationshipsLayersDataItemsType,
        )

        return {
            "id": (str,),
            "type": (ScheduleDataRelationshipsLayersDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: ScheduleDataRelationshipsLayersDataItemsType, **kwargs):
        """
        Relates a layer to this schedule, identified by ``id`` and ``type`` (must be ``layers`` ).

        :param id: The unique identifier of the layer in this relationship.
        :type id: str

        :param type: Layers resource type.
        :type type: ScheduleDataRelationshipsLayersDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type

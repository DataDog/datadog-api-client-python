# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.schedule_data_relationships_layers_data_items import (
        ScheduleDataRelationshipsLayersDataItems,
    )


class ScheduleDataRelationshipsLayers(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_data_relationships_layers_data_items import (
            ScheduleDataRelationshipsLayersDataItems,
        )

        return {
            "data": ([ScheduleDataRelationshipsLayersDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[ScheduleDataRelationshipsLayersDataItems], UnsetType] = unset, **kwargs):
        """
        Associates layers with this schedule in a data structure.

        :param data: An array of layer references for this schedule.
        :type data: [ScheduleDataRelationshipsLayersDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)

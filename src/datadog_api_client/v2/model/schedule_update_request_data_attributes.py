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
    from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items import (
        ScheduleUpdateRequestDataAttributesLayersItems,
    )


class ScheduleUpdateRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items import (
            ScheduleUpdateRequestDataAttributesLayersItems,
        )

        return {
            "layers": ([ScheduleUpdateRequestDataAttributesLayersItems],),
            "name": (str,),
            "tags": ([str],),
            "time_zone": (str,),
        }

    attribute_map = {
        "layers": "layers",
        "name": "name",
        "tags": "tags",
        "time_zone": "time_zone",
    }

    def __init__(
        self_,
        layers: List[ScheduleUpdateRequestDataAttributesLayersItems],
        name: str,
        time_zone: str,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines the updatable attributes for a schedule, such as name, time zone, tags, and layers.

        :param layers: The updated list of layers (rotations) for this schedule.
        :type layers: [ScheduleUpdateRequestDataAttributesLayersItems]

        :param name: A short name for the schedule.
        :type name: str

        :param tags: A list of tags that you can associate with this schedule.
        :type tags: [str], optional

        :param time_zone: The time zone used when interpreting rotation times.
        :type time_zone: str
        """
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.layers = layers
        self_.name = name
        self_.time_zone = time_zone

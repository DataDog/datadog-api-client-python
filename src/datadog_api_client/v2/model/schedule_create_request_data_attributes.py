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
    from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items import (
        ScheduleCreateRequestDataAttributesLayersItems,
    )


class ScheduleCreateRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items import (
            ScheduleCreateRequestDataAttributesLayersItems,
        )

        return {
            "layers": ([ScheduleCreateRequestDataAttributesLayersItems],),
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
        layers: List[ScheduleCreateRequestDataAttributesLayersItems],
        name: str,
        time_zone: str,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Describes the main attributes for creating a new schedule, including name, layers, time zone, and tags.

        :param layers: The layers of on-call coverage that define rotation intervals and restrictions.
        :type layers: [ScheduleCreateRequestDataAttributesLayersItems]

        :param name: A human-readable name for the new schedule.
        :type name: str

        :param tags: A list of tags for categorizing or filtering the schedule.
        :type tags: [str], optional

        :param time_zone: The time zone in which the schedule is defined.
        :type time_zone: str
        """
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.layers = layers
        self_.name = name
        self_.time_zone = time_zone

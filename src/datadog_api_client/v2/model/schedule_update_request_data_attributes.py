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
    validations = {
        "max_responders": {
            "inclusive_maximum": 10,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items import (
            ScheduleUpdateRequestDataAttributesLayersItems,
        )

        return {
            "layers": ([ScheduleUpdateRequestDataAttributesLayersItems],),
            "max_responders": (int,),
            "name": (str,),
            "time_zone": (str,),
        }

    attribute_map = {
        "layers": "layers",
        "max_responders": "max_responders",
        "name": "name",
        "time_zone": "time_zone",
    }

    def __init__(
        self_,
        layers: List[ScheduleUpdateRequestDataAttributesLayersItems],
        name: str,
        time_zone: str,
        max_responders: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines the updatable attributes for a schedule, such as name, time zone, and layers.

        :param layers: The updated list of layers (rotations) for this schedule.
        :type layers: [ScheduleUpdateRequestDataAttributesLayersItems]

        :param max_responders: Maximum number of users who can be on call at the same time.
            The value must be between 1 and the number of layers, and no greater than 10.
        :type max_responders: int, optional

        :param name: A short name for the schedule.
        :type name: str

        :param time_zone: The time zone used when interpreting rotation times.
        :type time_zone: str
        """
        if max_responders is not unset:
            kwargs["max_responders"] = max_responders
        super().__init__(kwargs)

        self_.layers = layers
        self_.name = name
        self_.time_zone = time_zone

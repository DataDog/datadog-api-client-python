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
    validations = {
        "max_responders": {
            "inclusive_maximum": 10,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items import (
            ScheduleCreateRequestDataAttributesLayersItems,
        )

        return {
            "layers": ([ScheduleCreateRequestDataAttributesLayersItems],),
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
        layers: List[ScheduleCreateRequestDataAttributesLayersItems],
        name: str,
        time_zone: str,
        max_responders: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Describes the main attributes for creating a new schedule, including name, layers, and time zone.

        :param layers: The layers of On-Call coverage that define rotation intervals and restrictions.
        :type layers: [ScheduleCreateRequestDataAttributesLayersItems]

        :param max_responders: Maximum number of users who can be on call at the same time.
            The value must be between 1 and the number of layers, and no greater than 10.
        :type max_responders: int, optional

        :param name: A human-readable name for the new schedule.
        :type name: str

        :param time_zone: The time zone in which the schedule is defined.
        :type time_zone: str
        """
        if max_responders is not unset:
            kwargs["max_responders"] = max_responders
        super().__init__(kwargs)

        self_.layers = layers
        self_.name = name
        self_.time_zone = time_zone

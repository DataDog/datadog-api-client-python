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
    from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items_restrictions_items_end_day import (
        ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay,
    )
    from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items_restrictions_items_start_day import (
        ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay,
    )


class ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items_restrictions_items_end_day import (
            ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay,
        )
        from datadog_api_client.v2.model.schedule_create_request_data_attributes_layers_items_restrictions_items_start_day import (
            ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay,
        )

        return {
            "end_day": (ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay,),
            "end_time": (str,),
            "start_day": (ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay,),
            "start_time": (str,),
        }

    attribute_map = {
        "end_day": "end_day",
        "end_time": "end_time",
        "start_day": "start_day",
        "start_time": "start_time",
    }

    def __init__(
        self_,
        end_day: Union[ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay, UnsetType] = unset,
        end_time: Union[str, UnsetType] = unset,
        start_day: Union[ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay, UnsetType] = unset,
        start_time: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines a time restriction for a schedule layer, including which day of the week
        it starts and ends, along with start/end times.

        :param end_day: The weekday when the restriction period ends (Monday through Sunday).
        :type end_day: ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsEndDay, optional

        :param end_time: The time of day when the restriction ends (hh:mm:ss).
        :type end_time: str, optional

        :param start_day: The weekday when the restriction period starts (Monday through Sunday).
        :type start_day: ScheduleCreateRequestDataAttributesLayersItemsRestrictionsItemsStartDay, optional

        :param start_time: The time of day when the restriction begins (hh:mm:ss).
        :type start_time: str, optional
        """
        if end_day is not unset:
            kwargs["end_day"] = end_day
        if end_time is not unset:
            kwargs["end_time"] = end_time
        if start_day is not unset:
            kwargs["start_day"] = start_day
        if start_time is not unset:
            kwargs["start_time"] = start_time
        super().__init__(kwargs)

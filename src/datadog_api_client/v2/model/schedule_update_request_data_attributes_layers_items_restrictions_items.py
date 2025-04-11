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
    from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_restrictions_items_end_day import (
        ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay,
    )
    from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_restrictions_items_start_day import (
        ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay,
    )


class ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_restrictions_items_end_day import (
            ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay,
        )
        from datadog_api_client.v2.model.schedule_update_request_data_attributes_layers_items_restrictions_items_start_day import (
            ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay,
        )

        return {
            "end_day": (ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay,),
            "end_time": (str,),
            "start_day": (ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay,),
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
        end_day: Union[ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay, UnsetType] = unset,
        end_time: Union[str, UnsetType] = unset,
        start_day: Union[ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay, UnsetType] = unset,
        start_time: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines a time restriction object for a layer within a schedule update, including
        start and end days, as well as times.

        :param end_day: Defines the day of the week on which the time restriction ends.
        :type end_day: ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsEndDay, optional

        :param end_time: The time at which this restriction ends (hh:mm:ss).
        :type end_time: str, optional

        :param start_day: Defines the day of the week on which the time restriction starts.
        :type start_day: ScheduleUpdateRequestDataAttributesLayersItemsRestrictionsItemsStartDay, optional

        :param start_time: The time at which this restriction starts (hh:mm:ss).
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

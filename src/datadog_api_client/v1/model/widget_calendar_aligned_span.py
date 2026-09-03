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
    from datadog_api_client.v1.model.widget_calendar_aligned_span_type import WidgetCalendarAlignedSpanType


class WidgetCalendarAlignedSpan(ModelNormal):
    validations = {
        "offset": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_calendar_aligned_span_type import WidgetCalendarAlignedSpanType

        return {
            "hide_incomplete_cost_data": (bool,),
            "offset": (int,),
            "timezone": (str,),
            "type": (WidgetCalendarAlignedSpanType,),
        }

    attribute_map = {
        "hide_incomplete_cost_data": "hide_incomplete_cost_data",
        "offset": "offset",
        "timezone": "timezone",
        "type": "type",
    }

    def __init__(
        self_,
        offset: int,
        type: WidgetCalendarAlignedSpanType,
        hide_incomplete_cost_data: Union[bool, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Used for calendar-aligned time spans, such as the current month or previous year.

        :param hide_incomplete_cost_data: Whether to hide incomplete cost data in the widget.
        :type hide_incomplete_cost_data: bool, optional

        :param offset: Number of completed periods before the current period. 0 represents the current period.
        :type offset: int

        :param timezone: Time zone used to align the calendar period.
        :type timezone: str, optional

        :param type: Calendar-aligned time span type.
        :type type: WidgetCalendarAlignedSpanType
        """
        if hide_incomplete_cost_data is not unset:
            kwargs["hide_incomplete_cost_data"] = hide_incomplete_cost_data
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)

        self_.offset = offset
        self_.type = type

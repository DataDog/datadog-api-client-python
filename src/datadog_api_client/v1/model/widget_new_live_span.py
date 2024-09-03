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
    from datadog_api_client.v1.model.widget_new_live_span_type import WidgetNewLiveSpanType
    from datadog_api_client.v1.model.widget_live_span_unit import WidgetLiveSpanUnit


class WidgetNewLiveSpan(ModelNormal):
    validations = {
        "value": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_new_live_span_type import WidgetNewLiveSpanType
        from datadog_api_client.v1.model.widget_live_span_unit import WidgetLiveSpanUnit

        return {
            "type": (WidgetNewLiveSpanType,),
            "unit": (WidgetLiveSpanUnit,),
            "value": (int,),
        }

    attribute_map = {
        "type": "type",
        "unit": "unit",
        "value": "value",
    }

    def __init__(self_, type: WidgetNewLiveSpanType, unit: WidgetLiveSpanUnit, value: int, **kwargs):
        """
        Used for arbitrary live span times, such as 17 minutes or 6 hours.

        :param type: Type "live" denotes a live span in the new format.
        :type type: WidgetNewLiveSpanType

        :param unit: Unit of the time span.
        :type unit: WidgetLiveSpanUnit

        :param value: Value of the time span.
        :type value: int
        """
        super().__init__(kwargs)

        self_.type = type
        self_.unit = unit
        self_.value = value

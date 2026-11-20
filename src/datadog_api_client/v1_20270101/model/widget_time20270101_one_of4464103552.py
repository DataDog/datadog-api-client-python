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
    from datadog_api_client.v1_20270101.model.widget_new_live_span_type import WidgetNewLiveSpanType


class WidgetTime20270101OneOf4464103552(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_new_live_span_type import WidgetNewLiveSpanType

        return {
            "hide_incomplete_cost_data": (bool,),
            "type": (WidgetNewLiveSpanType,),
            "unit": (str,),
            "value": (float,),
        }

    attribute_map = {
        "hide_incomplete_cost_data": "hide_incomplete_cost_data",
        "type": "type",
        "unit": "unit",
        "value": "value",
    }

    def __init__(
        self_,
        type: WidgetNewLiveSpanType,
        unit: str,
        value: float,
        hide_incomplete_cost_data: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param hide_incomplete_cost_data: Test-only generated schema for the dashboard versioning proof of concept.
        :type hide_incomplete_cost_data: bool, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: WidgetNewLiveSpanType

        :param unit: Test-only generated schema for the dashboard versioning proof of concept.
        :type unit: str

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: float
        """
        if hide_incomplete_cost_data is not unset:
            kwargs["hide_incomplete_cost_data"] = hide_incomplete_cost_data
        super().__init__(kwargs)

        self_.type = type
        self_.unit = unit
        self_.value = value

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
    from datadog_api_client.v1.model.widget_live_span import WidgetLiveSpan


class WidgetLegacyLiveSpan(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_live_span import WidgetLiveSpan

        return {
            "hide_incomplete_cost_data": (bool,),
            "live_span": (WidgetLiveSpan,),
        }

    attribute_map = {
        "hide_incomplete_cost_data": "hide_incomplete_cost_data",
        "live_span": "live_span",
    }

    def __init__(
        self_,
        hide_incomplete_cost_data: Union[bool, UnsetType] = unset,
        live_span: Union[WidgetLiveSpan, UnsetType] = unset,
        **kwargs,
    ):
        """
        Wrapper for live span

        :param hide_incomplete_cost_data: Whether to hide incomplete cost data in the widget.
        :type hide_incomplete_cost_data: bool, optional

        :param live_span: The available timeframes depend on the widget you are using.
        :type live_span: WidgetLiveSpan, optional
        """
        if hide_incomplete_cost_data is not unset:
            kwargs["hide_incomplete_cost_data"] = hide_incomplete_cost_data
        if live_span is not unset:
            kwargs["live_span"] = live_span
        super().__init__(kwargs)

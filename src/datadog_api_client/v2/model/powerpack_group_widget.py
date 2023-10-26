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
    from datadog_api_client.v2.model.powerpack_group_widget_definition import PowerpackGroupWidgetDefinition
    from datadog_api_client.v2.model.powerpack_group_widget_layout import PowerpackGroupWidgetLayout
    from datadog_api_client.v2.model.widget_live_span import WidgetLiveSpan


class PowerpackGroupWidget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.powerpack_group_widget_definition import PowerpackGroupWidgetDefinition
        from datadog_api_client.v2.model.powerpack_group_widget_layout import PowerpackGroupWidgetLayout
        from datadog_api_client.v2.model.widget_live_span import WidgetLiveSpan

        return {
            "definition": (PowerpackGroupWidgetDefinition,),
            "layout": (PowerpackGroupWidgetLayout,),
            "live_span": (WidgetLiveSpan,),
        }

    attribute_map = {
        "definition": "definition",
        "layout": "layout",
        "live_span": "live_span",
    }

    def __init__(
        self_,
        definition: PowerpackGroupWidgetDefinition,
        layout: Union[PowerpackGroupWidgetLayout, UnsetType] = unset,
        live_span: Union[WidgetLiveSpan, UnsetType] = unset,
        **kwargs,
    ):
        """
        Powerpack group widget definition object.

        :param definition: Powerpack group widget object.
        :type definition: PowerpackGroupWidgetDefinition

        :param layout: Powerpack group widget layout.
        :type layout: PowerpackGroupWidgetLayout, optional

        :param live_span: The available timeframes depend on the widget you are using.
        :type live_span: WidgetLiveSpan, optional
        """
        if layout is not unset:
            kwargs["layout"] = layout
        if live_span is not unset:
            kwargs["live_span"] = live_span
        super().__init__(kwargs)

        self_.definition = definition

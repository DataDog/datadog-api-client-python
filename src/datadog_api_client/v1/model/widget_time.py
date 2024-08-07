# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class WidgetTime(ModelComposed):
    def __init__(self, **kwargs):
        """
        Time setting for the widget.

        :param live_span: The available timeframes depend on the widget you are using.
        :type live_span: WidgetLiveSpan, optional

        :param type: Type "live" denotes a live span in the new format.
        :type type: WidgetNewLiveSpanType

        :param unit: Unit of the time span.
        :type unit: WidgetLiveSpanUnit

        :param value: Value of the time span.
        :type value: int

        :param _from: Start time in seconds since epoch.
        :type _from: int

        :param to: End time in seconds since epoch.
        :type to: int
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.widget_legacy_live_span import WidgetLegacyLiveSpan
        from datadog_api_client.v1.model.widget_new_live_span import WidgetNewLiveSpan
        from datadog_api_client.v1.model.widget_new_fixed_span import WidgetNewFixedSpan

        return {
            "oneOf": [
                WidgetLegacyLiveSpan,
                WidgetNewLiveSpan,
                WidgetNewFixedSpan,
            ],
        }
